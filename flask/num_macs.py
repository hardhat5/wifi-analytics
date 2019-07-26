from datetime import datetime as dt
import datetime
from influxdb import InfluxDBClient
from dateutil import tz
from functions import parseDatabase
import pymongo

def uniqueMACStoday(dev):
    """
    Returns a list whose each element is a dictionary of the form
    {time:number} where time refers to a particular hour and number
    is the number of unique MAC addresses that were detected in that
    particular hour

    Returns: List of dict objects
    """
    # Creating a MongoDB client and switching to the relevant database
    database = parseDatabase('InfluxDB')
    influx_client = InfluxDBClient(host=database['host'], port=database['port'])
    influx_client.switch_database('datadump')
    
    date=dt.today().strftime("%Y-%m-%d 00:00:00")
    start = dt.strptime(date,"%Y-%m-%d %H:%M:%S")

    times = []
    for i in range(0,25):
        times.append((start + datetime.timedelta(hours=i)).strftime("%Y-%m-%d %H:%M:%S"))

    mac_count = [0 for i in range(25)]

    final_list = []

    for i in range(0, 24):
        macs = []
        data = dict()
        results = influx_client.query("select * from {} where time >= '{}' and time < '{}'".format(dev, times[i], times[i+1]))
        points = results.get_points()
        for point in points:
            if (point['MAC'] not in macs) and (not point['MAC'].startswith('da:a1:19')):
                macs.append(point['MAC'])
        data['time'] = times[i][10:-3]
        data['count'] = len(macs)
        final_list.append(data)
    return final_list

def numUniqueMACS(dev, date=dt.now().strftime("%Y-%m-%d")):
    """
    Returns the number of unique MAC addresses that were detected on a given date
    """
    # Creating a MongoDB client and switching to the relevant database
    database = parseDatabase('MongoDB')
    mongo_client = pymongo.MongoClient(database['host'], int(database['port']))
    db = mongo_client[dev]
    col = db[date]
    results = col.find()
    return col.count_documents({})

def getUniqueMACS(dev, date=dt.now().strftime("%Y-%m-%d")):
    """
    Returns a dict containing all the unique MAC addresses that were detected on a given day
    """
    # Creating a MongoDB client and switching to the relevant database
    database = parseDatabase('MongoDB')
    mongo_client = pymongo.MongoClient(database['host'], int(database['port']))
    db = mongo_client[str(dev)]
    
    output = []
    col = db[date]
    results = col.find()
    for item in results:
        data = {}
        data['MAC'] = item['MAC']
        output.append(data)
    return output 

