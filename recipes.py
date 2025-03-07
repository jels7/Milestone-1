class Recipe:
    def __init__(self, recipe_id, title, ingredients, instructions, category):
        self.recipe_id = recipe_id
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category

class RecipeCatalog:
    def __init__(self):
        self.recipes = []
        self.next_id = 1

    def add_recipe(self, recipe):
        recipe.recipe_id = self.next_id
        self.recipes.append(recipe)
        self.next_id += 1

    def search_recipe(self, title):
        return [recipe for recipe in self.recipes if title.lower() in recipe.title.lower()]

    def get_recipe_details(self, title):
        for recipe in self.recipes:
            if recipe.title.lower() == title.lower():
                return recipe
        return None

    def get_recipe_by_id(self, recipe_id):
        for recipe in self.recipes:
            if recipe.recipe_id == recipe_id:
                return recipe
        return None

    def remove_recipe(self, recipe_id):
        self.recipes = [recipe for recipe in self.recipes if recipe.recipe_id != recipe_id]

    def list_all_recipes(self):
        return self.recipes