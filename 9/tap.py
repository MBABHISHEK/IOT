import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
touch_pin = 17

# Setup the input pin for the touch sensor
GPIO.setup(touch_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(touch_pin) == GPIO.HIGH:
            print("Touch sensor touched!")
        else:
            print("Touch sensor not touched")
        time.sleep(0.1)  # Wait for 0.1 seconds before reading again
except KeyboardInterrupt:
    GPIO.cleanup()
