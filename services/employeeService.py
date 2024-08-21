from database import db 
from models.order import Order
from models.employee import Employee
from models.order import Order
from models.product import Product
from sqlalchemy import select
from datetime import date

def save(employee_data):
    
    emloyee_output_= Employee(date=date.today(), employee_id = employee_data["employee_id"])

    for item_id in employee_data['products_ids']:
        query = select(Product).filter(Product.id == item_id)
        item = db.session.execute(query).scalar()
        print(item)
        employee_output.products.append(item)

    db.session.add(employee_data)
    db.session.commit()

    db.session.refresh(employee_data)
    return employee_data

