import json
import wiotp.sdk.device
import time

myConfig ={
    "identity":{
    "orgId": "rdegyk",
    "typeId":"safetygad",
    "deviceId":"gad1"
    },
    "auth":{
        "token":"gyg06jzil(!lTGsKxV"
       }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    name="locater"
    #in area location
    #latitude=13.145997614532394 
    #longitude=80.0619303452179

    #out area location
    latitude=13.15412          
    longitude=80.05729
    
    myData={'name':name, 'lat':latitude, 'lon':longitude}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Data published to IBM Iot platform: ",myData)
    time.sleep(2)
    
client.disconnect()
Footer
