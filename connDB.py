import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tienpk",
  database="learn_laravel"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users LIMIT 10")

for x in mycursor:
  print(x)