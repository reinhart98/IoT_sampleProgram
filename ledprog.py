import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
li = 12
GPIO.setup(li,GPIO.OUT)
try :
 while True:
  GPIO.output(li,True)
  print 'on'
  time.sleep(1)
  GPIO.output(li,False)
  print 'off'
  time.sleep(1)
except KeyboardInterrupt:
 GPIO.cleanup()
