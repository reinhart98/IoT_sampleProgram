from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import sys

mypubnubconfig = PNConfiguration()
mypubnubconfig.subscribe_key = 'your subkey'
mypubnubconfig.publish_key = 'your pubkey'
pubnub = PubNub(mypubnubconfig)


data = 'wakwauu'

def publish_callback(result, status):
 pass

pubnub.publish().channel("my_channel").message(data)\
 .async(publish_callback)
