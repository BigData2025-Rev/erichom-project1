# Entry point for app
import database.connection as connection
import services.orderService as orders
import services.productService as products
import services.userService as users
from tabulate import tabulate 

def main():
    cnx, cursor = connection.getConnection()

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

        if option not in ["1","2","3"]:
            print("Invalid action code. Please enter a valid option.")
            continue
        elif option == '1':

            print('')
            username = input("Enter username: ")
            password = input("Enter password: ")
            # make more robust later, bcrypt?
            query = ("SELECT * FROM users WHERE username = %s AND password = %s;")
            data = (username, password)
            cursor.execute(query, data)
            cursor.fetchall()
            for row in cursor:
                print(row)
         
            if cursor.rowcount == 1:
                print('')
                print("Logged in!")

                while True:
                    print("\nAdmin Panel")
                    print("[1] Add Product")
                    print("[2] View All Products")
                    print("[3] Update Product Price")
                    print("[4] Delete Product")
                    print("[5] Exit and Logout")

                    option = input("\nEnter action code: ")

                    if option not in ['1','2','3','4','5']:
                        print("Invalid action code. Please enter a valid option.")
                        continue
                    elif option == '1':
                        query = "INSERT INTO products(name, price) VALUES(%s, %s)"
                        productName = input("Product Name: ")
                        price = input("Price: ")
                        price = int(price)
                        data = (productName, price)
                        cursor.execute(query, data)
                        cnx.commit()

                    elif option == '2':
                        query = "SELECT * FROM products"
                        cursor.execute(query)
                        print('\nProduct List:')
                        print(tabulate(cursor.fetchall(), headers=["ID", "Name","Price"]))
                        # for row in cursor:
                        #     print(row)
                    
                    elif option == '3':
                        query = "UPDATE products SET price = %s WHERE id =%s"
                        id = input("Enter product id: ")
                        price = input("Enter new price: ")
                        id = int(id)
                        price = int(price)
                        data = (price, id)
                        cursor.execute(query, data)
                    
                    elif option == '4':
                        query = "DELETE FROM products WHERE id =%s"
                        id = input("Enter product ID to delete: ")
                        id = int(id)
                        cursor.execute(query, [id])

                    elif option == '5':
                        print('Logging out...')
                        break

                    continue

            else:
                print('')
                print("Invalid Username or Password!")
                continue
        elif option == '3':
            print("Thank you for shopping at The Motorcycle Emporium! Have a nice day!")
            break
if __name__ == '__main__':
    main()






