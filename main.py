from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    return "Best Freaking Whether"


@app.route("/<city>_<country>")
def forecast_page(city, country):
    return f"whether in {city}, {country}"
