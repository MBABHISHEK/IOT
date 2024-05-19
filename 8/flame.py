import RPi.GPIO as GPIO
import time

DO_PIN = 7  # GPIO pin connected to DO pin of the flame sensor

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Initialize the GPIO pin as an input
GPIO.setup(DO_PIN, GPIO.IN)

try:
    while True:
        flame_state = GPIO.input(DO_PIN)
        if flame_state == GPIO.HIGH:
            print("No flame => No fire detected.")
        else:
            print("Flame present => Fire detected.")
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
