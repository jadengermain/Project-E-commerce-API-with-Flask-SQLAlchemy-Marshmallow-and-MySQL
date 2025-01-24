from flask import Blueprint

# Initialize the routes blueprint
routes_bp = Blueprint('routes', __name__)

# Import user, product, and order routes
from .user_routes import *
from .product_routes import *
from .order_routes import *