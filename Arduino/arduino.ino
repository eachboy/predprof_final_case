#include <Servo.h>
int hall = A0;
int pos = 0;
Servo servo_x; 
Servo servo_y1;
Servo servo_y2; 
int pos_x = 0;
int pos_y = 90;
void setup() {
  servo_y1.attach(6);
  servo_y2.attach(7);
  servo_x.attach(9);  
  Serial.begin(9600);
}
String value;

void loop() {
   int rawValue = analogRead(hall);
  //  float voltage = rawValue * (5.0/1023) * 1000;
  //  float resitance = 10000 * ( voltage / ( 5000.0 - voltage) );
  //  float gauss = voltage/ resitance * 3 ;
  //  Serial.println(gauss);

  // Serial.print("Voltage:"); Serial.print(voltage); Serial.print("mV");
  // Serial.print(", Resistance:"); Serial.print(resitance); Serial.println("Ohm");
  // Serial.println("---------------------------------------");
  // delay(500);

    for (pos = 0; pos <= 90; pos += 1) 
    { 
    servo_x.write(pos);              
    delay(15);                       
    }
    for (pos = 90; pos >= 0; pos -= 1)
    { 
    servo_x.write(pos);              
    delay(15);                       
    }
    for (pos = 90; pos <= 180; pos += 1)
    { 
    servo_y1.write(pos);  
    servo_y2.write(pos);             
    delay(15);                       
    }
    for (pos = 180; pos >= 90; pos -= 1)
    { 
    servo_y1.write(pos);  
    servo_y2.write(pos);            
    delay(15);                       
    }
    delay(5000);
  
  for (pos_x = 0;pos_x <= 180;pos_x+=1){
    servo_x.write(pos_x);
    delay(15);
    for (pos_y = 70;pos_y <=160;pos_y+=1){
      servo_y1.write(pos_y);
      servo_y2.write(pos_y);
      delay(15);
      Serial.println(String(int(pos_x)) + " " + String(int(pos_y)) + " " + String(int(analogRead(hall))));
    }
  }
  Serial.println("finish");
  delay(10000);
}
