import requests
from django.conf import settings

def get_APIrecipe_list(queryString):
    url = "https://tasty.p.rapidapi.com/recipes/list"

    # querystring = {"from":"0","size":"20","tags":"under_30_minutes"}

    headers = {
        "x-rapidapi-key": settings.EXT_API_KEY,
        "x-rapidapi-host": "tasty.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params= queryString)

    if response.status_code == 200:
        return response.json()
    else: response.raise_for_status()

def get_APIrecipe_details(queryString):
    url = "https://tasty.p.rapidapi.com/recipes/get-more-info"
    
    # querystring = {"id":"480"}
    
    headers = {
        "x-rapidapi-key": settings.EXT_API_KEY,
        "x-rapidapi-host": "tasty.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params= queryString)
    # print("Status code:", response.status_code)
    # print("Response content:", response.content)

    if response.status_code == 200:
        return response.json()
    else: response.raise_for_status()

