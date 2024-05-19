import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin connected to the shock sensor
shock_sensor_pin = 18
GPIO.setup(shock_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read the state of the shock sensor
        shock_state = GPIO.input(shock_sensor_pin)
        
        # Check if the shock sensor is triggered
        if shock_state == GPIO.LOW:
            print("Shock sensor is triggered!")
        else:
            print("Shock sensor is not triggered.")
        
        # Add a short delay to avoid excessive polling
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
