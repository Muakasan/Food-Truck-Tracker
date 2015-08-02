from flask import render_template, Flask, request, json, jsonify
from database import *
from bson.json_util import dumps
#from json import stringify
dictionary = {}
app = Flask(__name__, static_folder='/home/muakasan/Documents/Food-Truck-Tracker/static')
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

@app.route('/')
def home():
    sumSessionCounter()
    return render_template('index.html')

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/home')
def returnHome():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/truck_array', methods=["POST"])
def getArray():
    truck_list = getTrucks() 
    return dumps(truck_list)

@app.route('/myprofile')
def myprofile():
    myprofile = getMyProfile("Username")
    return render_template('myprofile.html', username=myprofile["username"], description=myprofile["description"], food_truck_name=myprofile["foodTruckName"])

@app.route('/signup', methods=["POST"])
def signup_form_post():
    text = request.form["text"]
    processed_text = processed_text
    return processed_text

@app.route('/login')
def login():
    return render_template('login.html');
'''
@app.route('/login', methods=["POST"])
def login_post():
    return 
'''
def login():
    return render_template('login.html');

@app.route('/myprofile')
def myprofile():
    myprofile = getMyProfile("Username")
    return render_template('myprofile.html', username=myprofile["username"], description=myprofile["description"], food_truck_name=myprofile["food_truck_name"])

@app.route('/_create_user', methods=["POST"])
def _create_user():
    print("nlej")
    json = request.json
    createFoodTruck(json)
    #return jsonify(json)
    return "blank"
    
@app.route('/_update_location', methods=["POST"])
def _update_location():
    json = request.json
    updateFoodTruckLocation(json["username"], json["x"], json["y"])
                                         
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)