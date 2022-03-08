import sqlite3

connection = sqlite3.connect("product.db")

get_product = input("Enter a ProductCode to be Searched? ")

result = connection.execute("Select * From ProductData Where ProductCode=" +get_product)

for i in result:
    print("ProductCode", i[0])
    print("ProductName", i[1])
    print("ProductPrice", i[2])
    print("ProductDistributorName", i[3])
    print("ManufacturerName", i[4])