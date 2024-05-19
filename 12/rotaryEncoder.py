import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the rotary encoder
encoder_pin1 = 18
encoder_pin2 = 23
button_pin = 24

# Initialize the state variables
last_encoded = 0
last_state = GPIO.input(encoder_pin1)
position = 0

# Set up GPIO pins
GPIO.setup(encoder_pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoder_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to handle the rotary encoder rotation
def rotary_callback(channel):
    global last_encoded, position
    MSB = GPIO.input(encoder_pin1)
    LSB = GPIO.input(encoder_pin2)
    encoded = (MSB << 1) | LSB
    sum = (last_encoded << 2) | encoded
    if sum == 0b1101 or sum == 0b0100 or sum == 0b0010 or sum == 0b1011:
        position += 1
    elif sum == 0b1110 or sum == 0b0111 or sum == 0b0001 or sum == 0b1000:
        position -= 1
    last_encoded = encoded

# Add event detection to the rotary encoder pins
GPIO.add_event_detect(encoder_pin1, GPIO.BOTH, callback=rotary_callback)
GPIO.add_event_detect(encoder_pin2, GPIO.BOTH, callback=rotary_callback)

try:
    while True:
        # Read the state of the push-button
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.LOW:
            print("Button is pressed!")
        else:
            print("Button is not pressed.")

        # Print the current position of the rotary encoder
        print("Position:", position)

        # Add a short delay
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
