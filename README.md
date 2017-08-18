# P1 DSMR reader for the open source disaggregation project
Open Source project to log data from the DSMR (P1) meter via usb serial cable

## installation

To install the p1 USB reader run the following commands in your terminal:

```
mkdir disaggregation
cd disaggregation
git clone https://github.com/disaggregation/DSMR-P1-usb-logger
```

To run the script after each reboot:
```crontab -e```

Add this line to the crontab file:
 ```@reboot /usr/bin/python /path/to/loggers/usb_p1_logger/schedule_p1_reader.py 2>&1```
 
The file will launch the scheduler at reboot and record data every 10 seconds, which leads to about 1Mb per day. Make sure you have enough space..

## hardware requirements
- raspberry pi
- usb to serial cable (https://www.sossolutions.nl/slimme-meter-kabel)

## data storage
The data will be stored to a sqlite file 'data/yourhash256edmeterserialnumber.db'
Mysql logging is support, but required more setup skills.

# disaggregation
This repository will soon be updates with a working disaggregation model that determines which subload are behind your energy meter.
Pleas visit www.allianders.nl/disaggregation/demo/ to see the current disaggregate allogaritems results. An upload page for your data will be provided soon.

