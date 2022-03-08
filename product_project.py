import sqlite3

product_details = sqlite3.connect("product.db")  # creating a database

# product_details.execute('''   Create Table ProductData(
#                       ProductCode Integer Primary Key Autoincrement,
#                       ProductName Text,
#                       ProductPrice Integer,
#                       ProductDistributorName Text,
#                       ManufacturerName Text
# );     ''')
# print("Table Created Successfully")

get_product_name = input ("Enter the product name: ")
get_product_price = input ("Enter the product price: ")
get_distributer_name = input ("Enter the distributor name: ")
get_manufacturer_name = input ("Enter the manufacturer name: ")

product_details.execute("Insert Into ProductData(ProductName, ProductPrice, ProductDistributorName, ManufacturerName) \
                        Values('"+get_product_name+"',"+get_product_price+",'"+get_distributer_name+"','"+get_manufacturer_name+"')")

product_details.commit()
product_details.close()

print("Inserted successfully")