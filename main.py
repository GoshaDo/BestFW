from flask import Flask, render_template, request, redirect, url_for
from api import API

app = Flask(__name__)
loc = ""

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
    location_list = enumerate(location_list)
    return render_template("choose_location.html", loc_list=location_list)


@app.route('/loc/<location>', methods=['POST'])
def choose_loc(location):
    text = "chosen location"
    return redirect(url_for('weather', location=location))


@app.route('/weather/<location>')
def weather(location):
    text = f"weather in {location}"
    return text


if __name__ == '__main__':
    app.run(debug=True)
