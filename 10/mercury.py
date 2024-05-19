import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin connected to the tilt switch
tilt_pin = 18
GPIO.setup(tilt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read the state of the tilt switch
        tilt_state = GPIO.input(tilt_pin)
        
        # Check if the tilt switch is tilted
        if tilt_state == GPIO.LOW:
            print("Tilt switch is tilted!")
        else:
            print("Tilt switch is not tilted.")
        
        # Add a short delay to avoid excessive polling
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
