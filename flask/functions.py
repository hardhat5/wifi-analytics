#Contains helper functions which are commonly used by other functions
from datetime import datetime as dt
import datetime
from influxdb import InfluxDBClient
from dateutil import tz
import configparser

def parseDatabase(db):
    """
    Reads config.ini and returns a dictionary containing the hostname and port for an input database

    Valid inputs: 'InfluxDB', 'MongoDB'
    """
    data = {}
    config = configparser.ConfigParser()
    config.read('config.ini')
    options = config.options(db)
    for option in options:
        data[option] = config.get(db, option)

    return data

def parseDevices():
    """
    Read config.ini and returns a list containing all the device names which are 
    set to 'true' in the config file
    """
    devices = []
    config = configparser.ConfigParser()
    config.read('config.ini')
    options = config.options('Devices')
    for option in options:
        if config.get('Devices', option) == 'true':
            devices.append(option)
    
    return devices

