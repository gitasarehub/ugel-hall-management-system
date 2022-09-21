from distutils.log import Log
from email.policy import default
from xmlrpc.client import DateTime
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, or_, func
from datetime import date, datetime
from flask_login.utils import login_user
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_manager, login_user, LoginManager, login_required, logout_user, current_user
from datetime import datetime
import os
import click
from flask.cli import with_appcontext
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///hallmanagement.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# DATABASE_URL = os.environ['hallmanagement.db']
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE')
# connect = psycopg2.connect(DATABASE_URL, sslmode='require')


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# @click.command(name='create_tables')
# @with_appcontext
# def create_tables():
#     db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, unique=True, nullable=False)
    surname = db.Column(db.String(200), nullable=False)
    othernames = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(8), nullable=False)
    room_number = db.Column(db.String(5), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(3), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    hall = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(20), nullable=False)
    othernames = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(18), nullable=False)
    portfolio = db.Column(db.String(30), nullable=False)
    hall = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

class Complaints(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(8), nullable=False)
    std_fullname = db.Column(db.String(120), nullable=False)
    room_number = db.Column(db.String(5), nullable=False)
    hall = db.Column(db.String(30), nullable=False)
    issue_type = db.Column(db.String(25), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(120), nullable=False)
    event_type = db.Column(db.String(25), nullable=False)
    event_desc = db.Column(db.String)
    event_date = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

class Activities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doer = db.Column(db.String(200), nullable=False)
    event = db.Column(db.String(200), nullable=False)
    date_of_event = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id

class Keylog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(5), nullable=False)
    loggers_name = db.Column(db.String(120), nullable=False)
    time_in = db.Column(db.DateTime, default=datetime.utcnow)
    collectors_name = db.Column(db.String(120))
    time_out = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.id

class Visitors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitors_name = db.Column(db.String(120), nullable=False)
    id_type = db.Column(db.String(25), nullable=False)
    id_number = db.Column(db.String(25), nullable=False)
    hostname = db.Column(db.String(120), nullable=False)
    hall = db.Column(db.String(30), nullable=False)
    room_number = db.Column(db.String(5), nullable=False)
    contact = db.Column(db.String(18), nullable=False)
    time_in = db.Column(db.DateTime, default=datetime.utcnow)
    time_out = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.id

# --------------Home Page----------------
@app.route('/', methods=['POST','GET'])
def index():
    return render_template('home.html')

# --------------Login Page---------------
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').title()
        password = request.form.get('password')
        session['user'] = username
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password,password):
            error_statement = "Please Enter Your Correct Login Credentials!"
            return errorhandler(error_statement)
        else:
            login_user(user)
            return redirect(url_for('dashboard'))
    else:
        return render_template("login.html")

# ----------------------Signup Page-------------------
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == "POST":     
        if request.form['passcode'] != "staff@ugelhall2022":
            error_statement = "Passcode provided is invalid, visit your Admin for a Passcode"
            return errorhandler(error_statement)
        else:
            user_info = User(
                username = request.form['username'].title(),
                surname = request.form['surname'].title(),
                othernames = request.form['othernames'].title(),
                portfolio = request.form['staff-type'],
                gender = request.form['gender'].title(),
                email = request.form['email'].lower(),
                password = generate_password_hash(request.form['password']),
                contact = request.form['contact'],
                hall = request.form['hall'].title()
            )
            try:
                db.session.add(user_info)
                db.session.commit()  
                # Add new data to db
                return redirect(url_for("login"))
            except:
                # replace with nicer experience
                error_statement = "This Username or email already exists choose another one"
                return errorhandler(error_statement)
    else:
        return render_template('signup.html')

# --------------------Errorhandling page--------------------
@app.route('/errorhandling', methods=['POST','GET'])
def errorhandler(error_message):
    return render_template('errorhandling.html',error_message=error_message)

# ------------------------Dashboad Page---------------------
@app.route('/dashboard', methods=['POST','GET'])
@login_required
def dashboard():
    Male = Student.query.filter(Student.gender == "Male").count()
    Female = Student.query.filter(Student.gender == "Female").count()
    Activity = Activities.query.order_by(desc(Activities.date_of_event)).limit(4).all()
    PostedEvents = Events.query.order_by(Events.event_date).limit(4).all()
    return render_template('dashboard.html',Activity=Activity,Male=Male,Female=Female,PostedEvents=PostedEvents)

# -------------------------------Search Page---------------------------
@app.route('/search', methods=['POST','GET'])
@login_required
def search():
    if request.method == 'POST':
        searchQuery = request.form.get("searchQuery")
        try:
            results = Student.query.filter(or_(Student.student_id == searchQuery,
                                                Student.surname.op('regexp')(r'\b{}\b'.format(searchQuery.title())),
                                                Student.othernames.op('regexp')(r'\b{}\b'.format(searchQuery.title())),
                                                Student.room_number.op('regexp')(r'\b{}\b'.format(searchQuery.title()))
                                                    )).all()
            return render_template('SearchStudent.html', results=results)
        except:
            return "There was a problem with the querying code"
    else:
            return render_template('searchpage.html')

