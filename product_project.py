import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("product.db")

list_of_tables = connection.execute("Select name from sqlite_master Where type='table' And name='ProductData'").fetchall()

if list_of_tables != []:
    print("Table not Found!!! ")

else:

    connection.execute('''   Create Table ProductData(
                          ProductCode Integer Primary Key Autoincrement,
                          ProductName Text,
                          ProductPrice Integer,
                          ProductDistributorName Text,
                          ManufacturerName Text
    );     ''')
    print("Table Created Successfully")

while True:
    print("Select an option from the Menu: ? ")

    print("1. Add a Product: ? ")
    print("2. View all Product: ? ")
    print("3. Search a Product by using Product Name: ? ")
    print("4. Update a Product by using Product Name: ? ")
    print("5. Delete a Product by using Product Name: ? ")
    print("6. Highest Price of a Product: ? ")
    print("7. Lowest Price of a Product: ? ")
    print("8. Average Price of all Products: ? ")
    print("9. Sum of all prices in a Product: ? ")
    print("10. Count of a Product: ? ")
    print("11. Exit")

    choice = int(input("Enter a choice from the Menu: ? "))

    if choice == 1:

        get_product_name = input("Enter the Product Name: ")
        get_product_price = input("Enter the Product Price: ")
        get_distributor_name = input("Enter the Distributor Name: ")
        get_manufacturer_name = input("Enter the Manufacturer Name: ")

        connection.execute("Insert Into ProductData(ProductName, ProductPrice, ProductDistributorName, ManufacturerName) Values \
        ('" + get_product_name + "'," + get_product_price + ",'" + get_distributor_name + "','" + get_manufacturer_name + "')")

        connection.commit()

        print("Inserted successfully")

    elif choice == 2:

        result = connection.execute("Select * from ProductData")

        table = PrettyTable(["Code", "Product Name", "Product Price", "Product Distributor", "Product Manufacturer"])

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4]])

        print(table)

    elif choice == 3:

        get_name = input("Enter a Product Name to be Searched: ? ")

        result = connection.execute("Select * from ProductData Where ProductName= '"+get_name+"'")

        table = PrettyTable(["Code", "Product Name", "Product Price", "Product Distributor", "Product Manufacturer"])

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4]])

        print(table)

    elif choice == 4:

