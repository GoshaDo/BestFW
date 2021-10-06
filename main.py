from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)


class UserInputForm(FlaskForm):
    user_input = StringField('City or Country',
                             validators=[DataRequired(), Length(min = 2, max = 25)])
    submit = SubmitField("GO!")


@app.route("/home")
def home():
    form = UserInputForm()
    return render_template("home.html", title='Home Page', form=form)


@app.route("/<city>_<country>", methods=['GET'])
def forecast_page(city, country):
    return f"whether in {city}, {country}"


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=False)