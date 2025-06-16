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
- Frontend (React) (hopefully)

For backend I am using Django. Initially these are my steps:
- [ ] Managing the inventory
	- [x] Creating page to add and update inventory
	- [x] Showcasing the current inventory
	- [x] Showing messages for success and error
	- [ ] Deleting any item
- [x] Connecting to external DBMS (MySQL80)
- [x] Getting recipe from API 
	- [x] Integrating the API
	- [x] Showing recipes w search words
	- [x] Showing recipe details when clicked
- [x] Getting Recipe from user
	- [x] Taking the recipe as input
	- [x] Store them in database
	- [x] Showing recipes w search words
	- [x] Showing recipe details when clicked

- [x] Turning this whole thing into a backend endpoint