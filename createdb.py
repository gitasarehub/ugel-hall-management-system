import sqlite3

connection = sqlite3.connect("hallmanagement.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE student (student_id integer PRIMARY KEY, 
                 surname text NOT NULL, othernames text NOT NULL, gender text NOT NULL,
                 dob datetime, level integer NOT NULL, room_number integer NOT NULL, course text NOT NULL,
                contact text NOT NULL, emergency_contact text NOT NULL, email text NOT NULL)""")

cursor.execute("""CREATE TABLE room (room_number text PRIMARY KEY,
                block text NOT NULL, room_type text NOT NULL)""")

cursor.execute("""CREATE TABLE staff (staff_id integer PRIMARY KEY, 
                surname text NOT NULL, othernames text NOT NULL, gender text NOT NULL, dob datetime NOT NULL, 
                portfolio text NOT NULL, contact text NOT NULL, home_address text NOT NULL, 
                email text NOT NULL)""")
InputStudentData = [(10715846,"Asare", "Hubert",'M','1998-11-04', 400, 1001, "BSc Information Technology",
                    "0502885490", "0543789135","haofosu002@st.ug.edu.gh"),
                    (10726840,"Foriwa","Ama",'F','1998-11-04',200, 1005, "BSc Mathematics",
                    "0502885490", "0543789135","haofosu002@st.ug.edu.gh"),
                    (10732847,"Asante", "Samuel",'M','1998-11-04',100, 1009, "BA Political Science",
                    "0502885490", "0543789135","haofosu002@st.ug.edu.gh"),
                    (10915846,"Narh", "Ama",'F','1998-11-04',300, 1013,"BSc Computer Science",
                    "0502885490", "0543789135","haofosu002@st.ug.edu.gh"),
                    (10865891,"Asare", "Larbi",'M','1998-11-04',600, 1002,"BSc Pharmacy",
                    "0502885490", "0543789135","haofosu002@st.ug.edu.gh"),
                    (10949849,"Kimbu", "Akosua",'F','1998-11-04',200, 1006,"BSc Earth Science",
                    "0502885490", "0543789135","haofosu002@st.ug.edu.gh")]

InputRoomData = [(1001,'A',"4 in 1"),(1002,'B',"4 in 1"),(1003,'C',"4 in 1"),(1004,'D',"2 in 1"),
                 (1005,'A',"2 in 1"),(1006,'B',"4 in 1"),(1007,'C',"2 in 1"),(1008,'D',"4 in 1"),
                 (1009,'A',"4 in 1"),(1010,'B',"2 in 1"),(1011,'C',"4 in 1"),(1012,'D',"2 in 1"),
                 (1013,'A',"4 in 1"),(1014,'B',"4 in 1"),(1015,'C',"4 in 1"),(1016,'D',"4 in 1")]

InputStaffData = [(101,"Kumi", "Herbman",'M','1991-11-04', "Tutor",
                    "0502885490", "GA-0343-348-3","haofosu002@st.ug.edu.gh"),
                    (102,"Serwaa","Ansah",'F','1971-11-04', "Porter",
                    "0502885490", "GA-0343-348-4","haofosu002@st.ug.edu.gh"),
                    (103,"Sunku", "Tetteh",'M','1983-11-04',"Porter",
                    "0502885490", "GA-0343-348-5","haofosu002@st.ug.edu.gh"),
                    (104,"Aba", "Florence",'F','1988-11-04', "Electrican",
                    "0502885490", "GA-0343-348-6","haofosu002@st.ug.edu.gh"),
                    (105,"Asa", "Bonsu",'M','1998-11-04', "Carpenter",
                    "0502885490", "GA-0343-348-7","haofosu002@st.ug.edu.gh"),
                    (106,"Banba", "Nortey",'M','1997-11-04', "Plumber",
                    "0502885490", "GA-0343-348-8","haofosu002@st.ug.edu.gh")]

cursor.executemany("insert into student values (?,?,?,?,?,?,?,?,?,?,?)", InputStudentData)

cursor.executemany("insert into room values (?,?,?)", InputRoomData)

cursor.executemany("insert into staff values (?,?,?,?,?,?,?,?,?)", InputStaffData)

connection.commit()

connection.close()