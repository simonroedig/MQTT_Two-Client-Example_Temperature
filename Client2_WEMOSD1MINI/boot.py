# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


#----------------------------#
# CLIENT_2: WEMOS D1 MINI

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = '<replace>'
password = '<relace>'

# MQTT BROKER IP ADDRESS (test broker)
mqtt_server = 'test.mosquitto.org'

# ESP's ID
client_id = ubinascii.hexlify(machine.unique_id())

# SUBSCRIBE TOPIC
topic_sub = b'EspThanks'

# PUBLISH TOPIC
topic_pub = b'WemosTemperature'

last_message = 0
message_interval = 5
counter = 0

# ESP IS STATATION/CLIENT
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

