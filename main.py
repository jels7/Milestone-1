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
    print("5. About/Help - View information about the program and how to use it.")
    print("6. Undo last action - Undo the last action performed.")
    print("7. Exit - Exit the application.")

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
        print("5. About/Help")
        print("6. Undo last action")
        print("7. Exit")

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
                recipe = Recipe(title, ingredients.split(','), instructions)
                catalog.add_recipe(recipe)
                action_stack.append(('add', recipe))
                print("Recipe added successfully!")
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
                        print(f"- {recipe.title}")
                else:
                    print("No recipes found with that title.")
                    browse_choice = input("Would you like to browse all recipes instead? (y/n): ")
                    if browse_choice.lower() == 'y':
                        all_recipes = catalog.list_all_recipes()
                        if all_recipes:
                            print("All recipes:")
                            for recipe in all_recipes:
                                print(f"- {recipe.title}")
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
                    print(f"Title: {recipe.title}")
                    print(f"Ingredients: {', '.join(recipe.ingredients)}")
                    print(f"Instructions: {recipe.instructions}")
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
                    print(f"- {recipe.title}")
            else:
                print("No recipes available.")
        
        elif choice == '5':
            display_help()
        
        elif choice == '6':
            if action_stack:
                last_action = action_stack.pop()
                if last_action[0] == 'add':
                    catalog.remove_recipe(last_action[1].title)
                    print("Last action undone: Recipe removed.")
                # Add more undo actions here if needed
            else:
                print("No actions to undo.")
        
        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()