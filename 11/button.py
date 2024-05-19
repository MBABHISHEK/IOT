import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pins connected to the button and the laser emitter
button_pin = 18
laser_pin = 17

# Set up the button pin as an input with a pull-up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up the laser pin as an output
GPIO.setup(laser_pin, GPIO.OUT)

try:
    while True:
        # Check if the button is pressed
        if GPIO.input(button_pin) == GPIO.LOW:
            # Turn on the laser
            GPIO.output(laser_pin, GPIO.HIGH)
            print("Laser is on.")
        else:
            # Turn off the laser
            GPIO.output(laser_pin, GPIO.LOW)
            print("Laser is off.")
        
        # Add a short delay to debounce the button
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
