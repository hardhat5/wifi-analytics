from influxdb import InfluxDBClient
import pymongo
from datetime import datetime as dt
from datetime import timedelta
import datetime
from dateutil import tz
from num_macs import getUniqueMACS
from functions import parseDatabase

def getTimeData(dev, MAC):
    """
    Returns current day metrics for a given MAC address by querying MongoDB
    """
    # Creating a MongoDB client and switching to the relevant database
    database = parseDatabase('MongoDB')
    mongo_client = pymongo.MongoClient(database['host'], int(database['port']))
    db = mongo_client[dev]
    
    time_data = []
    date=dt.now().strftime("%Y-%m-%d")
    
    # Switching to the current day collection in MongoDB and getting the relevant document
    col = db[date]
    results = col.find({'MAC':MAC})
    
    data = dict()
    for i in results:
        
        data = i

    if data=={}:
        return {'data':'Not found'}
    else:
        data.pop('_id', None)
        return data

def getHistoricalData(dev, MAC):
    """
    Returns a dict containing the duration for a given MAC address for the last 5 days
    """
    # Creating a MongoDB client and switching to the relevant database
    database = parseDatabase('MongoDB')
    mongo_client = pymongo.MongoClient(database['host'], int(database['port']))
    db = mongo_client[dev]
    
    # Creating an array consisting of the dates for which data has to be retrieved
    base = datetime.datetime.today() - datetime.timedelta(days=1)
    date_list = [base - datetime.timedelta(days=x) for x in range(0, 5)]
    
    data = []
    # Loop to get data for the last five days
    for date in date_list:
        date_string = date.strftime("%Y-%m-%d")
        col = db[date_string]
        temp = dict()
        results = col.find({'MAC':MAC})
        for i in results:
            temp = i
        if not temp=={}:
            temp['date'] = date_string
            temp.pop('_id', None)
            to_pop = ['First detection', 'Last detection', 'Number', 'MAC', 'Last updated']
            for item in to_pop:
                temp.pop(item, None)
            data.append(temp)

        else:
            temp['date'] = date_string
            temp['Duration'] = 0
            data.append(temp)
            continue
                    

    return data

print(getTimeData('device_01', '5c:99:60:bf:44:43'))