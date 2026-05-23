import sqlite3

# Connect database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Show student table data
cursor.execute("SELECT * FROM student")
students = cursor.fetchall()

print("Student Table:")
for row in students:
    print(row)

# Show marks table data
cursor.execute("SELECT * FROM marks")
marks = cursor.fetchall()

print("Marks Table:")
for row in marks:
    print(row)

# Close connection
conn.close()