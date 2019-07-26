from flask import Flask, render_template, url_for, request, redirect, Markup, jsonify
from datetime import datetime as dt  
import datetime
from influxdb import InfluxDBClient
import json
from num_macs import numUniqueMACS, uniqueMACStoday
from num_repeats import getRepeatMACS
from maclookup import getTimeData, getHistoricalData
from functions import parseDatabase, parseDevices

app = Flask(__name__)
    
@app.route('/')
def index():
    devices = parseDevices()
    return render_template('index.html', devices=devices)

@app.route('/num_macs/<dev>/<start>/<end>')
def getMacData(dev, start, end):
    """
    Endpoint which returns number of unique MAC addresses detected for each day
    from the start and end dates for a specified device
    """
    output = []
    mac_start = dt.strptime(start,'%Y-%m-%d')
    mac_end = dt.strptime(end,'%Y-%m-%d')
    numdays = (mac_end - mac_start).days

    for i in range(0, numdays+1):
        date = (mac_start + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        num = numUniqueMACS(dev, date)
        data = {'date':date, 'count':num}
        output.insert(0,data)

    return jsonify(output)

@app.route('/num_macs/<dev>/today')
def getMACSToday(dev):
    """
    Endpoint which returns number of unique MAC addresses detected on the current
    day for a given device
    """
    data = uniqueMACStoday(dev)
    output = []
    time = int(datetime.datetime.now().strftime("%H"))
    for i in range(5):
        output.insert(0, data[time - i - 5])
    return jsonify(output)

@app.route('/num_repeats/<dev>/<start>/<end>/<int:offset>')
def getNumRepeats(dev, start, end, offset):
    output = []
    start = dt.strptime(start,'%Y-%m-%d')
    end = dt.strptime(end,'%Y-%m-%d')
    dates = []
    numdays = (end - start).days

    for i in range(numdays+1):
        string = (start + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        dates.append(string)
    
    for i in range(numdays+1):
        data = getRepeatMACS(dev, offset, dates[i])
        output.append(data)

    return jsonify(output)
    
@app.route('/mac_lookup/<dev>/<MAC>')
def macLookup(dev,MAC):
    output = getTimeData(dev,MAC)
    return jsonify(output)

@app.route('/historical_data/<dev>/<MAC>')
def histData(dev,MAC):
    output = getHistoricalData(dev,MAC)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