# -------------------------------Events Page-----------------------------------
@app.route('/events', methods=['POST','GET'])
@login_required
def events():
    if request.method == 'POST':
        event_name = request.form['event_name'].title()
        type_of_event = request.form['event_type'].title()
        event_date = request.form['event_date']
        description = request.form['description'].title()

        eventpassed = Events(
            event_name=event_name,
            event_type =type_of_event,
            event_desc =description,
            event_date = event_date
        )
        activity = Activities(
        doer =session['user'],
        event ="Added a new event coming on " + eventpassed.event_date)
        try:
            # db.session.add(eventpassed)
            db.session.add(activity)
            db.session.commit()
            return redirect(url_for("events"))
        except:
            error_message = "Error occured adding Event!"
            return errorhandler(error_message)
    else:
        PostedEvents = Events.query.order_by(Events.event_date).all()
        return render_template('events.html',PostedEvents=PostedEvents)

# -----------------------------Addstudents Page-------------------------------
@app.route('/addstudent', methods=['POST', 'GET'])
@login_required
def addStudent():
    if request.method == "POST":
        surname = request.form['surname'].title()
        othernames = request.form['othernames'].title()
        student_id = request.form['student_id']
        gender = request.form['gender'].title()
        hall = request.form['hall']
        level = request.form['level']
        room_number = request.form['room_number'].capitalize()
        contact = request.form['contact']
        course = request.form['course'].title()
        email = request.form['email'].lower()


        data = Student(
            surname=surname,
            othernames=othernames,
            student_id=student_id,
            gender=gender,
            hall=hall,
            level=level,
            room_number=room_number,
            contact=contact,
            course=course,
            email= email
        )
        activity = Activities(
        doer =session['user'],
        event ="Added a new student with ID: " + str(data.student_id))

        try:
                db.session.add(data)
                db.session.add(activity)
                db.session.commit()
                return redirect(url_for("database"))
        except:
                error_message = "Add student was unsuccessful"
                return errorhandler(error_message)
    else:
        return render_template('addstudent.html')

# ----------------------------Database Page------------------------------
@app.route('/database', methods=['POST','GET'])
@login_required
def database():
    Students = Student.query.order_by(Student.surname).all()
    return render_template('database.html',Students=Students)

# --------------------------Porterslodge Page----------------------------
@app.route('/porterslodge', methods=['POST','GET'])
@login_required
def porterslodge():
    return render_template('porterslodge.html')

# ---------LogKey under Porterslodge---------
@app.route('/logkey', methods=['POST','GET'])
@login_required
def logkey():
    if request.method=="POST":
        room_number=request.form['room_number'].capitalize()
        loggers_name=request.form['loggers_name'].title()
        
        alog = Keylog(
            room_number=room_number,
            loggers_name=loggers_name
        )
        activity = Activities(
        doer =session['user'],
        event ="Logged key of Room: " + room_number)
        try:
            db.session.add(alog)
            db.session.add(activity)
            db.session.commit()
            return redirect(url_for("logkey"))
        except:
            error_message = "Problem Encountered While Logging Room Key!"
            return errorhandler(error_message)
    Logs = Keylog.query.order_by(Keylog.time_in).all()
    return render_template('logkey.html',Logs=Logs)

#-------Vistorsbook under Porterslodge----------
@app.route('/visitorsbook', methods=['POST','GET'])
@login_required
def visitorsbook():
    if request.method=="POST":
        visitors_name=request.form['visitors_name'].title()
        id_type=request.form['id_type'].title()
        id_number=request.form['id_number']
        hostname=request.form['hostname'].title()
        hall=request.form['hall']
        room_number=request.form['room_number'].capitalize()
        visitors_contact=request.form['visitors_contact']
        
        Visits = Visitors(
            visitors_name=visitors_name,
            id_type=id_type,
            id_number=id_number,
            hostname=hostname,
            hall=hall,
            room_number=room_number,
            contact=visitors_contact
        )
        activity = Activities(
        doer =session['user'],
        event ="Logged a visitor of Room: " + room_number)
        try:
            db.session.add(Visits)
            db.session.add(activity)
            db.session.commit()
        except:
            error_message = "Problem Encountered While Logging Visitor!"
            return errorhandler(error_message)
    Visits = Visitors.query.order_by(Visitors.time_in).all()
    return render_template('visitorsbook.html',Visits=Visits)

# -------------------------SystemLogs Page-----------------------
@app.route('/systemtickets', methods=['POST','GET'])
@login_required
def systemtickets():
    Activity = Activities.query.order_by(desc(Activities.date_of_event)).all()
    return render_template('systemtickets.html',Activity=Activity)


