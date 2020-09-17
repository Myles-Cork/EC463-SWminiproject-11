# EC463-SWminiproject-11: Home Monitor

### Taqiya Chowdhury and Myles Cork

Our project is hosted on https://ec463-swminiproject-11.firebaseapp.com and https://ec463-swminiproject-11.web.app


## Summary

For this Software Mini Project, we created a web application called Home Monitor that is hosted on Firebase and written in HTML/CSS, Python and JavaScript. The app allows the user to monitor their home's temperature and humidity in multiple rooms. It receives and plots updated temperature and humidity every 15 minutes from a simulated sensor.


## Authentication

The user login is based around an SSO, using their Google Account, in order to reduce user application logins to one login for security and convenience. To authenticate users with Firebase using their Google Account, the sign-in flow was handled with the Firebase Javascript SDK to create an instance of the Google provider object and prompting users with a pop-up window. Google Accounts was chosen because of its widespread use.


## Database

The database was built using Cloud Firestore. The database contains one collection, "devices", which holds a document for each home monitor device/sensor.
The javascript code in example1.html takes in the documents associated with the authenticated user from firestore, finds out how many devices it needs to place in the .html, appends new rows to a table, and fills each row with data using ids.

Database Organization Chart:
![Cloud Firestore Organization Chart](https://github.com/Myles-Cork/EC463-SWminiproject-11/blob/master/images/EC463SWmini_CloudstoreOrganizationV2.png)


## Sensor API and Simulation

The sensor API is built around the REST API. It uses HTTP patch requests from devices to update the database. For security, new devices must be added by an admin through the firebase console. The deviceId and userId are both required in to link a device to a user in the database.

A python script (mocksensor.py) for simulating a sensor device writing to the database can be found in the mocksensor folder.


## Verification

In order to verify that the Home Monitor web app met all of its deliverables, the website was tested by loggin in with different Google Accounts using the SSO feature. Upon successful login, the user is directed to a web page showing temperature and humidity of each device in their home. The sensor API is used to simulate the temperature and humidity at all times, updating the values on the webpage. The graphs for the simulated sensors are updated every 15 minutes.

## Test Cases

Case: Google Authentication - User inputs wrong email address, login invalid -> Test Success
Case: Google Authentication - User input correct email address, login valid -> Test Success
Case: mocksensor.py - User inputs wrong device, database not updated -> Test Success

## Demonstrations (bu.edu email required):

### Authentication/SSO, Multiple Users, Sensor API, Realtime Updates, Moving Devices Between Users:
https://drive.google.com/file/d/1yxEwKMwqey6UkGPaxlhJyClx2BtCoUEp/view?usp=sharing
This demonstration shows multiple users signing in, using mocksensor.py to update the database with information and moving devices between users (excluding the inputted deviceId’s for security), and the web app’s device page updating in real time. This demonstration used mocksensor.py’s default values for update speed, so the graphs update every 15 minutes (not in this video).

### Multiple Users, Sensor API, Realtime (Faster) Graph Updates
https://drive.google.com/file/d/1Cenm5dkpqlLYmLY_lGV8H2dujYSRFNBL/view?usp=sharing
This demonstration shows using mocksensor.py to update the database with and the web app’s device page updating in realtime. This demonstration used modified mocksensor.py’s values for update speed, so the graphs update every few seconds.

### Demonstration Drive Folder (All of the above):
https://drive.google.com/drive/folders/1w4qlGLsrzm89koznBIVgXqmCsQ1QgGbN?usp=sharing

Note: If you would like a deviceId (or more than one) to use in mocksensor.py and associate with your accounts, let us know and we can send it/them to you.


## Setup

Setting up the firebase webapp requires Node.js, firebase CLI, and a clone of this repository

Follow the basic firebase setup guides: https://firebase.google.com/docs/guides

Deploy the project to firebase.

install extra dependencies for mocksensor.py:
npm install --save express body-parser firebase-functions-helper


## Project Timeline

Tuesday, 09/08/2020 - We discussed the project deliverables and discussed a layout of the web app. We decided to use Firebase Firestore for our database service. In order to better navigate Firebase, HTML/CSS, and JavaScript, we focused on familiarizing ourselves with a codelabs and coding tutorials, often using Firebase Guides and W3Schools as a resource.  

Sunday, 09/13/2020 - We created a Firebase project, completed the initial setup and pushed it to GitHub. The front end development for the web app was started with a welcome page that would lead to the SSO Google login and the database updating function for Firebase was completed.

Monday, 09/14/2020 - The device simulation program to output temperature and humidity values was created. At this point, the Firestore database was organized into a collection of users, which encompassed all users based on their userID, with a device subcollection per user for each device. In the front end, SSO authentication was completed with a login button, with some debugging errors.

Tuesday, 09/15/2020 - For the front end, the welcome page was improved with better formatting and a backgroun and a web page was created to display the temperature and humidity graphs. The Firestore database was re-organized to be a collection of devices, which holds a document for each home monitor device (see above in Database).

Wednesday, 09/16/2020 - The layout of the graph web page was completed with the graphs being displayed in row by 2 columns set up, displaying temperature and humidity side by side for one device, using the Python functions. The userID was printed on the web page above the graphs by setting an observer on the Auth object.

Thursday, 09/16/2020 - Multiple devices are now available on the graph web page, depicting plots of temperature and humidity in multiple rooms with realtime updates. The front end design was tweaked for easier visualization for the user.


## References
Firebase Guides: https://firebase.google.com/docs/guides
W3Schools: https://www.w3schools.com
