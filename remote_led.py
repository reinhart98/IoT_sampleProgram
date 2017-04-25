import RPi.GPIO as GPIO
import time
import sys
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

mypubnubconfig = PNConfiguration()
mypubnubconfig.subscribe_key = 'sub-c-231884a6-14a6-11e7-bc52-02ee2ddab7fe'
mypubnubconfig.publish_key = 'pub-c-898d4c55-2abe-4317-b23c-c20ec9f09d19'
pubnub = PubNub(mypubnubconfig)

channels = 'disco'

GPIO.setmode(GPIO.BOARD)
li = 12
GPIO.setup(li,GPIO.OUT)

def data_callback(m,channel):
 print(m)
 if m['onit']==1:
  GPIO.output(li,True)
  time.sleep(20) 

pubnub.publish().channel(channels).message(' ').async(data_callback)

