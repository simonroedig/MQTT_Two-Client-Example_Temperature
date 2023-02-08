# CLIENT_2: WEMOS D1 MINI
# Is subscribed to "EspThanks" and publishes on "WemosTemperature"
# Measure the Temperature with a sensor module and publishes it
# the Esp32 is subscribed to WemosTemperature and sends back a thank you msg

# USING WEMOS WITH TEMPERATUR AND HUMIDITY SENSOR
# for pins: https://ezcontents.org/wemos-d1-mini-temperature-server
from machine import Pin
import dht
d = dht.DHT11(Pin(2))

def sub_cb(topic, msg):
  print((topic, msg))

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()
  

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  d.measure()
  """
  print("Local print: Temperatur: ", d.temperature())
  print("Local pirnt: Humidity: ", d.humidity())
  """
  try:
    new_message = client.check_msg()
    if new_message != 'None':
      client.publish(topic_pub, str(d.temperature()))
    time.sleep(1)
  except OSError as e:
    restart_and_reconnect()

