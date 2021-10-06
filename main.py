from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to weather app</h1>'

@app.route('/city')
def search_city():
    city = request.args.get('q')
    return city

if __name__ == '__main__':
    app.run(debug=True)
