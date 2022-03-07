sample payload:

manuf data = cf040400464906ffffffff2c01061700ffff2c010000

image

The Data comes in three payloads (containing data for 2 of the 6 sensors) The Channel Byte indicates the payload number 0, 1 or 2 (indicated by the highest 2 Bits) as well as a connection state of all 6 sensors (lowest 6 bits)

Example:

0xBE

1011 1110

The payload is for sensors 5 and 6. Sensors 2, 3, 4, 5, 6 are connected. Sensor 1 is not connected.
