import requests
from django.conf import settings

def get_external_recipe(queryString):
    url = "https://recipe-by-api-ninjas.p.rapidapi.com/v1/recipe"

    headers = {
        "x-rapidapi-key": settings.EXT_API_KEY,
        "x-rapidapi-host": "recipe-by-api-ninjas.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params={"query": queryString})

    if response.status_code == 200:
        return response.json()
    else: response.raise_for_status()