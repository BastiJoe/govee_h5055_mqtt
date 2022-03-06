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

	Battery state?	Channel		Temp a	Low	High		Temp b	Low	High			
manuf data =  cf040400	47	2f	06	1800	0100	ffff	06	1600	0200	ffff	0000		Channel 1 and 2
manuf data =  cf040400	47	6f	06	1600	0300	ffff	06	1700	0400	ffff	0000		Channel 3 and 4
manuf data =  cf040400	47	af	06	ffff	0500	ffff	06	1600	0600	ffff	0000		Channel 5 and 6

![image](https://user-images.githubusercontent.com/47536246/156933808-df32e4ac-7358-4c9b-bde4-50370c3df9e8.png)


The Data comes in three payloads (containing data for 2 of the 6 sensors)
The Channel Byte indicates the payload number 0, 1, 2 (indicated by the highest 2 Bits) as well as a conenction state of all 6 sensors (lowest 6 bits)
Example: 
0xBE
1011 1110
The payload is for sensors 5 and 6. Sensors 2, 3, 4, 5, 6 are connected. Sensor 1 is not connected.![image](https://user-images.githubusercontent.com/47536246/156933822-0dbc700d-fcb4-4613-8da1-6f7e237b86ee.png)
