import MySQLdb
import xlwt


#Instantiates a workbook and sheet to write the query results to
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet1") # name of the worksheet


#Database connection
db = MySQLdb.connect(host="localhost", # your host, usually localhost
user="root", # your username
passwd="test@123", # your password
db="northwind") # name of the data base


# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()


# Use all the SQL you like
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

rowNum = 0 #keep track of rows
colNum = 0 #keep track of columns


# print all the cells of the row to excel sheet
for row in cur.fetchall() :
sheet.write(rowNum, colNum, row) # row, column, value
rowNum = rowNum + 1
colNum = colNum + 1