from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import sys

mypubnubconfig = PNConfiguration()
mypubnubconfig.subscribe_key = 'sub-c-231884a6-14a6-11e7-bc52-02ee2ddab7fe'
mypubnubconfig.publish_key = 'pub-c-898d4c55-2abe-4317-b23c-c20ec9f09d19'
pubnub = PubNub(mypubnubconfig)


data = 'wakwauu'

def publish_callback(result, status):
 pass

pubnub.publish().channel("my_channel").message(data)\
 .async(publish_callback)
