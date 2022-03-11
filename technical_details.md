sample payload:

manuf data = cf040400464906ffffffff2c01061700ffff2c010000

image

The Data comes in three payloads (containing data for 2 of the 6 sensors) The Channel Byte indicates the payload number 0, 1 or 2 (indicated by the highest 2 Bits) as well as a connection state of all 6 sensors (lowest 6 bits)

Example:

0xBE

1011 1110

The payload is for sensors 5 and 6. Sensors 2, 3, 4, 5, 6 are connected. Sensor 1 is not connected.





sample mqtt raw data:
home/OpenMQTTGateway/BTtoMQTT/A4C138CF0404 {"id":"A4:C1:38:CF:04:04","mac_type":0,"manufacturerdata":"cf0404003b0806ffffffff2c0106ffffffff2c010000","rssi":-74}


sample converted data:
/sensor/govee/Mosquitto/a4:c1:38:cf:04:04/batt 70
/sensor/govee/Mosquitto/a4:c1:38:cf:04:04/batt 70
/sensor/govee/Mosquitto/a4:c1:38:cf:04:04/batt 70
/sensor/govee/Mosquitto/a4:c1:38:cf:04:04/Channel_4/temp 24
/sensor/govee/Mosquitto/a4:c1:38:cf:04:04/Channel_4/low 65535
/sensor/govee/Mosquitto/a4:c1:38:cf:04:04/Channel_4/high 300



