import logging
import database.connection as connection
from tabulate import tabulate 

logger = logging.getLogger(__name__)


def registerUser(username, password):
    cnx, cursor = connection.getConnection()
    logger.info(f'NEW USER REGISTERED: {username}')
    query = "INSERT INTO users(username, password, isAdmin) VALUES(%s, %s, 0)"
    params = (username, password)
    cursor.execute(query, params)
    cnx.commit()

def viewAllUsers():
    cnx, cursor = connection.getConnection()
    logger.info(f'ALL USERS VIEWED')
    query = "SELECT id, username, isAdmin FROM users"
    cursor.execute(query)
    print('\nUser List:\n')
    print(tabulate(cursor.fetchall(), headers=["ID", "Username","isAdmin"]))

def login(username, password):
    loggedIn = 0
    isAdmin = 0
    currentUser = ''
    cnx, cursor = connection.getConnection()
    logger.info(f'LOGIN ATTEMPTED FOR: {username}')
    query = ("SELECT * FROM users WHERE username = %s AND password = %s;")
    data = (username, password)
    cursor.execute(query, data)
    data=cursor.fetchall()


    if cursor.rowcount == 1:
        print('')
        loggedIn = 1
        isAdmin = data[0][3]
        currentUser = data[0][1]
        level = ''
        if (isAdmin == 1):
            level = 'Admin'
        else:
            level = 'User'
        print(f'Logged in as {data[0][1]} ({level}).')
        # print(f'isAdmin: {isAdmin}')


    return loggedIn, isAdmin, currentUser


def viewAllProducts():
    cnx, cursor = connection.getConnection()
    logger.info(f'PRODUCTS TABLE VIEWED')
    query = "SELECT * FROM products"
    cursor.execute(query)
    print('\nProduct List:\n')
    print(tabulate(cursor.fetchall(), headers=["ID", "Name","Price"]))

def addProduct(productName, price):
    cnx, cursor = connection.getConnection()
    logger.info(f'NEW PRODUCT ADDED: {productName}')
    query = "INSERT INTO products(name, price) VALUES(%s, %s)"
    data = (productName, price)
    cursor.execute(query, data)
    cnx.commit()

def updateProduct(id, price):
    cnx, cursor = connection.getConnection()
    logger.info(f'PRODUCT UPDATED. id: {id}')
    query = "UPDATE products SET price = %s WHERE id =%s"
    data = (price, id)
    cursor.execute(query, data)
    cnx.commit()

def deleteProduct(id):
    cnx, cursor = connection.getConnection()
    logger.info(f'PRODUCT DELETED. id: {id}')
    query = "DELETE FROM products WHERE id =%s"
    cursor.execute(query, [id])

def buyProduct(id, currentUser):
    cnx, cursor = connection.getConnection()
    logger.info(f'{currentUser} PURCHASED PRODUCT. id: {id}')
    query = "SELECT name FROM products WHERE id =%s"
    cursor.execute(query, [id])
    data=cursor.fetchall()
    name = data[0][0]
    print(f'Are you sure you want to order: {name}?')
    confirm = input("Confirm: y/n: ")
    if confirm == 'y':
        print('Order placed!')
        query = "INSERT INTO orders(productName, custName) VALUES(%s, %s)"
        data = (name, currentUser)
        cursor.execute(query, data)
        cnx.commit()
    else:
        print('Order canceled.')

def viewAllOrders():
    cnx, cursor = connection.getConnection()
    logger.info(f'ALL ORDERS VIEWED')
    query = "SELECT * FROM orders"
    cursor.execute(query)
    print('\nOrder List:\n')
    print(tabulate(cursor.fetchall(), headers=["ID", "Product Name","Customer Name"]))

def viewUserOrders(name):
    cnx, cursor = connection.getConnection()
    logger.info(f'{name} VIEWED ORDERS')
    query = "SELECT id, productName FROM orders WHERE custName=%s"
    cursor.execute(query, [name])
    print('\nYour Orders:\n')
    print(tabulate(cursor.fetchall(), headers=["ID", "Product Name"]))

def grantAdmin(id):
    cnx, cursor = connection.getConnection()
    logger.info(f'{id} GRANTED ADMIN ACCESS')
    query = "UPDATE users SET isAdmin=1 WHERE id=%s"
    cursor.execute(query,[id])
    print('Admin access granted.')
    cnx.commit()

def deleteUser(id):
    cnx, cursor = connection.getConnection()
    logger.info(f'{id} USER DELETED')
    query = "DELETE FROM users WHERE id=%s"
    cursor.execute(query,[id])
    print('User deleted.')
    cnx.commit()
    




