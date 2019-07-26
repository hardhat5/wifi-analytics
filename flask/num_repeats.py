from datetime import datetime as dt
import datetime
from influxdb import InfluxDBClient
from dateutil import tz
from num_macs import getUniqueMACS
from functions import parseDatabase

def getRepeatMACS(dev, offset=5, date=datetime.datetime.today().strftime("%Y-%m-%d")):
    """
    Returns the number of repeated MACS detected on a given date upto a 
    specified offset.

    Example - if date = 2019-07-08 and offset = 5, the function will return
    the number of MAC addresses that were detected on 2019-07-08 as well as
    on any day between 2019-07-08 and 2019-07-03
    """
    database = parseDatabase('InfluxDB')
    influx_client = InfluxDBClient(host=database['host'], port=database['port'])
    influx_client.switch_database('datadump')
    # Generate Query string   

    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    offset_date = date - datetime.timedelta(days=offset)

    date = date.strftime("%Y-%m-%d")
    offset_date = offset_date.strftime("%Y-%m-%d")

    # Iterate over all unique MACS 
    MACS = getUniqueMACS(dev, date)
    repeats = 0
    new = 0
    for MAC in MACS:
        results = influx_client.query("select count(*) from {} where time >= '{}' and time < '{}' and MAC='{}'".format(dev, offset_date, date, MAC['MAC']))
        points = results.get_points()
        for point in points:
            if point['count_strength']>0:
                repeats += 1
            else:
                new += 1
            
    return {'date': date, 'count': repeats}