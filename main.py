from flask import Flask, render_template, request, redirect, url_for
from api import API

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home_page.html")


@app.route('/', methods=['POST'])
def user_input():
    text = request.form['text']
    return redirect(url_for('search_loc', location=text))


@app.route('/loc/<location>')
def search_loc(location):
    api = API()
    location_list = api.get_loc(location)
    return render_template("choose_location.html", loc_list=location_list)


if __name__ == '__main__':
    app.run(debug=True)