# ------------------Compliants Submission Page-------------------
@app.route('/complaintsSubmission', methods=['POST','GET'])
def complaintsSubmission():
    if request.method == "POST":
        room_number = request.form['room_number'].capitalize()
        fullname = request.form['std_fullname'].title()
        hall = request.form['hall']
        student_id = request.form['student_id']
        issue_type = request.form['issue_type']
        other_specify = request.form['other_specify']
        description = request.form['description'].capitalize()

        check_Id = Student.query.filter_by(student_id=student_id).first()
        if check_Id:    
            if issue_type == "Other":
                issue_type = other_specify
        
        data = Complaints(
            room_number=room_number,
            std_fullname=fullname,
            student_id=student_id,
            hall=hall,
            issue_type=issue_type,
            description=description
        )
        try:
                db.session.add(data)
                db.session.commit()
                error_statement = "Complaint Submitted Successfully!"
                return errorhandler(error_statement)
        except:
                error_statement = "Complaint Submitted was Unsuccessful!"
                return errorhandler(error_statement)
    else:
        return render_template('complaintsSubmission.html')

# --------------------View Complaints-----------------------
@app.route('/complaints', methods=['POST','GET'])
@login_required
def complaints():
    Issues = Complaints.query.order_by(desc(Complaints.date_submitted)).all()
    return render_template('complaints.html',Issues=Issues)

# ------------------Update Students--------------------------
@app.route('/update/<int:id>', methods=['POST','GET'])
@login_required
def update(id):
    updateStudent = Student.query.get_or_404(id)
    activity = Activities(
        doer =session['user'],
        event ="Updated details of student with ID: " + str(updateStudent.student_id))

    if request.method == 'POST':
# UpdateHere just can't update student ID
        updateStudent.surname = request.form['surname'].title()
        updateStudent.lastname = request.form['othernames'].title()
        updateStudent.gender = request.form['gender'].title()
        updateStudent.room_number = request.form['room_number'].capitalize()
        updateStudent.contact = request.form['contact']
        updateStudent.course = request.form['course'].title()
        updateStudent.level = request.form['level']
        updateStudent.hall = request.form['hall']
        updateStudent.email = request.form['email'].lower()

        try:
            db.session.add(activity)
            db.session.commit()
            return redirect(url_for("database"))
        except:
                error_statement = "Make Sure All Required Details Are Not Empty!"
                return errorhandler(error_statement)
    else:
        return render_template('updateStudent.html', updateStudent=updateStudent)

# ----------------------Delete Student---------------------------
@app.route('/delete/<int:id>')
@login_required
def delete(id):
    student_to_delete = Student.query.get_or_404(id)

    activity = Activities(
        doer = session['user'],
        event = "Deleted student with ID: " + str(student_to_delete.student_id))
    try:
        db.session.add(activity)
        db.session.delete(student_to_delete)
        db.session.commit()
        return redirect(url_for('database'))
    except:
        error_statement = "There Was a Problem Deleting This Student"
        return errorhandler(error_statement)

# ------------------Sign Out Keylog--------------------
@app.route('/signoutLogger/<int:id>', methods=['POST','GET'])
@login_required
def updateLoggers(id):
    updateLog = Keylog.query.get_or_404(id)
    activity = Activities(
        doer =session['user'],
        event ="Signed Out Key of Room: " + updateLog.room_number)

    if request.method == 'POST':
        updateLog.collectors_name = request.form['collectors_name'].title()
        updateLog.time_out = datetime.now()
        
        try:
            db.session.add(activity)
            db.session.commit()
            return redirect(url_for('logkey'))
        except:
                error_statement = "Make Sure All Required Details Are Not Empty!"
                return errorhandler(error_statement)
    else:
        Logs = Keylog.query.order_by(Keylog.time_in).all()
        return render_template('signOutKeylog.html', Logs=Logs,updateLog=updateLog)

# ------------------Sign Out Visitors--------------------
@app.route('/signoutVisitor/<int:id>', methods=['POST','GET'])
@login_required
def updateVisitors(id):
    SignOutVisits = Visitors.query.get_or_404(id)
    activity = Activities(
        doer =session['user'],
        event ="Signed Out Visitor of Room: " + SignOutVisits.room_number)

    if request.method == 'POST':
        SignOutVisits.time_out = datetime.now()

        try:
            db.session.add(activity)
            db.session.commit()
            return redirect(url_for('visitorsbook'))
        except:
                error_statement = "System Encountered Error Signing Visitor Out!"
                return errorhandler(error_statement)
    else:
        Visits = Visitors.query.order_by(Visitors.time_in).all()
        return render_template('signOutVisitor.html',Visits=Visits,SignOutVisits=SignOutVisits)

# ------------------------------Log Out-------------------------------
@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

# ------------------------About_us Page--------------------------
@app.route('/about_us', methods=['POST','GET'])
def about_us():
    return render_template('about_us.html')

# ----------------------Contact_us Page--------------------
@app.route('/contact_us', methods=['POST','GET'])
def contact_us():
    return render_template('contact_us.html')


if __name__ == "__main__":
    app.run(debug=True)