import Adafruit_DHT
import time

# Set up DHT sensor
sensor = Adafruit_DHT.DHT11
pin = 17  # GPIO pin where the DHT11 is connected

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print("Temperature: {:.1f}°C, Humidity: {:.1f}%".format(temperature, humidity))
        else:
            print("Failed to read data from sensor. Retrying...")
        time.sleep(2)  # Read every 2 seconds

except KeyboardInterrupt:
    print("Program stopped by user.")
