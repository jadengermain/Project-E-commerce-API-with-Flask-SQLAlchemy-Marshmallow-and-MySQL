# E-commerce API

This project is a fully functional e-commerce API built using Flask, Flask-SQLAlchemy, Flask-Marshmallow, and MySQL. It manages Users, Orders, and Products with proper relationships, including One-to-Many and Many-to-Many associations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Technologies Used](#technologies-used)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ecommerce_api
   ```

2. Set up a virtual environment:
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - Mac/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up the MySQL database:
   - Create a new database named `ecommerce_api` in MySQL Workbench.

6. Update the database URI in `config.py` with your MySQL credentials.

## Usage

To run the application, execute the following command:
```
python app.py
```

The API will be available at `http://localhost:5000`.

## API Endpoints

### User Endpoints
- `GET /users`: Retrieve all users
- `GET /users/<id>`: Retrieve a user by ID
- `POST /users`: Create a new user
- `PUT /users/<id>`: Update a user by ID
- `DELETE /users/<id>`: Delete a user by ID

### Product Endpoints
- `GET /products`: Retrieve all products
- `GET /products/<id>`: Retrieve a product by ID
- `POST /products`: Create a new product
- `PUT /products/<id>`: Update a product by ID
- `DELETE /products/<id>`: Delete a product by ID

### Order Endpoints
- `POST /orders`: Create a new order
- `GET /orders/<order_id>/add_product/<product_id>`: Add a product to an order
- `DELETE /orders/<order_id>/remove_product`: Remove a product from an order
- `GET /orders/user/<user_id>`: Get all orders for a user
- `GET /orders/<order_id>/products`: Get all products for an order

## Database Models

The project includes the following database models:
- User
- Order
- Product
- Order_Product (association table)

## Technologies Used

- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- MySQL
- Marshmallow-SQLAlchemy

For more details, refer to the individual files in the `app` directory.