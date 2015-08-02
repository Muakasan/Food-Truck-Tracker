from pymongo import MongoClient
client = MongoClient()
db = client.food_truck_database
food_trucks = db.food_trucks

def createFoodTruck2(json):
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

#def createFoodTruck(username, password, food_truck_name, description, menu_path, x, y):
#	food_trucks.insert("username": username, "password": password, "food_truck_name":food_truck_name, "description":description, "menu_path": menu_path, "x":x, "y":y)
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

