from crypt import methods
# from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
# from flask_login.utils import login_user
# from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy import or_, func
# from flask_login import UserMixin, login_manager, login_user, LoginManager, login_required, logout_user
from datetime import datetime, date, timedelta
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from flask_mail import Mail, Message
import os
import click
from flask.cli import with_appcontext
# import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
# DATABASE_URL = os.environ['DATABASE']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE')
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hallmanagement.db'
# db = SQLAlchemy(app)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('home.html')

@app.route('/Templates/login', methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/Templates/signup.html', methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@app.route('/Templates/base.html', methods=['POST','GET'])
def base():
    return render_template('base.html')

@app.route('/Templates/dashboard.html', methods=['POST','GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/Templates/systemtickets.html', methods=['POST','GET'])
def systemtickets():
    return render_template('systemtickets.html')

@app.route('/Templates/database.html', methods=['POST','GET'])
def database():
    return render_template('database.html')

if __name__ =="__main__":
    app.run(debug=True)