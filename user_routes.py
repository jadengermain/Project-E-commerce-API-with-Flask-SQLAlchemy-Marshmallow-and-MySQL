from flask import Blueprint, request, jsonify
from app.models import User, db
from app.schemas import UserSchema

user_routes = Blueprint('user_routes', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

@user_routes.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

@user_routes.route('/users', methods=['POST'])
def create_user():
    new_user = user_schema.load(request.json)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201

@user_routes.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    updated_user = user_schema.load(request.json, instance=user)
    db.session.commit()
    return user_schema.jsonify(updated_user)

@user_routes.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 204