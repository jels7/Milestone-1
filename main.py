from recipes import Recipe, RecipeCatalog

def display_help():
    print("\nAbout/Help")
    print("This Recipe Catalog program allows you to manage your favorite recipes.")
    print("You can add new recipes, search for recipes by title, and view detailed information about each recipe.")
    print("\nMenu Options:")
    print("1. Add a new recipe - Add your favorite recipes to the catalog.")
    print("2. Search for a recipe by title - Find recipes quickly by their title.")
    print("3. View recipe details - Get detailed information about a specific recipe.")
    print("4. About/Help - View information about the program and how to use it.")
    print("5. Exit - Exit the application.")

def main():
    print("Welcome to the Recipe Catalog!")
    print("This program allows you to add, search, and view recipes.")
    print("You can manage your favorite recipes easily through this command-line interface.\n")

    catalog = RecipeCatalog()

    while True:
        print("\nRecipe Catalog")
        print("1. Add a new recipe")
        print("2. Search for a recipe by title")
        print("3. View recipe details")
        print("4. About/Help")
        print("5. Exit")

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
            display_help()
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()