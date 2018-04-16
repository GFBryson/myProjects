/* switches and led's
 *  
 */

int inputPins[] = {2,3,4,5,6}; //array for switches
int ledPins[]={52,50,48,46,11}; //array for leds

void setup(){
  for(int i=0;i<5;i++){
    pinMode(ledPins[i],OUTPUT);//declare as output
    pinMode(inputPins[i],INPUT);//declare as input
    digitalWrite(inputPins[i],HIGH);//enable pull up resistors
  }
  Serial.begin(9600);//send output to serial monitor
}
void loop(){
  for( int i=0;i<5;i++){//for each LED-Pin set
    int val = digitalRead(inputPins[i]);//read inout val
    Serial.print(val);
    Serial.print(":");
    Serial.print(i);
    Serial.print("\n");
    if(val == LOW){//check is switch is on
      digitalWrite(ledPins[i],HIGH);//LED on
    }
    else{
      digitalWrite(ledPins[i],LOW);//LED off
    }
  }
}
