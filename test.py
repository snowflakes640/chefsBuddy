
import requests
from django.conf import settings
from django.shortcuts import render, Http404

# Assuming you have a function to get the initial list of recipes
def get_initial_recipe_list_from_api(query_params):
    # This function would call your API that returns the list of recipes
    # For example, using a different RapidAPI endpoint like /recipes/list
    list_url = "https://tasty.p.rapidapi.com/recipes/list"
    headers = {
        "x-rapidapi-key": settings.EXT_API_KEY,
        "x-rapidapi-host": "tasty.p.rapidapi.com"
    }
    try:
        response = requests.get(list_url, headers=headers, params=query_params, timeout=10)
        response.raise_for_status() # Raise HTTPError for 4xx/5xx responses
        return response.json().get('results', []) # Assuming results key holds the list
    except requests.exceptions.RequestException as e:
        print(f"Error fetching initial recipe list: {e}")
        return []

def your_list_view(request):
    # Example: fetch some trending recipes or search results
    initial_api_params = {"from": "0", "size": "20", "tags": "under_30_minutes"} # Example params

    raw_recipe_data_list = get_initial_recipe_list_from_api(initial_api_params)

    processed_recipes_for_template = []
    for recipe_item in raw_recipe_data_list:
        canonical_id_full = recipe_item.get('canonical_id') # e.g., "recipe:4180"
        extracted_numeric_id = None

        if canonical_id_full and ":" in canonical_id_full:
            try:
                # Extract the numeric part and convert to string for the URL
                extracted_numeric_id = canonical_id_full.split(":")[1]
                # Ensure it's treated as a string for the URL resolver
                # (even though it's numeric characters)
                extracted_numeric_id = str(extracted_numeric_id)
            except IndexError:
                print(f"Warning: canonical_id '{canonical_id_full}' unexpected format, cannot split.")
                extracted_numeric_id = None # Or handle appropriately
        elif canonical_id_full:
            # If canonical_id exists but doesn't have "recipe:", use it directly
            extracted_numeric_id = str(canonical_id_full)


        # Create a new dictionary for the template to avoid modifying original API response
        processed_recipe = {
            'title': recipe_item.get('name', 'No Title'), # Tasty API uses 'name' for title in list endpoint
            'extracted_id_for_url': extracted_numeric_id, # This is the key for your template
            # Add any other data you need for the list view
        }
        processed_recipes_for_template.append(processed_recipe)

    return render(request, 'recipes/your_recipe_list_template.html', {'recipeData': processed_recipes_for_template})

# --- The extRecipe_details view is separate and remains largely the same ---
# (from previous answers, handling the single detail API call)

def extRecipe_details(request, recipe_id): # recipe_id will be the pure numeric string, e.g., "4180"
    # Convert to integer for the API call
    try:
        api_id = int(recipe_id)
    except ValueError:
        raise Http404("Invalid recipe ID format. Must be an integer.")

    params = {
        "id": api_id # Pass the integer ID to the API
    }

    response_data = get_APIrecipe_details(params) # This is the API call for details

    if response_data is None:
        raise Http404(f"Recipe with ID {api_id} not found or API error.")

    # Process response_data (e.g., getting slug, generating title)
    slug = response_data.get("slug")
    if slug:
        title = slug.replace("-", " ")
        response_data["title"] = title
    else:
        response_data["title"] = "Unknown Recipe"

    return render(request, "recipes/extRrecipe_details.html", {"recipe": response_data})


# The get_APIrecipe_details function (for single recipe details)
def get_APIrecipe_details(queryString):
    url = "https://tasty.p.rapidapi.com/recipes/get-more-info"
    headers = {
        "x-rapidapi-key": settings.EXT_API_KEY,
        "x-rapidapi-host": "tasty.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=queryString, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 204:
            print(f"API returned 204 No Content for ID: {queryString.get('id')}")
            return None
        else:
            response.raise_for_status()
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request to Tasty API failed: {e}")
        return None