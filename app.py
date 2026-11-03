from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]


@app.route('/')
def homepage():
    """Homepage route that returns a welcome message."""
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200


@app.route('/products', methods=["GET"])
def get_products():
    """Returns all products, or filters by category if a query string is provided."""
    category = request.args.get('category')
    if category:
        filtered = [p for p in products if p["category"] == category]
        return jsonify(filtered), 200
    return jsonify(products), 200


@app.route('/products/<int:id>', methods=["GET"])
def get_product(id):
    """Returns a specific product by ID, or 404 if not found."""
    product = next((p for p in products if p["id"] == id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200


if __name__ == "__main__":
    app.run(debug=True)