import requests
import random
from collections import deque
import time
from datetime import datetime, timedelta

print("This script sends mock data to the database under the deviceId specified\n")
deviceId = input("Enter a deviceId: ")


numPoints = 10 #number of datapoints to keep track of
updateTime = 5 #seconds between current temp updates
historyUpdateTime = 60 * 15 #seconds between history upates. History updates are when the arrays of previous temp/humidity values update
historyUpdateIteration = historyUpdateTime/updateTime #number of iterations of current time updates inbetween history updates
numUpdates = 100 #total number of times to update (must be greater than numPoints*historyUpdateIteration for a full cycle of generated data points through the arrays)

#The following are for calculating new values for Temperature and Humidity
tempmax = 80
tempmin = 65
humidmax= 50
humidmin= 40
tempshift = 1
humidshift= 1
prevtemp = random.randint(tempmin,tempmax) #aka the start temperature
prevhumid= random.randint(humidmin,humidmax) #aka the start humidity

Temperature = deque([0]*numPoints)
Humidity = deque([0]*numPoints)
SampleTimes = deque([0]*numPoints) #Number at index corresponds to the time Temperature/Humidity at the

prewarmAns = ' '
while prewarmAns != 'Y' and prewarmAns != 'N':
    print("Prewarm the history data? (Arrays start full with randomly generated values)") #saves on function calls for graph testing
    prewarmAns = input("Enter Y or N: ")

if prewarmAns == 'Y':
    for k in range(numPoints-1,-1,-1):
        Temperature[k]= max(tempmin,  min(tempmax, prevtemp   + random.randint(-tempshift,tempshift)))
        Humidity[k]   = max(humidmin, min(humidmax, prevhumid + random.randint(-humidshift,humidshift)))
        prevtemp = Temperature[k]
        prevhumid = Humidity[k]
        SampleTimes[k] = (datetime.now() - timedelta(seconds=(historyUpdateTime*(k+1)))).strftime("%H:%M:%S")

userAns = ' '
while userAns != 'Y' and prewarmAns != 'N':
    print("Change userid for this device?")
    userAns = input("Enter Y or N: ")

useridAns = ' '
if userAns == 'Y':
    useridAns = input("Enter new userId for this device: ")
    r = requests.patch('https://us-central1-ec463-swminiproject-11.cloudfunctions.net/webApi/api/v1/device/' + deviceId,
        data = {
            'userId' : useridAns
        })
    print(r)
    # print content of request
    print(r.content)

for i in range(0, numUpdates):
    start = time.process_time()

    currentTemp = max(tempmin,  min(tempmax, prevtemp   + random.randint(-tempshift,tempshift)))   #new temperature is previous shifted randomly up to tempshift + or - and clamped between tempmin and tempmax
    currentHumid= max(humidmin, min(humidmax, prevhumid + random.randint(-humidshift,humidshift))) #new humidity is previous shifted randomly up to humidshift + or - and clamped between humidmin and humidmax

    prevtemp = currentTemp
    prevhumid = currentHumid

    if i%historyUpdateTime == 0:
        Temperature.rotate(1)
        Humidity.rotate(1)
        SampleTimes.rotate(1)
        Temperature[0] = currentTemp
        Humidity[0] = currentHumid
        SampleTimes[0] = datetime.now().strftime("%H:%M:%S")


    r = requests.patch('https://us-central1-ec463-swminiproject-11.cloudfunctions.net/webApi/api/v1/device/' + deviceId,
        data = {
            'CurrentTemperature' : currentTemp,
            'CurrentHumidity' : currentHumid,
            'Temperature' : Temperature,
            'Humidity' : Humidity,
            'SampleTimes' : SampleTimes
        })
    # check status code for response recieved
    # success code - 200
    print(r)
    # print content of request
    print(r.content)

    sleepTime = max(0.0 , updateTime - (time.process_time() - start)) #ensures time between updates is the same as updateTime and/or non-negative

    time.sleep(sleepTime)
    print("Update Time:")
    print(sleepTime)

print("Done")
