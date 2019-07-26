# Wifi Analytics Dashboard

Dashboard to display Wifi data about devices in a vicinity by capturing probe requests.

## Motivation

Retail stores need as much information as they can about their customers to stay competitive. Since smartphones are ubiquitous, valuable insights can be gained from information broadcasted by the smartphones of customers without invading their privacy(by capturing probe requests). This project guides you on how to set up wifi routers to capture data and delivers a dashboard to visualize insights from that data.

## Screenshots
![screenshot](https://github.com/hardhat5/Wifi-Analytics-Dashboard/blob/master/dashboard?raw=true "Dashboard")

## Tech/frameworks used

1. OpenWrt
2. Flask
3. Chart.js
4. Python 3

## Quickstart

### 1. Selecting a device

Make sure your wifi router satisfies the following requirements:

1. Supports OpenWrt
2. Supports monitor mode

To find out if your device is compatible, or to find compatible devices, read more here

### 2. Setting up the server

1. Install InfluxDB and edit the config file to allow for more than 10000 values per tag.
2. Start the InfluxDB server and create a database called 'datadump'
3. Install MongoDB, start the server and create a database called 'wifi'

### 3. Setting up the device

1. Install OpenWrt(an open source operating system targetting embedded devices) on your router.
2. Install `airmon-ng`(a tool to enable monitor mode) on the router.
3. Install `tcpdump`(a tool to capture wifi packets for analysis) on the router.
4. Download the `capture.sh` script.
5. Edit device name of your choice and IP address of your InfluxDB server in the script.
6. Replace `mon0` with the name of your wireless interface when monitor mode is activated in the script.

More information about these steps can be found here

### 4. Gathering the data

1. Install the `pipenv` library for Python
3. Download the pipfile and copy it to a folder of your choice
3. Navigate to that folder and run `pipenv install` - this will create a virtual environment with all dependencies installed.
4. Run the `processing.py` script on the server - this will process the InfluxDB data and push to the MongoDB database regularly.
5. Enable monitor mode on the router.
6. Execute the `capture.sh` script to start packet capture

### 5. Running the dashboard

With the virtual environment activated, run`app.py` and the dashboard will be live at `localhost:5000`

## Bugs

1. ‘nowkn)’
2. Script hangs sometimes

## Further Work

1. Enable SSL encryption
2. On device config
3. Register MAC addresses 
4. Trilateration
5. Filtering

## Reference

1. Setting up
2. Project layout
3. Adding a new graph to the dashboard

