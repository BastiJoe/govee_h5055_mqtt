#!/usr/bin/python
'''
This is a python Bluetooth advertisement scanner for the Govee brand Bluetooth
temperature sensor.  Tested on model H5075 using Raspberry Pi 3.
Temperature, humidity, and battery level is published as MQTT messages.

Credit:  I used information for Govee advertisement format from
github.com/Thrilleratplay/GoveeWatcher

Install dependencies:
 sudo apt-get install python3-pip libglib2.0-dev
 sudo pip3 install bluepy
 sudo apt install -y mosquitto mosquitto-clients
 sudo pip3 install paho-mqtt

Needs sudo to run on Raspbian
sudo python3 govee_ble_mqtt_pi.py

Run in background
sudo nohup python3 govee_ble_mqtt_pi.py &

'''

from __future__ import print_function

from time import gmtime, strftime, sleep
from bluepy.btle import Scanner, DefaultDelegate, BTLEException
import sys
import paho.mqtt.client as mqtt
import pickle

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print("on message")
    
client = mqtt.Client()
mqtt_prefix = "/sensor/govee"
mqtt_gateway_name = "/Mosquitto"

debug = []

class ScanDelegate(DefaultDelegate):
    
    global client
    # mqtt message topic/payload:  /prefix/gateway_name/mac/
    global mqtt_prefix
    global mqtt_gateway_name
    
    def handleDiscovery(self, dev, isNewDev, isNewData):
        #if (dev.addr == "a4:c1:38:xx:xx:xx") or (dev.addr == "a4:c1:38:xx:xx:xx"):
        if dev.addr[:8]=="a4:c1:38":          
            
            #returns a list, of which the [2] item of the [3] tupple is manufacturing data
            adv_list = dev.getScanData()
            
            #debug
            if 0:
                debug.append(adv_list)
                with open('adv_list.pickle', 'wb') as handle:
                    pickle.dump(debug, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print(isNewData)
            #check if received data is payload
            if (adv_list[0][2] == "05") & isNewData:
                
                
                adv_manuf_data = adv_list[2][2]
                
                print("manuf data = ", adv_manuf_data)
                
                #read channel1 measured value, low byte, high byte switched
                sensor_a_meas = int(adv_manuf_data[16:18] + adv_manuf_data[14:16], 16)
                sensor_a_low = int(adv_manuf_data[20:22] + adv_manuf_data[18:20], 16)
                sensor_a_high = int(adv_manuf_data[24:26] + adv_manuf_data[22:24], 16)
                
                sensor_b_meas = int(adv_manuf_data[30:32] + adv_manuf_data[28:30], 16)
                sensor_b_low = int(adv_manuf_data[34:36] + adv_manuf_data[32:34], 16)
                sensor_b_high = int(adv_manuf_data[38:40] + adv_manuf_data[36:38], 16)
                
                
                #extract Channel number
                ch_hex = adv_manuf_data[10:12]
                ch_int = int(ch_hex,16)
                #keep only the first 2 bits
                #ch_nr = ch_int & int(0b11000000)
                #konvert to 8 bit string
                ch_nr = format(ch_int, "08b")
                #extract channel number from first 2 bits
                channel = 2*int(ch_nr[0:2],2) + 1
                
                #check in lower 6 bits, if channel is connected
                #die beiden Bitmuster mit AND verknüpfen, und schauen, ob der Sensor connected ist
                #z.B. Sensor 5 => 2**5 = 32 mit Bitmuster 10 0000
                #nun schauen wir ob diese 1 sich im Bitmuster 1011 0011 wiederfindet (hier wären z.B. Sensor 1,2,5,6) verbunden)
                ch_a_connected = ch_int & 2**(channel-1) > 0
                ch_b_connected = ch_int & 2**(channel) > 0              


                mac=dev.addr
                signal = dev.rssi
                mqtt_topic = mqtt_prefix + mqtt_gateway_name + mac + "/"
                #client.publish(mqtt_topic+"alarm", alarm, qos=0)
                
                if ch_a_connected:
                    #print("mac=", mac, "   percent humidity ", hum_percent, "   temp_F = ", temp_F, "   battery percent=", battery_percent, "  rssi=", signal)
                    mqtt_topic = mqtt_prefix + mqtt_gateway_name + mac + "/Channel_" + str(channel) + "/"

                    #client.publish(mqtt_topic+"rssi", signal, qos=0)
                    client.publish(mqtt_topic+"temp", sensor_a_meas, qos=0)
                    client.publish(mqtt_topic+"low", sensor_a_low, qos=0)
                    client.publish(mqtt_topic+"high", sensor_a_high, qos=0)
                
                if ch_b_connected:
                    #client.publish(mqtt_topic+"battery_pct", battery_percent, qos=0)
                    mqtt_topic = mqtt_prefix + mqtt_gateway_name + mac + "/Channel_" + str(channel + 1) + "/"
        
                    #client.publish(mqtt_topic+"rssi", signal, qos=0)
                    client.publish(mqtt_topic+"temp", sensor_b_meas, qos=0)
                    client.publish(mqtt_topic+"low", sensor_b_low, qos=0)
                    client.publish(mqtt_topic+"high", sensor_b_high, qos=0)
                
                
            sys.stdout.flush()

scanner = Scanner().withDelegate(ScanDelegate())

#replace localhost with your MQTT broker
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

#while True:
scanner.scan(5.0, passive=True)

