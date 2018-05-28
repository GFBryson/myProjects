#define LED_PIN 13
#define BUTTON_PIN 4
#include "config.h"

// button state
int current = 0;
int last = 0;

AdafruitIO_Feed *button_post = io.feed("button_post");


void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(115200);

  //connect to Adafruit
  io.connect();
  while(io.status() < AIO_CONNECTED){//waiting for connection
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print(io.statusText());
  
}

void loop() {
  // grab the current state of the button.
  // we have to flip the logic because we are
  // using INPUT_PULLUP.
  io.run();

  
  if(digitalRead(BUTTON_PIN) == LOW)
    current = 1;
  else
    current = 0;

  // return if the value hasn't changed
  //button_post->save(current);
  if(current == last)
    return;
  Serial.println(current);
  if(current == 1){
    button_post->save("button has been pressed");
  }
  digitalWrite(LED_PIN, current);
  
  last = current;
}

