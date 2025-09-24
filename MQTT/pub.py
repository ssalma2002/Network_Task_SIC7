import paho.mqtt.client as paho
import time
import random

def on_publish(client, userdata, mid):
    print(f"Temperature = {temperature}" )
 
client = paho.Client()
client.on_publish = on_publish
client.connect('broker.mqttdashboard.com', 1883)
client.loop_start()

while True:
    temperature = random.randint(1, 40)
    (rc, mid) = client.publish('encyclopedia/temperature', str(temperature), qos=1)
    # print(temperature)
    time.sleep(2)

