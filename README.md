# govee_h5055_mqtt
Govee H5055 BBQ Thermometer MQTT Gateway

I started with Openhab recently. As i was looking for devices to connect, i thought about connecting my bbq thermometer (govee h5055) to openhab.
As i am passionate in bbq, i thought it would be nice to have the charts of my next pulled pork on my raspberry.

https://www.amazon.de/Govee-Grillthermometer/dp/B07T5SG3QZ

![image](https://user-images.githubusercontent.com/47536246/156933357-ed17c286-0bf9-4eb4-ba4a-143f196c3c1e.png)

I went on the internet to find a repo but there wasn't one on that specific device. But I found this great repo:
https://github.com/tsaitsai/govee_bluetooth_gateway
Thanks to Eric!

It took me some time to decode the bits and bytes of the govee communication but now it is working.

Install instuctions

cd ~

git clone https://github.com/BastiJoe/govee_h5055_mqtt

cd ~/govee_h5055_mqtt/

sudo python3 govee_h5055_mqtt.py

I am using it with crontab

sudo crontab -e

add this line to run script every minute:

*/1 * * * * python3 /home/pi/govee_h5055_mqtt/govee_h5055_mqtt.py
