from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.routes import user_routes, product_routes, order_routes

app.register_blueprint(user_routes.bp)
app.register_blueprint(product_routes.bp)
app.register_blueprint(order_routes.bp)

if __name__ == '__main__':
    app.run(debug=True)