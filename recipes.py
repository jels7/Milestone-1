class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeCatalog:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_recipe(self, title):
        return [recipe for recipe in self.recipes if title.lower() in recipe.title.lower()]

    def get_recipe_details(self, title):
        for recipe in self.recipes:
            if recipe.title.lower() == title.lower():
                return recipe
        return None

    def remove_recipe(self, title):
        self.recipes = [recipe for recipe in self.recipes if recipe.title.lower() != title.lower()]

    def list_all_recipes(self):
        return self.recipes