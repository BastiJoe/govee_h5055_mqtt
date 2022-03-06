# govee_h5055_mqtt
Govee H5055 BBQ Thermometer MQTT Gateway

I started with Openhab recently. As i was looking for devices to connect, i thought about connecting my bbq thermometer (govee h5055) to openhab.
As i am passionate in bbq, i thought it would be nice to have the charts of my next pulled pork on my raspberry.
![image](https://user-images.githubusercontent.com/47536246/156933357-ed17c286-0bf9-4eb4-ba4a-143f196c3c1e.png)

I went on the internet to find a repo but there wasn't one on that specific device. But I found this great repo:
https://github.com/tsaitsai/govee_bluetooth_gateway
Thanks to Eric!

It took me some time to decode the bits and bytes of the govee communication but now it is working.


sample payload:

manuf data =  cf040400464906ffffffff2c01061700ffff2c010000

![image](https://user-images.githubusercontent.com/47536246/156933808-df32e4ac-7358-4c9b-bde4-50370c3df9e8.png)

The Data comes in three payloads (containing data for 2 of the 6 sensors)
The Channel Byte indicates the payload number 0, 1 or 2 (indicated by the highest 2 Bits) as well as a connection state of all 6 sensors (lowest 6 bits)

Example: 

0xBE

1011 1110

The payload is for sensors 5 and 6. Sensors 2, 3, 4, 5, 6 are connected. Sensor 1 is not connected.
