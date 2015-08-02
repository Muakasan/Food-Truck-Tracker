from flask import render_template, Flask, request, json
dictionary = {}
app = Flask(__name__, static_folder='/Users/Main_Account/Documents/Homework/Food-Truck-Tracker/static')

@app.route('/')
def home():
    #return 'Index page'
    return render_template('index.html')

@app.route('/home')
def returnHome():
    return render_template('index.html');

@app.route('/map')
def map():
    return render_template('map.html');

@app.route('/signup')
def signup():
    return render_template('signup.html');

@app.route('/login')
def login():
    return render_template('login.html');

@app.route('/_create_user', methods=["POST"])
    # Get the parsed contents of the form data
    json = request.json
    print(json)
    # Render template
    return jsonify(json)
    
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)