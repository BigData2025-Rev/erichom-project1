# Entry point for app
import database.connection as connection
import services.orderService as orders
import services.productService as products
from services.userService import userService
from services.productService import productService
from services.orderService import orderService
from tabulate import tabulate 
import logging
import os

def main():

    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='erichom-project1/history.log', encoding='utf-8', level=logging.DEBUG)

    # cnx, cursor = connection.getConnection()
    userHandler = userService()
    productHandler = productService()
    orderHandler = orderService()
    loggedIn = 0
    isAdmin = 0
    currentUser = ''

    #Entry point
    while True:
        print('\n')
        print('----------------------------------')
        print("Welcome to The Motorcycle Emporium!")
        print("[1] Login")
        print("[2] Register")
        print("[3] Exit")
        print('----------------------------------')
        print('\n')
        option = input("Enter action: ")
        os.system('clear')

        if option not in ["1","2","3"]:
            print("Invalid action code. Please enter a valid option.")
            continue

        elif option == '1':

            print('')
            username = input("Enter username: ")
            password = input("Enter password: ")
            # make more robust later, bcrypt?
            # query = ("SELECT * FROM users WHERE username = %s AND password = %s;")
            # data = (username, password)
            # cursor.execute(query, data)
            # data = cursor.fetchall()
            
            loggedIn, isAdmin, currentUser = userHandler.login(username, password)
            # print(f'currentUser: {currentUser}')
            # print(data[0][3])
         
            if loggedIn == 1 and isAdmin == 1:
                # print('')
                # print("Logged in!")
                logger.info(f'ADMIN {currentUser} LOGGED IN SUCCESSFULLY')
                
                while True:
                    print('----------------------------------')
                    print('Menu:')
                    print("[1] View All Products")
                    print("[2] Purchase Products")
                    print("[3] View Orders")
                    print("[4] Exit and Logout")
                    print("[5] ACCESS ADMIN PANEL")

                    option = input("\nEnter action code: ")
                    os.system('clear')

                    if option not in ['1','2','3','4','5']:
                        print("Invalid action code. Please enter a valid option.")
                        continue

                    elif option == '1':
                        productHandler.viewAllProducts()

                    elif option == '2':
                        id = input('Enter the id of the motorcycle you want to order: ')
                        id = int(id)
                        productHandler.buyProduct(id, currentUser)
                    
                    elif option =='3':
                        orderHandler.viewUserOrders(currentUser)
                    
                    elif option == '4':
                        print('Logging out...')
                        break

                    elif option == '5':
                        while True:
                            print('----------------------------------')
                            print("\nAdmin Panel")
                            print("[1] Add Product")
                            print("[2] View All Products")
                            print("[3] Update Product Price")
                            print("[4] Delete Product")
                            print("[5] View All Users")
                            print("[6] View All Orders")
                            print("[7] Grant Admin Access")
                            print("[8] Delete Users")
                            print("[9] Exit")

                            option = input("\nEnter action code: ")
                            os.system('clear')

                            if option not in ['1','2','3','4','5','6','7','8','9']:
                                print("Invalid action code. Please enter a valid option.")
                                continue
                            
                            elif option == '1':
                                productName = input("Product Name: ")
                                price = input("Price: ")
                                price = int(price)
                                productHandler.addProduct(productName, price)

                            elif option == '2':
                                productHandler.viewAllProducts()
                    
                            elif option == '3':
                                id = input("Enter product id: ")
                                price = input("Enter new price: ")
                                id = int(id)
                                price = int(price)

                                productHandler.updateProduct(id, price)
                            
                            elif option == '4':
                                # query = "DELETE FROM products WHERE id =%s"
                                id = input("Enter product ID to delete: ")
                                id = int(id)
                                productHandler.deleteProduct(id)

                            elif option == '5':
                                userHandler.viewUsers()

                            elif option == '6':
                                orderHandler.viewAllOrders()

                            elif option == '7':
                                id = input('Enter id of user that you wish to grant admin access to: ')
                                id = int(id)
                                confirm = input('ARE YOU SURE THAT YOU WANT TO PROCEED? Type YES if so. ')
                                if confirm == 'YES':
                                    userHandler.grantAdmin(id)
                            
                            elif option == '8':
                                id = input('Enter id of user to delete: ')
                                id = int(id)
                                userHandler.deleteUser(id)
                             
                            elif option == '9':
                                print('Returning to previous menu...')
                                break

                            continue
                    continue


                

            elif loggedIn == 1 and isAdmin == 0:
                logger.info(f'USER {currentUser} LOGGED IN SUCCESSFULLY')
                while True:
                    print('----------------------------------')
                    print('Menu:')
                    print("[1] View All Products")
                    print("[2] Purchase Products")
                    print("[3] View Orders")
                    print("[4] Exit and Logout")

                    option = input("\nEnter action code: ")
                    os.system('clear')

                    if option not in ['1','2','3','4']:
                        print("Invalid action code. Please enter a valid option.")
                        continue

                    elif option == '1':
                        productHandler.viewAllProducts()

                    elif option == '2':
                        id = input('Enter the id of the motorcycle you want to order: ')
                        id = int(id)
                        productHandler.buyProduct(id, currentUser)
                    
                    elif option =='3':
                        orderHandler.viewUserOrders(currentUser)
                    
                    elif option == '4':
                        print('Logging out...')
                        break

                    continue

            else:
                print('')
                print("Invalid Username or Password!")
                
                continue

        elif option == '2':
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            userHandler.register(username, password)
            print('Use your new credentials to login.')

        elif option == '3':
            print("Thank you for shopping at The Motorcycle Emporium! Have a nice day!")
            break

if __name__ == '__main__':
    main()






