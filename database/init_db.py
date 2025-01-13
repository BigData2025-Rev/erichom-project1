import connection

cnx, cursor = connection.getConnection()

#use bcrypt later

dropAllTables = "DROP TABLE if EXISTS products, users, orders;"
createTable = "CREATE TABLE if NOT EXISTS products(id int AUTO_INCREMENT PRIMARY KEY, name varchar(30), price int);"
createTable2 = "CREATE TABLE if NOT EXISTS users(id int AUTO_INCREMENT PRIMARY KEY, username varchar(255), password varchar(255), isAdmin int);"
createTable3 = "CREATE TABLE if NOT EXISTS orders(id int AUTO_INCREMENT PRIMARY KEY, productName varchar(255), custName varchar(255));"

testQ = "INSERT INTO products(name, price) VALUES('2025 Yamaha R1', 18999);"
printQ = "SELECT * FROM products;"

testUser = "INSERT INTO users(username, password, isAdmin) VALUES('admin', '123', 1)"
printUser = "SELECT * FROM users"


cursor.execute(dropAllTables)
cursor.execute(createTable)
cursor.execute(createTable2)
cursor.execute(createTable3)
cursor.execute(testQ)
cursor.execute(printQ)

for row in cursor:
    print(row)

cursor.execute(testUser)
cursor.execute(printUser)

for row in cursor:
    print(row)

cnx.commit()
cursor.close()
cnx.close()

