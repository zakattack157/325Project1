import requests

def get_steam_reviews(app_id, language='english', num_reviews=10):
    url = f"http://store.steampowered.com/appreviews/{app_id}"
    parameters = {
        "json": 1,
        "language": language,
        "num_per_page": num_reviews
    }

    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()
        if 'reviews' in data:
            reviews = data['reviews']
            return reviews
        else:
            return "No reviews found."
    else:
        return f"Failed to retrieve reviews. Status Code: {response.status_code}"

input_file = open("Webscraper/scraperInputs.txt", "r")
num = 1
for line in input_file:
    
    app_id = line.strip()

    if not app_id or app_id.startswith('#'):
        continue

    file = open(f"Webscraper/Reviews/FarCry_{num}.txt", "w")

    num = num + 1
    reviews = get_steam_reviews(app_id)

    for review in reviews:
        file.write(f"Review ID: {review['recommendationid']}\n")
        file.write(f"Review Content: {review['review']}\n")
        file.write("-" * 40 + "\n")
    file.close()