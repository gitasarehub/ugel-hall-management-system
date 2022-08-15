from flask import Flask, render_template, request, g, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login.utils import login_user
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy import or_, func
from flask_login import UserMixin, login_manager, login_user, LoginManager, login_required, logout_user, current_user
from datetime import datetime, date, timedelta
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from flask_mail import Mail, Message
import os
import click
from flask.cli import with_appcontext
# import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
# DATABASE_URL = os.environ['DATABASE']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE')
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hallmanagement.db'
db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

# class HallManage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(200), nullable=False)
#     lastname = db.Column(db.String(200), nullable=False)
#     student_name = db.Column(db.String(200), nullable=False)
#     student_id = db.Column(db.Integer, unique=True, nullable=False)
#     gender = db.Column(db.String(10), nullable=False)
#     room_number = db.Column(db.String(20), nullable=False)
#     phone_number = db.Column(db.String(20), nullable=False)
#     course_name = db.Column(db.String(100), nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.id

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fullname = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(200), nullable=False)
#     username = db.Column(db.String(200), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

#     def get_reset_token(self, expires_sec=1800):
#         s = Serializer(app.config['SECRET_KEY'], expires_sec)
#         return s.dumps({'user_id': self.id}).decode('utf-8')

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('home.html')

@app.route('/Templates/database.html', methods=['POST','GET'])
def database():
    return render_template('database.html')

@app.route('/Templates/login', methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/Templates/signup.html', methods=['POST','GET'])
def signup():
    # if request.method == 'POST':
    #     if request.form['password'] != request.form['confirmpassword']:
    #         flash("Passwords do not match check it", 'warning')
    #         return redirect("/SignUp")
    #     elif request.form['secretkey'] != "staff@ugelhall2022":
    #         flash("Passcode provided is invalid, visit your Chief Porter for a Passcode", 'info')
    #         return redirect("/SignUp")
    #     else:
    #         user_info = User(
    #             fullname=request.form['fullname'].title(),
    #             email=request.form['email'],
    #             username=request.form['username'],
    #             password=generate_password_hash(
    #                 request.form['password'], method='sha256')

    #         )
    #         try:
    #             db.session.add(user_info)
    #             db.session.commit()  # Add new data to db
    #             return redirect("/login")
    #         except:
    #             # replace with nicer experience
    #             flash("Username already exists choose another one", 'error')
    #             return redirect("/SignUp")
    # else:
        return render_template('signup.html')

@app.route('/Templates/base.html', methods=['POST','GET'])
def base():
    return render_template('base.html')

@app.route('/Templates/registration.html', methods=['POST','GET'])
def registration():
    return render_template('registration.html')

@app.route('/Templates/dashboard.html', methods=['POST','GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/Templates/porterslodge.html', methods=['POST','GET'])
def porterslodge():
    return render_template('porterslodge.html')

@app.route('/Templates/keylogging.html', methods=['POST','GET'])
def keylogging():
    return render_template('keylogging.html')

@app.route('/Templates/systemtickets.html', methods=['POST','GET'])
def systemtickets():
    return render_template('systemtickets.html')

if __name__ =="__main__":
    app.run(debug=True)