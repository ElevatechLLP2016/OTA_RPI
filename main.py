import ugit
from machine import Pin
import time

pin = Pin(0,Pin.IN,Pin.PULL_UP)
if pin.value() is 0:
    ugit.pull_all()
    
#main code here
TIME_MS=100
LED = Pin("LED", Pin.OUT)
#LED1 = Pin(4, Pin.OUT)
while True:
    LED.off()
    #LED1.on()
    time.sleep_ms(TIME_MS)
    LED.on()
   # LED1.off()
    time.sleep_ms(TIME_MS)
