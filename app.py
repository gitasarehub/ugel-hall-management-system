from turtle import title
from unittest import result
from flask import Flask, render_template, request, g, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login.utils import login_user
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_manager, login_user, LoginManager, login_required, logout_user, current_user
from datetime import datetime, date, timedelta
import os
import click
from flask.cli import with_appcontext
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from flask_mail import Mail, Message
from sqlalchemy import or_, func
# import psycopg2

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
    print("login is", User.query.get(int(user_id)))
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

    def __repr__(self):
        return '<User %r>' % self.id

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(100), nullable=False)
    othernames = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    portfolio = db.Column(db.String(30), nullable=False)
    hall = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(8), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return '<User %r>' % self.id


class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assignee = db.Column(db.String(200), nullable=False)
    action = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    person_modified = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

# Home Page
@app.route('/', methods=['POST','GET'])
def index():
    return render_template('home.html')

# Login Page
@app.route('/login', methods=['POST','GET'])
def login():
    return render_template('login.html')

# Signup Page
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        if request.form['passid'] != request.form['passid2']:
            flash("Passwords do not match check it", 'warning')
            return redirect("/signup")
        elif request.form['userpasscode'] != "staff@ugelhall2022":
            flash("Passcode provided is invalid, visit your Chief Porter for a Passcode", 'info')
            return redirect("/signup")
        else:
            user_info = User(
                surname = request.form['surname'].title(),
                othernames = request.form['othernames'].title(),
                portfolio = request.form['portfolio'].title(),
                gender = request.form['gender'].title(),
                username = request.form['username'],
                password = generate_password_hash(password=request.form['passid'], method='sha256'),
                contact = request.form['contact'],
                email = request.form['email'].title(),
                hall = request.form['hall'].title()
            )
            try:
                db.session.add(user_info)
                db.session.commit()  
                # Add new data to db
                return redirect("/login")
            except:
                # replace with nicer experience
                flash("Username already exists choose another one", 'error')
                return redirect("/signUp")
    else:
        return render_template('signup.html')

# Base Page
@app.route('/base', methods=['POST','GET'])
def base():
    return render_template('base.html')

# Dashboad Page
@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    return render_template('dashboard.html')

# Addstudents Page
@app.route('/addstudent', methods=['POST', 'GET'])
@login_required
def addStudent():
    if request.method == 'POST':
        surname = request.form['surname'].title()
        othernames = request.form['othernames'].title()
        student_id = request.form['student_id'].capitalize()
        gender = request.form['gender'].title()
        room_number = request.form['room_number']
        contact = request.form['contact']
        course = request.form['course'].title()
        email = request.form['email'].title()


        data = Student(
            surname=surname,
            othernames=othernames,
            student_name=surname + " " + othernames,
            student_id=student_id,
            gender=gender,
            room_number=room_number,
            contact=contact,
            course=course,
            email= email
        )
        activity = ActivityLog(
            assignee=session['user'],
            action="Added a new student",
            person_modified=surname + " " + othernames
        )

    try:
            db.session.add(data)
            db.session.add(activity)
            db.session.commit()
            flash("Student successfully added")
            return redirect("/addstudent")
    except:
            return render_template('ErrorID.html')

    else:
        order = Student.query.order_by(Student.student_id).all()
        return render_template('Add_Student.html', tasks=order,)

# Database Page
@app.route('/database', methods=['POST','GET'])
def database():
    Students =Student.query.all()
    return render_template('index.html',Students=Students)

# Porterslodge Page
@app.route('/porterslodge', methods=['POST','GET'])
def porterslodge():
    return render_template('porterslodge.html')

# Keylogging Page under Porterslodge Page
@app.route('/keylogging', methods=['POST','GET'])
def keylogging():
    return render_template('keylogging.html')

# ActivityLogs Page
@app.route('/systemtickets', methods=['POST','GET'])
def systemtickets():
    return render_template('systemtickets.html')

# About_us Page
@app.route('/about_us', methods=['POST','GET'])
def about_us():
    return render_template('about_us.html')

# Contact_us Page
@app.route('/contact_us', methods=['POST','GET'])
def contact_us():
    return render_template('contact_us.html')

if __name__ =="__main__":
    app.run(debug=True)