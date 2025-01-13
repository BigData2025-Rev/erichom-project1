import database.dao as db

class orderService:

    def __init__(self):
        self.dao = db
    
    def viewAllOrders(self):
        db.viewAllOrders()

    def viewUserOrders(self, name):
        db.viewUserOrders(name) 
    