from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('base.html')

@app.route('/Templates/dashboard.html')

def dashboard():
    return render_template('dashboard.html')

@app.route('/Templates/systemtickets.html')

def systemtickets():
    return render_template('systemtickets.html')

if __name__ =="__main__":
    app.run(debug=True)