import sqlite3

connection = sqlite3.connect("product.db")

get_product = input("Enter a ProductCode to be Updated? ")

get_product_name = input ("Enter the new product name: ")
get_product_price = input ("Enter the new product price: ")
get_distributor_name = input ("Enter the new distributor name: ")
get_manufacturer_name = input ("Enter the new manufacturer name: ")

connection.execute("Update ProductData \
Set ProductName= '"+get_product_name+"', ProductPrice= "+get_product_price+", ProductDistributorName= '"+get_distributor_name+"',\
ManufacturerName= '"+get_manufacturer_name+"'" )

result = connection.execute("Select * From ProductData")

for i in result:
    print("Product Code", i[0])
    print("Product Name", i[1])
    print("Product Price", i[2])
    print("Product Distributor Name", i[3])
    print("Manufacturer Name", i[4])