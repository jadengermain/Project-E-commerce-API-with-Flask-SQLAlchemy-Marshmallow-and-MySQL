from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from .models import User, Order, Product  # Import models
        db.create_all()  # Create database tables

        from .routes import user_routes, product_routes, order_routes  # Import routes
        app.register_blueprint(user_routes.bp)
        app.register_blueprint(product_routes.bp)
        app.register_blueprint(order_routes.bp)

    return app