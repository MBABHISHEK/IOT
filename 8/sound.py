import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pin connected to the sound sensor
sound_pin = 17

# Set up the GPIO pin as an input
GPIO.setup(sound_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(sound_pin) == GPIO.HIGH:
            print("Big sound detected!")
        else:
            print("Small sound detected")
        time.sleep(0.1)  # Adjust delay as needed
except KeyboardInterrupt:
    GPIO.cleanup()
