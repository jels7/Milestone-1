from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample storage for shopping lists
shopping_lists = {}

# Route to add ingredients to the shopping list
@app.route('/add_to_shopping_list', methods=['POST'])
def add_to_shopping_list():
    data = request.json
    user_id = data.get("user_id")
    ingredients = data.get("ingredients")

    if user_id not in shopping_lists:
        shopping_lists[user_id] = []

    shopping_lists[user_id].extend(ingredients)
    return jsonify({"message": "Ingredients added to shopping list", "shopping_list": shopping_lists[user_id]})

# Route to get the shopping list
@app.route('/get_shopping_list', methods=['GET'])
def get_shopping_list():
    user_id = request.args.get('user_id')

    if user_id not in shopping_lists:
        return jsonify({"shopping_list": []})

    return jsonify({"shopping_list": shopping_lists[user_id]})

# Route to remove ingredients from the shopping list
@app.route('/remove_from_shopping_list', methods=['POST'])
def remove_from_shopping_list():
    data = request.json
    user_id = data.get("user_id")
    ingredients = data.get("ingredients")

    if user_id not in shopping_lists:
        return jsonify({"error": "Shopping list not found"}), 404

    shopping_lists[user_id] = [ingredient for ingredient in shopping_lists[user_id] if ingredient not in ingredients]
    return jsonify({"message": "Ingredients removed from shopping list", "shopping_list": shopping_lists[user_id]})

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5003, debug=True)