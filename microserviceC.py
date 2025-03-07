from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample storage for recipes and reviews
recipes = {
    1: {"name": "Pasta", "ingredients": ["noodles", "tomato sauce"], "category": "Italian", "reviews": []},
    2: {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber"], "category": "Vegetarian", "reviews": []},
    3: {"name": "Chicken Curry", "ingredients": ["chicken", "curry powder", "coconut milk"], "category": "Indian", "reviews": []}
}

# Route to submit a rating and review for a recipe
@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.json
    recipe_id = data.get("id")
    rating = data.get("rating")
    review = data.get("review")

    if recipe_id not in recipes:
        return jsonify({"error": "Recipe not found"}), 404

    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    recipes[recipe_id]["reviews"].append({"rating": rating, "review": review})
    return jsonify({"message": "Review submitted successfully", "reviews": recipes[recipe_id]["reviews"]})

# Route to get the average rating and reviews for a recipe
@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    recipe_id = int(request.args.get('id'))

    if recipe_id not in recipes:
        return jsonify({"error": "Recipe not found"}), 404

    reviews = recipes[recipe_id]["reviews"]
    if not reviews:
        return jsonify({"average_rating": None, "reviews": []})

    average_rating = sum(review["rating"] for review in reviews) / len(reviews)
    return jsonify({"average_rating": average_rating, "reviews": reviews})

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5002, debug=True)