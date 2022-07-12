import sqlite3

connection = sqlite3.connect("hallmanagement.db")
cursor= connection.cursor()

# cursor.execute("""CREATE TABLE student (student_id INTEGER, 
#                 surname TEXT, othernames TEXT, dob TEXT, 
#                 level INTEGER, course TEXT, CONTACT text, 
#                 emergency_contact TEXT, email TEXT)""")

# cursor.execute("""CREATE TABLE room (room_number TEXT,
#                 block TEXT, room_type TEXT)""")

# cursor.execute("""CREATE TABLE staff (staff_id INTEGER, 
#                 surname TEXT, othernames TEXT, dob TEXT, 
#                 portfolio TEXT, contact TEXT, home_address TEXT, 
#                 email TEXT)""")

connection.commit()

connection.close()