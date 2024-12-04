import requests
import os

class SteamApp:
    
    def __init__(self, app_id):
        self.app_id = app_id
        self.name = self.get_game_name()

    def get_game_name(self):
        #uses steamID with steamworks API to get game name
        url = f"https://store.steampowered.com/api/appdetails?appids={self.app_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data[str(self.app_id)]['success']:
                return data[str(self.app_id)]['data']['name']
        return "Unknown Game"

    def get_reviews(self, language='english', num_reviews=2):
        #uses steamID with steamworks API to get game reviews
        url = f"http://store.steampowered.com/appreviews/{self.app_id}"
        parameters = {
            "json": 1,
            "language": language,
            "num_per_page": num_reviews
        }

        response = requests.get(url, params=parameters)
        if response.status_code == 200:
            data = response.json()
            return data.get('reviews', [])
        return []

    def save_reviews(self, output_dir="Webscraper/Reviews"):
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        sanitized_name = self.name.replace(' ', '_')
        output_file = os.path.join(output_dir, f"{sanitized_name}.txt")

        reviews = self.get_reviews()

        with open(output_file, "w", encoding="utf-8") as file:
            if not reviews:
                file.write("No reviews found.\n")
            else:
                for review in reviews:
                    file.write(f"Review ID: {review['recommendationid']}\n")
                    file.write(f"Review Content: {review['review']}\n")
                    file.write("-" * 40 + "\n")
        print(f"Saved reviews for {self.name} to {output_file}")


class SteamReviewScraper:
    
    def __init__(self, input_file):
        self.input_file = input_file

    def parse_app_ids(self):
        #Reads input file to get steamIDs for games
        with open(self.input_file, "r") as file:
            app_ids = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        return app_ids

    def scrape_reviews(self, output_dir="Webscraper/Reviews"):
        #Gets the reviews and saves them to their respective games output file
        app_ids = self.parse_app_ids()
        for app_id in app_ids:
            app = SteamApp(app_id)
            app.save_reviews(output_dir=output_dir)


# Usage example
if __name__ == "__main__":
    input_file = "Webscraper/scraperInputs.txt"
    scraper = SteamReviewScraper(input_file)
    scraper.scrape_reviews()
