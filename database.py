from pymongo import MongoClient
client = MongoClient()
db = client.food_truck_database
food_trucks = db.food_trucks

def createFoodTruck(json):
    food_trucks.insert(json)
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
def updateFoodTruckLocation(username, x, y):
    food_truck = food_trucks.find_one({"username": username})
    food_truck.x = x
    food_truck.y = y
    food_trucks.insert(food_truck)

def getMyProfile(username):
    return food_trucks.find_one({"username": username})