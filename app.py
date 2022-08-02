from crypt import methods
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hallmanagement.db'
db = SQLAlchemy(app)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('home.html')

@app.route('/Templates/login')
def login():
    return render_template('login.html')

@app.route('/Templates/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/Templates/base.html')
def base():
    return render_template('base.html')

@app.route('/Templates/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/Templates/systemtickets.html')
def systemtickets():
    return render_template('systemtickets.html')

@app.route('/Templates/database.html')
def database():
    return render_template('database.html')

if __name__ =="__main__":
    app.run(debug=True)