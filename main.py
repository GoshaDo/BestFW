from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return "render_template('home_page.html')"
    if request.method == 'POST':
        user_input = request.form
        return f"{user_input}"


@app.route("/<city>_<country>", methods=['GET'])
def forecast_page(city, country):
    return f"whether in {city}, {country}"
