from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    return "Best Freaking Whether"


@app.route("/whether_forecast")
def forecast_page():
    return "rainy all day"
