MQTT example with two clients, a test broker, and two topics.

WEMOS publishes on „WemosTemperature“ to which
ESP32 is subscribed to. So the ESP32 receives
the temperature that the WEMOS measures.
The ESP32 also publishes a message with a counter on „EspThanks“ 
to which the WEMOS is subscribed to. 

![Setup](setup.png)