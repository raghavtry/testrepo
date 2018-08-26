import sys
import MySQLdb

import pandas as pd


#Database connection
db = MySQLdb.connect(host="localhost", # your host, usually localhost
user="root", # your username
passwd="Mind@123", # your password
db="northwind") # name of the data base

sql = "SELECT * FROM orders"

df = pd.read_sql(sql, db)

#print df.head()

#Export to CSV
df.to_excel('orders.xlsx', index=False)
print('Done')