from flask import Flask, render_template, request
from api import API

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to weather app</h1>'


@app.route('/<location>')
def search_city(location):
    api = API()
    location_list = api.get_loc(location)
    print(location_list)
    return location


if __name__ == '__main__':
    app.run(debug=True)
