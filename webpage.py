from flask import render_template, Flask, request, json, jsonify
from database import *
dictionary = {}
app = Flask(__name__, static_folder='/home/muakasan/Documents/Food-Truck-Tracker/static')

@app.route('/')
def home():
    #return 'Index page'
    print("hello world")
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

@app.route('/signup', methods=["POST"])
def signup_form_post():
    text = request.form["text"]
    processed_text = processed_text
    return processed_text

@app.route('/login')
def login():
    return render_template('login.html');

@app.route('/myprofile')
def myprofile():
    myprofile = getMyProfile("Username")
    return render_template('myprofile.html', username=myprofile["username"], description=myprofile["description"], food_truck_name=myprofile["foodTruckName"])

@app.route('/_create_user', methods=["POST"])
def _create_user():
    #print("asdfasfa");
    # Get the parsed contents of the form data

    json = request.json
    createFoodTruck(json)
    print(json["username"])

    #print(json)
    # Render template
    return jsonify(json)
    
    
@app.route('/_update_location', methods=["POST"])
def _update_location():
    json = request.json
    updateFoodTruckLocation(json["username"], json["x"], json["y"])
                                         
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)