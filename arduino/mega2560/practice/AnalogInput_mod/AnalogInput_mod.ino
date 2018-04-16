/*
  Analog Input

  Demonstrates analog input by reading an analog sensor on analog pin 0 and
  turning on and off a light emitting diode(LED) connected to digital pin 13.
  The amount of time the LED will be on and off depends on the value obtained
  by analogRead().

  The circuit:
  - potentiometer
    center pin of the potentiometer to the analog input 0
    one side pin (either one) to ground
    the other side pin to +5V
  - LED
    anode (long leg) attached to digital output 13
    cathode (short leg) attached to ground

  - Note: because most Arduinos have a built-in LED attached to pin 13 on the
    board, the LED is optional.

  created by David Cuartielles
  modified 30 Aug 2011
  By Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogInput
*/

int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 52;      // select the pin for the LED
int ledPin2 = 48;
int sensorValue = 0;  // variable to store the value coming from the sensor
bool alt_set = false;
void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);
  pinMode(ledPin2,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);
  
  // stop the program for <sensorValue> milliseconds:
  Serial.print(sensorValue);
  delay(sensorValue);
  Serial.print("\n");
  if(sensorValue<=170){
    digitalWrite(52,HIGH);
  }else if(sensorValue<=340){
    digitalWrite(50,HIGH);
  }else if(sensorValue<=510){
    digitalWrite(48,HIGH);
  }else if(sensorValue<=680){
    digitalWrite(46,HIGH);
  }else if(sensorValue<=850){
    digitalWrite(44,HIGH);
  }else if(sensorValue<=1024){
    digitalWrite(42,HIGH);
  }
  delay(sensorValue);
if(sensorValue<=170){
    digitalWrite(52,LOW);
  }else if(sensorValue<=340){
    digitalWrite(50,LOW);
  }else if(sensorValue<=510){
    digitalWrite(48,LOW);
  }else if(sensorValue<=680){
    digitalWrite(46,LOW);
  }else if(sensorValue<=850){
    digitalWrite(44,LOW);
  }else if(sensorValue<=1024){
    digitalWrite(42,LOW);
  }
  
}
