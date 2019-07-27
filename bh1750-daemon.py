#!/usr/bin/python
import smbus
import time
import paho.mqtt.client as mqtt
from configparser import ConfigParser
import json

config = ConfigParser(delimiters=('=', ))
config.read('config.ini')

topic = config['mqtt'].get('topic', 'lux/luxtest')
decim_digits = config['sensor'].getint('decimal_digits', 2)
sleep_time = config['sensor'].getint('interval', 60)
pitype = config['sensor'].get('pitype', 'smbus.SMBus(1)')
luxres = config['sensor'].get('luxres', 0x20)

bus = smbus.SMBus(int(pitype))

# Define some constants from the datasheet
DEVICE     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {}".format(rc))

client = mqtt.Client()
client.on_connect = on_connect
username, password = config['mqtt'].get("username", None), config['mqtt'].get("password", None)
if username:
    client.username_pw_set(username, password)

client.connect(config['mqtt'].get('hostname', 'homeassistant'),
               config['mqtt'].getint('port', 1883),
               config['mqtt'].getint('timeout', 60))
client.loop_start()

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,luxres)
  return convertToNumber(data)

while True:

    entry = {'lux': round(readLight(), decim_digits)}
    client.publish(topic, json.dumps(entry))
    print('Published.', entry, 'Sleeping ...')

    time.sleep(sleep_time)
