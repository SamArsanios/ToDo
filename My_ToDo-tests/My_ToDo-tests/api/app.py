'''
    My ToDo v1.0
    app file
    where the application is run
'''
from flask import Flask
from flask_restful import Api

APP = Flask(__name__)
API = Api(APP)

from .views import Home, User

API.add_resource(Home, '/')
API.add_resource(User, '/sign_up')
if __name__ == "__main__":
    APP.run(debug = True)