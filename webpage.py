from flask import render_template, Flask, request, json
dictionary = {}
app = Flask(__name__, static_folder='/Users/Main_Account/Documents/Homework/HackTJ project/static')

@app.route('/')
def home():
    #return 'Index page'
    return render_template('index.html')