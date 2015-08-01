
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template
import requests
import get_weather

@route('/')
def hello_world():
    return template("chat")
@route('/tempanalysis')
def temp_analysis():
    return template("Temp_Light")
@route('/map')
def hello_map():
    req = requests.get('https://data.sparkfun.com/output/YGVlo4OwmWCzVvm8pjAw.json?')
    data = req.json()
    return template("map",data=data)
@route('/stream')
def stream_data():
    req = requests.get('https://data.sparkfun.com/output/WGDJmjvGrgTAMQ7v71Zr.json')
    data = req.json()
    #return template('sample',data=data)
    return template("sample",data=data)
    #from bottle import response
    #from json import dumps
    #rv = [{ "id": 1, "name": "Test Item 1" }, { "id": 2, "name": "Test Item 2" }]
    #response.content_type = 'application/json'
    #return dumps(rv)
@route('/chart')
def chart():
    req = requests.get('https://data.sparkfun.com/output/YGVlo4OwmWCzVvm8pjAw.json?')
    data = req.json()
    return template("chart", data=data)
@route('/weather')
def weather():
    req = requests.get('https://data.sparkfun.com/output/8dNAzZgaorH19l1WgRR7.json?')
    data = req.json()
    return template("weather", data=data)
@route('/weatherstream')
def classmap() :
    req = requests.get('https://data.sparkfun.com/output/G2qzL2WqraSR7opxjGNL.json?')
    data = req.json()
    return template("classmap", data=data)

@route('/mapnew')
def map_route():
    list = get_weather.get_weather_list()
    states = []
    reds = []
    greens = []
    blues = []
    for item in list:
        states.append(item)
        reds.append(list[item]['humidity']*2)
        greens.append(0)
        blues.append(int(list[item]['temp']-273)*5)
    return template("usafinished", states = states, reds = reds, greens = greens, blues = blues)
@route('/samplenew')
def sample_route():
    list = get_weather.get_weather_list()
    i = 10
    states = ''
    colors = ''
    for item in list:
        states = states + '"' + item + '",'
        colors = colors + '' + str(i) + ','
        i = i + 4
    return template("sample1",states=states,colors=colors)


application = default_app()
