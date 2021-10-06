from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('home_page.html')


@app.route("/", methods = ['POST'])
def data_insertation():
    user_input = request.form['input_text']
    return user_input

@app.route("/<city>_<country>", methods=['GET'])
def forecast_page(city, country):
    return f"whether in {city}, {country}"


 if __name__ == "__main__":
     # Launch the Flask dev server
     app.run(host="localhost", debug=True)