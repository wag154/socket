from applications import db,app
from applications.model import Test_class

def create_Database():
    with app.app_context():
        db.create_all()

def delete_Database():
    with app.app_context():
        db.drop_all()

def add_stock_entries ():
    stock_entry_1 = Test_class(name = "jack",message = "Hello1")
    stock_entry_2 = Test_class(name = "Nathan",message = "Hello2")
    stock_entry_3 = Test_class(name = "Kacper",message = "Hello3")
    with app.app_context():
        db.session.add(stock_entry_1)
        db.session.add(stock_entry_2)
        db.session.add(stock_entry_3)
        db.session.commit()
def see_db_entries():
    with app.app_context():
        stock_entries = Test_class.query.all()
        for entry in stock_entries:
            print(f"{entry.name}, {entry.message}")
        
if __name__ == "__main__":
    delete_Database()
    create_Database()
    add_stock_entries()
    see_db_entries()