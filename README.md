# EC463-SWminiproject-11

## Summary


## Authentication

## Database

The database was built using Cloud Firestore. The database contains one collection, "devices", which holds a document for each home monitor device/sensor. Each device document includes arrays for

Database Organization Chart:
![Cloud Firestore Organization Chart](https://github.com/Myles-Cork/EC463-SWminiproject-11/blob/master/images/EC463SWmini_CloudstoreOrganizationV2.png)

## Sensor API and Simulation

The sensor API is built around the REST API. It uses HTTP patch requests from devices to update the database. For security, new devices must be added by an admin through the firebase console. The deviceId and userId are both required in to link a device to a user in the database.

A python script (mocksensor.py) for simulating a sensor device writing to the database can be found in the mocksensor folder.

## Setup
install extra dependencies:
npm install --save express body-parser firebase-functions-helper
