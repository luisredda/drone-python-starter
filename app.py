#!./bin/python
from waitress import serve
from flask import Flask, jsonify, request
from os import environ

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():

    return "This is my first Drone.io Build!"

if __name__ == '__main__':
    #app.run(debug=False)
    serve(app, host='0.0.0.0', port=5000)
