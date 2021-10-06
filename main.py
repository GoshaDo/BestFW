from flask import Flask, render_template, request
from api import API

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home_page.html")


@app.route('/', methods=['POST'])
def user_input():
    text = request.form['user_input']
    return text


@app.route('/<location>')
def search_city(location):
    api = API()
    location_list = api.get_loc(location)
    print(location_list)
    return location


if __name__ == '__main__':
    app.run(debug=True)
