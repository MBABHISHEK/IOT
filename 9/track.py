import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pin connected to the tracking sensor
tracking_pin = 17

# Set up the GPIO pin as an input
GPIO.setup(tracking_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(tracking_pin) == GPIO.HIGH:
            print("Track detected!")
        else:
            print("No track detected")
        time.sleep(0.1)  # Adjust delay as needed
except KeyboardInterrupt:
    GPIO.cleanup()
