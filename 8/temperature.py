import Adafruit_DHT
import time

# Set the GPIO pin for DHT11 sensor
DHT_PIN = 4  # Adjust this to match your setup

def read_dht11():
    # Attempt to get a sensor reading
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
    return humidity, temperature

def main():
    try:
        while True:
            humidity, temperature = read_dht11()
            if humidity is not None and temperature is not None:
                print("Temperature: {:.2f}°C, Humidity: {:.2f}%".format(temperature, humidity))
            else:
                print("Failed to read from DHT11 sensor")
            time.sleep(1)  # Update reading every one second
    except KeyboardInterrupt:
        print("Exiting program")

if __name__ == "__main__":
    main()
