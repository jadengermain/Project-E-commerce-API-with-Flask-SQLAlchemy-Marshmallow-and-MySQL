from flask import Blueprint, request, jsonify
from app.models import Product, db
from app.schemas import ProductSchema

product_routes = Blueprint('product_routes', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_routes.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

@product_routes.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)

@product_routes.route('/products', methods=['POST'])
def create_product():
    new_product = product_schema.load(request.json)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

@product_routes.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    updated_product = product_schema.load(request.json, instance=product)
    db.session.commit()
    return product_schema.jsonify(updated_product)

@product_routes.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204