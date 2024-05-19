import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin connected to the ball switch
ball_pin = 18
GPIO.setup(ball_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read the state of the ball switch
        ball_state = GPIO.input(ball_pin)
        
        # Check if the ball switch is triggered
        if ball_state == GPIO.LOW:
            print("Ball switch is triggered!")
        else:
            print("Ball switch is not triggered.")
        
        # Add a short delay to avoid excessive polling
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
