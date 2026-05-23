import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS student (
#     student_id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER,
#     class TEXT
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS marks (
#     mark_id INTEGER PRIMARY KEY,
#     student_id INTEGER,
#     subject TEXT,
#     marks INTEGER
# )
# """)

# Insert data into student table
cursor.execute("INSERT INTO student VALUES (4, 'Antara', 16, '10th')")
cursor.execute("INSERT INTO student VALUES (5, 'Ravi', 15, '9th')")
cursor.execute("INSERT INTO student VALUES (6, 'Sneha', 17, '11th')")

# Insert data into marks table
cursor.execute("INSERT INTO marks VALUES (5, 4, 'Math', 85)")
cursor.execute("INSERT INTO marks VALUES (6, 4, 'Science', 90)")
cursor.execute("INSERT INTO marks VALUES (7, 5, 'Math', 78)")
cursor.execute("INSERT INTO marks VALUES (8, 6, 'English', 88)")

print("Data added successfully")

conn.commit()
conn.close()
