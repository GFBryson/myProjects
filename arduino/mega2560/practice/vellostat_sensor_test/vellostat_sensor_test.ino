/*pressure sensor test code multiple inputs
 * 
 * sensor made with vellostat and conductive wire
 */

int pressure_LED = 52; //led will light up when pressure sensor is activated
int sensorPin=A0;//read from analogue0
int sensor_value =0;
int old_value =0;
void setup() {
  // put your setup code here, to run once:
  pinMode(pressure_LED,OUTPUT);
  Serial.begin(9600);//to read output
}

void loop() {
  // put your main code here, to run repeatedly:
  sensor_value = analogRead(sensorPin);
  if (sensor_value!=old_value){
    old_value=sensor_value;
    Serial.print(sensor_value);
    Serial.print("\n");
  }
  if(sensor_value >= 1){
    digitalWrite(pressure_LED,HIGH);
  }
  else{
    digitalWrite(pressure_LED,LOW);
  }
  if (sensor_value>=2){
   digitalWrite(50,HIGH);
  }else{
    digitalWrite(50,LOW);
  }
  if (sensor_value>=3){
   digitalWrite(48,HIGH);
  }else{
    digitalWrite(48,LOW);
  }
  if (sensor_value>=4){
   digitalWrite(46,HIGH);
  }else{
    digitalWrite(46,LOW);
  }
  if (sensor_value>=5){
   digitalWrite(44,HIGH);
  }else{
    digitalWrite(44,LOW);
  }
}
