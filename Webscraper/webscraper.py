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

app_id = 2344520
reviews = get_steam_reviews(app_id)

for review in reviews:
    print(f"Review ID: {review['recommendationid']}")
    print(f"Review Content: {review['review']}")
    print("-" * 40)