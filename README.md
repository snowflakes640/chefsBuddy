This is a personal project of mine to practice different side of development on my own.It would be like an assistand app for kitchen.
User should be able to:
- Have an inventory system, see it anytime to know what is in his kitchen currently
- Add, update or remove any item from the system to keep up with his daily purchases and usage
- Search Recipes online
- Save own recipes and use them later
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
- [ ] Connecting to external DBMS (MySQL80)
- [x] Getting recipe from API 
	- [x] Integrating the API
	- [x] Showing recipes w search words
- [ ] Getting Recipe from user
	- [] Taking the recipe as input
	- [ ] Store them in database
	- [ ] Showing recipes w search words