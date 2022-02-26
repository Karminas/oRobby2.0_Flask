from urllib.request import urlopen
from flask import Flask, render_template
from flask import *
from sqlalchemy import null, true
import requests
import json
from classes.user import User


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", title="Api REST test 1")


@app.route('/addUser')
def addUser():
    return render_template("addUser.html", title="Api REST/ -addUser-")


@app.route('/getUser')
def getUser():
    return render_template("getUser.html", title="Api REST / -getUser-")


@app.route('/login')
def login():
    return render_template("login.html", title="Api REST / -login-")


@app.route('/allUsers')
def allUsers():

    url = "http://192.168.0.236:8080/user/"
    response = urlopen(url)
    userList = json.loads(response.read())

    return render_template("allUSers.html", title="Api REST / -all users-", apiResponse=json.dumps(userList, sort_keys=False, indent=2))


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        id = request.form.get('Id')
        print(id)

    if(id != null):
        url = "http://192.168.0.236:8080/user/{Id}"
        payload = {'pId': id}
        response = requests.get(url, params=payload)
        user = response.json()

    return render_template("user.html", title="Api REST / -user-", apiResponse=json.dumps(user, sort_keys=False, indent=2))


if __name__ == '__main__':
    app.run(debug=true)
