import database.dao as db

class productService:

    def __init__(self):
        self.dao = db
    
    def viewAllProducts(self):
        db.viewAllProducts()
    
    def addProduct(self, productName, price):
        db.addProduct(productName, price)
    
    def updateProduct(self, id, price):
        db.updateProduct(id, price)

    def deleteProduct(self, id):
        db.deleteProduct(id)
    
    def buyProduct(self, id, currentUser):
        db.buyProduct(id, currentUser)