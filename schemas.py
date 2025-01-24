from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    address = fields.Str(required=True)
    email = fields.Email(required=True)

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    product_name = fields.Str(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    order_date = fields.DateTime(required=True)
    user_id = fields.Int(required=True)