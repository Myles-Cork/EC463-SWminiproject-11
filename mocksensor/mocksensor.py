import requests
import random
from collections import deque
import time

print("This script sends mock data to the database under the deviceId specified\n")
deviceId = input("Enter a deviceId: ")

numPoints = 10 #number of datapoints to keep track of.
updateTime = 5 #seconds between updates
numUpdates = 20 # number of times to update the temperature

#The following are for calculating new values for Temperature and Humidity
tempmax = 80
tempmin = 65
humidmax= 50
humidmin= 40
tempshift = 2
humidshift= 2
prevtemp = 72
prevhumid= 45

Temperature = deque([0]*numPoints)
Humidity = deque([0]*numPoints)


for i in range(0, numUpdates):
    Temperature.rotate(1)
    Humidity.rotate(1)

    Temperature[0] = max(tempmin,  min(tempmax, prevtemp   + random.randint(-tempshift,tempshift)))   #new temperature is previous shifted randomly up to tempshift + or - and clamped between tempmin and tempmax
    Humidity[0]    = max(humidmin, min(humidmax, prevhumid + random.randint(-humidshift,humidshift))) #new humidity is previous shifted randomly up to humidshift + or - and clamped between humidmin and humidmax
    prevtemp = Temperature[0]
    prevhumid = Humidity[0]

    r = requests.patch('https://us-central1-ec463-swminiproject-11.cloudfunctions.net/webApi/api/v1/device/' + deviceId,
        data ={
            'Temperature' : Temperature,
            'Humidity' : Humidity
        })
    # check status code for response recieved
    # success code - 200
    print(r)
    # print content of request
    print(r.content)
    time.sleep(updateTime)

print("Done")
