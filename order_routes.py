from flask import Blueprint, request, jsonify
from app.models import db, User, Order, Product
from app.schemas import OrderSchema, ProductSchema

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    order_date = data.get('order_date')
    
    new_order = Order(user_id=user_id, order_date=order_date)
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify(OrderSchema().dump(new_order)), 201

@order_bp.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['GET'])
def add_product_to_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    
    if product in order.products:
        return jsonify({"message": "Product already in order"}), 400
    
    order.products.append(product)
    db.session.commit()
    
    return jsonify(OrderSchema().dump(order)), 200

@order_bp.route('/orders/<int:order_id>/remove_product', methods=['DELETE'])
def remove_product_from_order(order_id):
    data = request.get_json()
    product_id = data.get('product_id')
    
    order = Order.query.get_or_404(order_id)
    product = Product.query.get(product_id)
    
    if product in order.products:
        order.products.remove(product)
        db.session.commit()
        return jsonify({"message": "Product removed from order"}), 200
    
    return jsonify({"message": "Product not found in order"}), 404

@order_bp.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify(OrderSchema(many=True).dump(orders)), 200

@order_bp.route('/orders/<int:order_id>/products', methods=['GET'])
def get_products_in_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(ProductSchema(many=True).dump(order.products)), 200