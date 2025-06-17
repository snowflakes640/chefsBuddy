This is a personal project of mine to practice different sides of web app development on my own. It should result in an assistant app to maintain inventory and meal planning.

User should be able to:
- Have an inventory system, see it anytime to know what is in his kitchen currently
- Add, update or remove any item from the system to keep up with his daily purchases and usage
- Search recipes online
- Have a collection of own recipe initially
- Save new recipes and use them later
- Have a recommendation system to suggest recipes based on the available ingredients in his kitchen

At the end it should have a clean
- Backend (Django)
- Recommendation System (donno yet)
- Frontend (React) (MUI)

For **backend**, initially these are my steps:
- [ ] Managing the inventory
	- [x] Creating form to add and update inventory
	- [x] Showcasing the current inventory
	- [x] Showing messages for success and error
	- [ ] Deleting any item
- [x] Connecting to external DBMS (MySQL80) and prepopulating them with collected database
- [x] Getting recipe from API 
	- [x] Integrating the API
	- [x] Showing recipes w search words
	- [x] Showing recipe details when clicked
- [x] Getting Recipe from user
	- [x] Taking the recipe as input
	- [x] Store them in database
	- [x] Showing recipes w search words
	- [x] Showing recipe details when clicked
- [x] Merging the recipe sources
	- [x] Cleaning the external API data into native database schema
	- [x] Merging both the search lists together for the user to get results from both sources
- [x] Creating endpoint for 
	- [x] Showing inventory
	- [x] Adding new item
	- [x] Saving recipe
	- [x] Showing searched recipes

- [ ] Creating authentication system for multiple users

---	
For **Frontend**, tried to keep it simple:
	- [x] Creating separated page for adding item and recipes, showing inventory and search results
	- [x] Maintaining a theme for the whole app using MUI

---
Thinking of implementing **ML system** here
- [ ] Creating a recsystem for user based, inventory-wise recipe

---
- [ ] Extended plans: