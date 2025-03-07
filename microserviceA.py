from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample recipe storage
recipes = {
    1: {"name": "Pasta", "ingredients": ["noodles", "tomato sauce"]},
    2: {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber"]}
}

# Route to edit an existing recipe
@app.route('/edit_recipe', methods=['POST'])
def edit_recipe():
    data = request.json
    recipe_id = data.get("id")
    new_name = data.get("name")
    new_ingredients = data.get("ingredients")

    # Check if the recipe exists and update it
    if recipe_id in recipes:
        recipes[recipe_id] = {"name": new_name, "ingredients": new_ingredients}
        return jsonify({"message": "Recipe updated", "recipe": recipes[recipe_id]})
    return jsonify({"error": "Recipe not found"}), 404

# Route to delete an existing recipe
@app.route('/delete_recipe', methods=['POST'])
def delete_recipe():
    data = request.json
    recipe_id = data.get("id")

    # Check if the recipe exists and delete it
    if recipe_id in recipes:
        del recipes[recipe_id]
        return jsonify({"message": "Recipe deleted"})
    return jsonify({"error": "Recipe not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)