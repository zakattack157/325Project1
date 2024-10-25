#Requests import to send get requests to urls
import requests

#Calls the Steamworks API to gather the name of game associated with AppID
def get_game_name(app_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data[str(app_id)]['success']:
            return data[str(app_id)]['data']['name']
        else:
            return "Unknown Game" 
    else:
        return "Failed to retrieve game name"

#Calls Steamworks API to gather user reviews of AppID
def get_steam_reviews(app_id, language='english', num_reviews=10):
    url = f"http://store.steampowered.com/appreviews/{app_id}"
    parameters = {
        "json": 1,
        "language": language,
        "num_per_page": num_reviews
    }

    #Sends get request to Steam store page of requested application to grab user reviews in JSON format
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

#Opens the input file that holds each apps AppID
input_file = open("Webscraper/scraperInputs.txt", "r")

#Reads through each line of the input file ignoring comments starting with '#'
for line in input_file:
    
    app_id = line.strip()

    if not app_id or app_id.startswith('#'):
        continue
    
    #Calls function to grab apps name
    game_name = get_game_name(app_id)

    #Creates output file that will hold the respective apps user reviews
    file = open(f"Webscraper/Reviews/{game_name.replace(' ','_')}.txt", "w")

    
    reviews = get_steam_reviews(app_id)

    #Writes each individual review to their respective output file
    for review in reviews:
        file.write(f"Review ID: {review['recommendationid']}\n")
        file.write(f"Review Content: {review['review']}\n")
        file.write("-" * 40 + "\n")
    file.close()