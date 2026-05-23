import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "",
    database="school"
)
print("Connected to the xampp")

cur = conn.cursor()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for i in rows:
    print(i)

conn.close()