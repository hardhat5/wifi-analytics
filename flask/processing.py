from influxdb import InfluxDBClient
import pymongo
from datetime import datetime, timedelta
from dateutil import tz
from timeloop import Timeloop
from functions import parseDatabase, parseDevices

tl = Timeloop()

devices = parseDevices()

# Creating an InfluxDB client and switching to the relevant database
influx = parseDatabase('InfluxDB')
influx_client = InfluxDBClient(host=influx['host'], port=influx['port'])
influx_client.switch_database('datadump')

def getMACSFromInflux(dev, date=datetime.today().strftime("%Y-%m-%d")):
    """
    Returns a list of unique MACS detected on a given day by a given device
    """
    MACS = []
    date = datetime.strptime(date, '%Y-%m-%d')
    start = date.strftime("%Y-%m-%d")
    end = (date + timedelta(days=1)).strftime("%Y-%m-%d")
    query = "select * from {} where time>='{}' and time<'{}'".format(dev, start, end)
    results = influx_client.query(query)
    points = results.get_points()
    for point in points:
        
        if point['MAC'] not in MACS:
            data = {}
            MACS.append(point['MAC'])
    return MACS

def getTimeData(dev, MAC, date=datetime.now().strftime("%Y-%m-%d")):
    """
    Returns time of first detection, last detection and duration for a given 
    MAC address on a given day
    """

    time_data = dict()
    
    date = datetime.strptime(date, '%Y-%m-%d')
    start = date.strftime("%Y-%m-%d")
    end = (date + timedelta(days=1)).strftime("%Y-%m-%d")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    
    results = influx_client.query("select first(*) from {} where MAC='{}' and time >= '{}' and time <=  '{}'".format(dev, MAC, start, end))
    points = results.get_points()
    local_first = datetime.now()
    for point in points:
        utc = datetime.strptime(point['time'][:19],'%Y-%m-%dT%H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        local_first = utc.astimezone(to_zone)
        time_data['first'] = local_first.strftime("%H:%M:%S")
    
    
    results = influx_client.query("select last(*) from {} where MAC='{}'".format(dev, MAC))
    points = results.get_points()
    local_last = datetime.now()
    for point in points:
        utc = datetime.strptime(point['time'][:19],'%Y-%m-%dT%H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        local_last = utc.astimezone(to_zone)
        time_data['last'] = local_last.strftime("%H:%M:%S")

    duration = local_last.replace(tzinfo=None) - local_first.replace(tzinfo=None)
    duration_in_s = str(duration.total_seconds()) 
    time_data['duration'] = duration_in_s
   
    return time_data

def mongoUpdate(date = datetime.now().strftime("%Y-%m-%d")):
    """
    Updates MongoDB after processing the data captured on a given day
    """

    # Creating client for MongoDB
    mongo = parseDatabase('MongoDB')
    mongo_client = pymongo.MongoClient(mongo['host'], int(mongo['port']))
    
    for device in devices:

        MACS = getMACSFromInflux(device, date)
        local_db = mongo_client[device]
        collection = local_db[date]

        if MACS==[]:
            continue

        for MAC in MACS:

            if MAC=='nown)' or MAC.startswith('da:a1:19'):
                continue


            time_data = getTimeData(device, MAC, date)

            post = {
                'MAC': MAC,
                'First detection': time_data['first'],
                'Last detection': time_data['last'],
                'Duration': time_data['duration'],
                'Last updated': datetime.now().strftime("%H:%M:%S")
                }


            if not collection.count_documents({'MAC': MAC}):
                post_id = collection.insert_one(post)

            else:
                post_id = collection.update_one({'MAC': MAC}, {"$set":post})


@tl.job(interval=timedelta(seconds=60))
def timelyUpdate():
    
    mongoUpdate('2019-07-10')

    print("Updated")

if __name__ == "__main__":
     tl.start(block=True)


