import requests
from recipes import Recipe, RecipeCatalog

def display_help():
    print("\nAbout/Help")
    print("This Recipe Catalog program allows you to manage your favorite recipes.")
    print("You can add new recipes, search for recipes by title, and view detailed information about each recipe.")
    print("\nMenu Options:")
    print("1. Add a new recipe - Add your favorite recipes to the catalog.")
    print("2. Search for a recipe by title - Find recipes quickly by their title.")
    print("3. View recipe details - Get detailed information about a specific recipe.")
    print("4. Browse all recipes - List all recipes in the catalog.")
    print("5. Edit a recipe - Edit an existing recipe.")
    print("6. Delete a recipe - Delete an existing recipe.")
    print("7. Search recipes by ingredient - Find recipes that use a specific ingredient.")
    print("8. About/Help - View information about the program and how to use it.")
    print("9. Exit - Exit the application.")

def search_by_ingredient():
    ingredient = input("Enter the ingredient to search for: ")
    response = requests.get(f'http://localhost:5001/search_by_ingredient?ingredient={ingredient}')

    if response.status_code == 200:
        recipes = response.json().get("recipes")
        if recipes:
            print("Recipes found:")
            for recipe in recipes:
                print(f"- {recipe['name']}: {', '.join(recipe['ingredients'])}")
        else:
            print("No recipes found with that ingredient.")
    else:
        print("Error:", response.json().get("error"))



def edit_recipe(catalog):
    recipe_id = int(input("Enter the recipe ID to edit: "))
    recipe = catalog.get_recipe_by_id(recipe_id)
    if not recipe:
        print("Recipe not found.")
        return

    new_name = input(f"Enter the new recipe name (current: {recipe.title}): ")
    new_ingredients = input(f"Enter the new ingredients (comma-separated, current: {', '.join(recipe.ingredients)}): ").split(',')
    new_category = input(f"Enter the new category (current: {recipe.category}): ")

    response = requests.post('http://localhost:5000/edit_recipe', json={
        "id": recipe_id,
        "name": new_name,
        "ingredients": new_ingredients,
        "category": new_category
    })

    if response.status_code == 200:
        print("Recipe updated successfully!")
        updated_recipe = response.json().get("recipe")
        recipe.title = updated_recipe["name"]
        recipe.ingredients = updated_recipe["ingredients"]
        recipe.category = updated_recipe["category"]
    else:
        print("Error:", response.json().get("error"))

def delete_recipe(catalog):
    recipe_id = int(input("Enter the recipe ID to delete: "))
    recipe = catalog.get_recipe_by_id(recipe_id)
    if not recipe:
        print("Recipe not found.")
        return

    response = requests.post('http://localhost:5000/delete_recipe', json={"id": recipe_id})

    if response.status_code == 200:
        catalog.remove_recipe(recipe_id)
        print("Recipe deleted successfully!")
    else:
        print("Error:", response.json().get("error"))

def main():
    print("Welcome to the Recipe Catalog!")
    print("This program allows you to add, search, and view recipes.")
    print("You can manage your favorite recipes easily through this command-line interface.\n")

    catalog = RecipeCatalog()
    action_stack = []

    while True:
        print("\nRecipe Catalog")
        print("1. Add a new recipe")
        print("2. Search for a recipe by title")
        print("3. View recipe details")
        print("4. Browse all recipes")
        print("5. Edit a recipe")
        print("6. Delete a recipe")
        print("7. Search recipes by ingredient")
        print("8. About/Help")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            while True:
                title = input("Enter the recipe title: ")
                if not title:
                    print("Title cannot be empty. Please try again.")
                    continue
                ingredients = input("Enter the ingredients (comma-separated): ")
                if not ingredients:
                    print("Ingredients cannot be empty. Please try again.")
                    continue
                instructions = input("Enter the instructions: ")
                if not instructions:
                    print("Instructions cannot be empty. Please try again.")
                    continue
                category = input("Enter the category: ")
                recipe = Recipe(None, title, ingredients.split(','), instructions, category)
                catalog.add_recipe(recipe)
                action_stack.append(('add', recipe))
                print(f"Recipe added successfully with ID {recipe.recipe_id}!")
                break
        
        elif choice == '2':
            while True:
                title = input("Enter the recipe title to search: ")
                if not title:
                    print("Title cannot be empty. Please try again.")
                    continue
                results = catalog.search_recipe(title)
                if results:
                    print("Recipes found:")
                    for recipe in results:
                        print(f"- {recipe.recipe_id}: {recipe.title}")
                else:
                    print("No recipes found with that title.")
                    browse_choice = input("Would you like to browse all recipes instead? (y/n): ")
                    if browse_choice.lower() == 'y':
                        all_recipes = catalog.list_all_recipes()
                        if all_recipes:
                            print("All recipes:")
                            for recipe in all_recipes:
                                print(f"- {recipe.recipe_id}: {recipe.title}")
                        else:
                            print("No recipes available.")
                break
        
        elif choice == '3':
            while True:
                title = input("Enter the recipe title to view details: ")
                if not title:
                    print("Title cannot be empty. Please try again.")
                    continue
                recipe = catalog.get_recipe_details(title)
                if recipe:
                    print(f"ID: {recipe.recipe_id}")
                    print(f"Title: {recipe.title}")
                    print(f"Ingredients: {', '.join(recipe.ingredients)}")
                    print(f"Instructions: {recipe.instructions}")
                    print(f"Category: {recipe.category}")
                else:
                    print("Recipe not found.")
                back_choice = input("Press 'b' to go back to the main menu: ")
                if back_choice.lower() == 'b':
                    break
        
        elif choice == '4':
            all_recipes = catalog.list_all_recipes()
            if all_recipes:
                print("All recipes:")
                for recipe in all_recipes:
                    print(f"- {recipe.recipe_id}: {recipe.title}")
            else:
                print("No recipes available.")
        
        elif choice == '5':
            edit_recipe(catalog)
        
        elif choice == '6':
            delete_recipe(catalog)
        
        elif choice == '7':
            search_by_ingredient()
        
        elif choice == '8':
            display_help()
        
        elif choice == '9':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()