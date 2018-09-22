# flask uses jinja to render templates
# http://jinja.pocoo.org/
from flask import Flask, render_template
import json


def weather_report(date):
    with open('./data/seattle-data.json', 'r') as jsonfile:
        weather_data = json.loads(jsonfile.read())

    # get the data for the requested date and return it as a json string
    return json.dumps(weather_data[date])


# create a Flask app
app = Flask(__name__)

# set Flask routes so that we can serve HTTP traffic on them


# / is the website root, the entry point
@app.route('/')
def index():
    # render_template searches directory templates
    return render_template('index.html')


# route passes url date to weather function
# allow for empty date
# https://stackoverflow.com/questions/14023664/flask-url-route-route-several-urls-to-the-same-function
@app.route('/weather/')
@app.route('/weather/<date>')
def weather(date=None):
    if date is None:
        return render_template('page.html', date='', weather_report='n/a')

    spaced_date = ' ' + date
    weather_string = weather_report(date)

    # pass info to render_template
    return render_template('page.html', date=spaced_date, weather_report=weather_string)


# https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # ipv4
    # '0.0.0.0' accessible to any device on the network, including localhost http://127.0.0.1
    # for example on server machine http://0.0.0.0:5000/ may redirect to localhost http://127.0.0.1:5000
    # https://www.digitalocean.com/community/questions/accessing-debugger-for-flask-127-0-0-1-5000
    host = '0.0.0.0'

    # alternatively could use ipv6
    # https://stackoverflow.com/questions/21673068/dual-ipv4-and-ipv6-support-in-flask-applications#21689979
    # host = '::'
    # e.g. http://[::]:9092/

    # flask default port is 5000
    port = '5000'
    # port = '9092'

    app.run(debug=True, host=host, port=port)
