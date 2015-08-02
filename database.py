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

def verifyUser(username, password):
    if food_trucks.find({"username": username, "password":password}):
        return True
    return False

def updateFoodTruckLocation(username, x, y):
    food_truck = food_trucks.find_one({"username": username})
    food_truck.loc[0] = x
    food_truck.loc[1] = y
    food_trucks.insert(food_truck)

def getMyProfile(username):
    return food_trucks.find_one({"username": username})

def getTrucks():
    return food_trucks.find(projection={'_id': False, 'password': False, 'username':False})