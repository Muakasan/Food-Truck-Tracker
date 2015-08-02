from pymongo import MongoClient
client = MongoClient()
db = client.food_truck_database
food_trucks = db.food_trucks

def updateFoodTruck(username, ):

def createFoodTruck(username, password, food_truck_name, description, menu_path, x, y):
	food_trucks.insert("username": username, "password": password, "food_truck_name":food_truck_name, "description":description, "menu_path", menu_path, "x":x, "y":y)

def updateFoodTruckLocation(username, x, y):

