from flask import render_template, Flask, request, json, jsonify, session, redirect, url_for
from database import *
from bson.json_util import dumps
#from json import stringify
dictionary = {}
app = Flask(__name__, static_folder='/static/')
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

@app.route('/my-profile')
def myprofile():
    #myprofile = getMyProfile("tacotruck")
    #return render_template('my-profile.html', username=myprofile["username"], description=myprofile["description"], food_truck_name=myprofile["food_truck_name"])
    return render_template('my-profile.html')
@app.route('/sign-up')
def signup():
    print("test")
    return render_template("sign-up.html")

'''
@app.route('/signup', methods=["POST"])
def form():
    text = request.form["text"]
    processed_text = processed_text
    return processed_text
'''
@app.route('/login')
def login():
    return render_template('login.html');
'''
@app.route('/login', methods=["POST"])
def login_post():
    if request.args.get('username'):
        print('username: '+ request.args.get('username'))
        session['username']= request.args.get('username')
    return redirect(url_for("home"))
'''
@app.route('/form', )
def form():
    if request.args.get('username'):
        print("found username")
        username = request.args.get('username')
        password = request.args.get('password')
        print(username)
        print(password)
        if verifyUser(username, password):
            print("veridfied")
            myprofile = getMyProfile(username)
            session['username'] = username
            session['food-truck-name'] = myprofile['food_truck_name']
            session['description'] = myprofile['description']
    return render_template("index.html")

@app.route('/_create_user', methods=["POST"])
def createUser():
    json = request.json
    createFoodTruck(json)
    return "blank"

@app.route('/_update_location', methods=["POST"])
def _update_location():
    json = request.json
    print(json["x"])
    print(json["y"])
    updateFoodTruckLocation(json["username"], json["x"], json["y"])
    return "test"
                                         
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)