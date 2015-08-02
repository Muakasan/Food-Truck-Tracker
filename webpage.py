from flask import render_template, Flask, request, json
dictionary = {}
app = Flask(__name__, static_folder='/Users/Main_Account/Documents/Homework/Food-Truck-Tracker/static')

@app.route('/')
def home():
    #return 'Index page'
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html');

@app.route('/signup')
def signup():
    return render_template('signup.html');

@app.route('/login')
def login():
    return render_template('login.html');

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)