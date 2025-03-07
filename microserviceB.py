from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample recipe storage with categories
recipes = {
    1: {"name": "Pasta", "ingredients": ["noodles", "tomato sauce"], "category": "Italian"},
    2: {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber"], "category": "Vegetarian"},
    3: {"name": "Chicken Curry", "ingredients": ["chicken", "curry powder", "coconut milk"], "category": "Indian"}
}

# Route to search recipes by ingredients
@app.route('/search_by_ingredient', methods=['GET'])
def search_by_ingredient():
    ingredient = request.args.get('ingredient')
    if not ingredient:
        return jsonify({"error": "Ingredient is required"}), 400

    matching_recipes = [recipe for recipe in recipes.values() if ingredient in recipe["ingredients"]]
    return jsonify({"recipes": matching_recipes})

# Route to filter recipes by category
@app.route('/filter_by_category', methods=['GET'])
def filter_by_category():
    category = request.args.get('category')
    if not category:
        return jsonify({"error": "Category is required"}), 400

    category = category.lower()  # Normalize case
    matching_recipes = [recipe for recipe in recipes.values() if recipe["category"].lower() == category]

    return jsonify({"recipes": matching_recipes})

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5001, debug=True)