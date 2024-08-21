from . import ma
from marshmallow import fields




class EmployeeSchema(ma.Schema):
    employee_id = fields.Integer(required=False) #Primary Key is Autogenerated and doesn't need to be apart of the payload
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    role_id = fields.Integer(required=True)

    class Meta: 
        fields = ("id", "name", "email", "phone", "username", "password", "role_id")


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True, exclude=["password"])

class EmployeeProductSchema(ma.Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)