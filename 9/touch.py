Import RP1.GPIO as GPIO

import time GPIO.setmode (GPIO.BCH)

button pin=24

GPIO.setup(button_p pin, GPIO.IN, pull up down GPIO.PUD DOWN)

while True:
  touch detected=GPIO.input(button pin) 
  if touch detected == 1:
    print("touch detected")
  else:
    print("No touch detected")
    time.sleep(3)
