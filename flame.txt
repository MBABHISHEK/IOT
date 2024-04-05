int led = 13; // define the LED pin
int digitalPin = 2; // KY-026 digital interface
int analogPin = A0; // KY-026 analog interface
int digitalVal; // digital readings
int analogVal; //analog readings

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(digitalPin, INPUT);
  //pinMode(analogPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  // Read the digital interface
  digitalVal = digitalRead(digitalPin); 
    analogVal = analogRead(analogPin); 
    Serial.println(analogVal);
  if(analogVal >45) // if flame is detected
  {
    digitalWrite(led, HIGH);
    Serial.println("Fire detected");
    // turn ON Arduino's LED
  }
  else
  {
    digitalWrite(led, LOW); 
    Serial.println("Fire not detected");// turn OFF Arduino's LED
  }
  //Serial.println(analogVal); // print analog value to serial

  delay(100);
}
