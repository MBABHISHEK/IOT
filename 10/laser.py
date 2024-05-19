import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin connected to the laser emitter
laser_pin = 18
GPIO.setup(laser_pin, GPIO.OUT)

try:
    while True:
        # Turn on the laser
        GPIO.output(laser_pin, GPIO.HIGH)
        print("Laser is on.")
        
        # Wait for a few seconds
        time.sleep(2)
        
        # Turn off the laser
        GPIO.output(laser_pin, GPIO.LOW)
        print("Laser is off.")
        
        # Wait for a few seconds
        time.sleep(2)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
