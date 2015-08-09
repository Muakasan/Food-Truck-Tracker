from pymongo import MongoClient
client = MongoClient()
db = client.food_truck_database
food_trucks = db.food_trucks

def createFoodTruck(json):
    print(json["username"])
    print("ayyy")
    food_trucks.insert(json)
    print("meh")
'''
def updateFoodTruck(username, ):
    food_trucks.update_one({
      '_id': p['_id']
    },{
      '$set': {
        'd.a': existing + 1
      }
    }, upsert=False)
'''

'''
def updateFoodTruck(username, ):
    food_trucks.update_one({
      '_id': p['_id']
    },{
      '$set': {
        'd.a': existing + 1
      }
    }, upsert=False)
'''

def verifyUser(username, password): #broken
    print(food_trucks.find_one({"username": username, "password":password}))
    if food_trucks.find_one({"username": username, "password":password}):
        return True
    return False

def updateFoodTruckLocation(username, x, y):
    print("went to database")
    print(username)
    print(x)
    print(y)
    food_trucks.find_one_and_update({'username': username}, {'$set': {'loc': [x,y]}})
'''
def getLocation(username):
    food_trucks.find({'username':username}, projection={'loc'=True})
'''
def getMyProfile(username):
    return food_trucks.find_one({"username": username}, projection={'_id:': False, 'password': False, 'username': False})

def getTrucks():
    return food_trucks.find(projection={'_id': False, 'password': False, 'username':False})