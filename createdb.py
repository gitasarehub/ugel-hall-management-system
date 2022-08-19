import sqlite3
from traceback import print_list

GET_ALL_STUDENT = """SELECT * FROM Student;"""

CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, surname TEXT, othernames TEXT,
                    portfolio TEXT NOT NULL, email TEXT, username TEXT, password TEXT);"""

CREATE_STUDENT_TABLE = """CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY, student_id integer, 
                    surname text NOT NULL, othernames text NOT NULL, gender text NOT NULL,
                    dob datetime, level integer NOT NULL, room_number integer NOT NULL, course text NOT NULL,
                    contact text NOT NULL, email text NOT NULL);"""

CREATE_ACTIVITY_LOG = """CREATE TABLE IF NOT EXISTS ActivityLog (id INTEGER PRIMARY KEY, assignee TEXT NOT NULL,
                        action TEXT NOT NULL, date_created DateTime NOT NULL, person_modified TEXT NOT NULL);"""

# Student_Asare = [(student_id=10715846, surname='Asare', othernames='Hubert','Male', 400, 1001, "BSc Information Technology",
#                      '0502885490',email='haofosu002@st.ug.edu.gh'),
#                      (10726840,"Foriwa","Ama",'F','1998-11-04',200, 1002, "BSc Mathematics",
#                       "0543789135","haofosu002@st.ug.edu.gh"),
#                      (10732847,"Asante", "Samuel",'M','1998-11-04',100, 1003, "BA Political Science",
#                         "0543789135","asantesamuel002@st.ug.edu.gh"),
#                      (10917195,"Narh", "Ama",'F','1998-11-04',300, 1044,"BSc Computer Science",
#                      "0543789135","haofosu002@st.ug.edu.gh"),
#                      (10865891,"Asare", "Larbi",'F','1998-11-04',600, 2102,"BSc Pharmacy",
#                      "0505885490","larbi02@yahoo.com"),
#                      (10949849,"Kimbu", "Akosua",'F','1998-11-04',200, 3006,"BSc Earth Science",
#                      "0502885490","kimbu@gmail.com")]

connect = sqlite3.connect("hallmanagement.db") 
# connect.execute(CREATE_STUDENT_TABLE)
# connect.execute(CREATE_ACTIVITY_LOG)
# connect.execute(CREATE_USER_TABLE)
# connect.executemany("""INSERT INTO Student (student_id, surname, othernames, gender, dob, level, room_number, course, contact, email)
#                     VALUES(?,?,?,?,?,?,?,?,?,?);""", InputStudentData)
# connect.commit()
# connect.close()