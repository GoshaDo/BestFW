from flask import Flask, render_template, request, redirect, url_for
from api import API
from utilities import loc_list_to_human

app = Flask(__name__)
api = API()


@app.route('/')
def index():
    return render_template("home_page.html")


@app.route('/', methods=['POST'])
def user_input():
    text = request.form['text']
    return redirect(url_for('search_loc', location=text))


@app.route('/loc/<location>')
def search_loc(location):
    location_list = api.get_loc(location)
    location_list = enumerate(loc_list_to_human(location_list))
    return render_template("choose_location.html", loc_list=location_list)


@app.route('/loc/<location>', methods=['POST'])
def choose_loc(location):
    op = request.form['options']
    return redirect(url_for('weather_present', location=location, option=op))


@app.route('/weather/<location>/<option>')
def weather_present(location, option):
    option = int(option)
    country = api.loc_list[option][1]
    dist = api.loc_list[option][3]
    city = api.loc_list[option][0]
    state = api.loc_list[option][2]
    print(">>>>>",country, dist, city, state)
    return render_template("weather_present.html", Country=country, State=state, District=dist, City=city)


if __name__ == '__main__':
    app.run(debug=True)
