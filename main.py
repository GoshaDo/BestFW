from flask import Flask, render_template, request, redirect, url_for
from api import API
from utilities import loc_list_to_human
import database as db
from CONF import DB_FILE


app = Flask(__name__)
api = API()
db.init_db(DB_FILE)

@app.route('/')
def index():
    return render_template("home_page.html", NotFound=False)


@app.route('/')
def not_found():
    return render_template("home_page.html", NotFound=True)


@app.route('/', methods=['POST'])
def user_input():
    text = request.form['text']
    api.__init__()
    if not api.get_loc(text):
        return redirect(url_for('not_found'))
    return redirect(url_for('search_loc', location=text))


@app.route('/loc/<location>')
def search_loc(location):
    location_list = api.loc_list
    location_list = enumerate(loc_list_to_human(location_list))
    return render_template("choose_location.html", loc_list=location_list)


@app.route('/loc/<location>', methods=['POST'])
def choose_loc(location):
    op = request.form['options']
    return redirect(url_for('weather_present', location=location, option=op))


@app.route('/weather/<location>/<option>')
def weather_present(location, option):
    option = int(option)
    if not api.choose_city(option):  # need to check the return status code
        return redirect(url_for('/'))
    country = api.loc_list[option][1]
    dist = api.loc_list[option][3]
    city = api.loc_list[option][0]
    state = api.loc_list[option][2]
    max_temp = api.max_temp
    min_temp = api.min_temp
    humidity = api.humidity
    status = api.status
    zipped = zip(max_temp.items(), min_temp.items(), humidity.items())

    db.insert_db(DB_FILE, api)

    return render_template("playground.html",
                           Country=country, State=state, District=dist, City=city,
                           Max_Temp=max_temp, Min_Temp=min_temp, Humidity=humidity,
                           Status=status, ZippedItems=zipped)


if __name__ == '__main__':
    app.run(debug=True)
