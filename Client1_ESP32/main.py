# CLIENT_1: ESP32
# Is subscribed to "WemosTemperature" and publishes on "EspThanks"
# Receives the temperature that the Wemos measure
# and responses with a thank you message

# Callback func: runs whenever a message is published on a topic the ESP is subscribed to
def sub_cb(topic, msg):
  print("Subcribed to topic :", topic)
  print("Received temperature: ", msg)
  print(" ")

# Connect to broker and subscribe to a topic
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  # connect client to broker
  client.connect()
  # client is subscribing to "topic_sub" = temperature, see boot.py
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

# receive and publish messages
while True:
  try:
    # checks whether pending message from server is available  
    client.check_msg()
    # check whether 5 sec have passed snce last message was sent
    if (time.time() - last_message) > message_interval:
      msg = b'Hello, I am ESP32 and received your temperature #%d' % counter
      # CLIENT PUBLISHES HERE
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()
