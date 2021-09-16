#include <Servo.h>

int x;
int pos;

bool servo1 = false; //Pulgar - Amarillo
bool servo2 = false; //Indice - Azul
bool servo3 = false; //Centro - Rojo
bool servo4 = false; //Anular - Verde
bool servo5 = false; //Meñique - BlancoNaranja
Servo myservo1; //Pulgar - Amarillo
Servo myservo2; //Indice - Azul
Servo myservo3; //Centro - Rojo
Servo myservo4; //Anular - Verde
Servo myservo5; //Meñique - BlancoNaranja

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  myservo1.attach(2);
  myservo2.attach(3);
  myservo3.attach(4);
  myservo4.attach(5);
  myservo5.attach(6);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
}

void loop() {

  while (!Serial.available());
  x = Serial.readString().toInt();

  if ( x == 1 ) {
    digitalWrite(8,HIGH);
    if ( servo1 == true ) {
      for (pos = 180; pos >= 0; pos -= 5) { 
        myservo1.write(pos);
        delay(10);
      }
      servo1 = false;
    } else if ( servo1 == false ) {
      for (pos = 0; pos <= 180; pos += 5) {
        myservo1.write(pos);
        delay(10);
      }
      servo1 = true;
    }
    digitalWrite(8,LOW);
  }
  else if ( x == 2 ) {
    digitalWrite(9,HIGH);
    if ( servo2 == true ) {
      for (pos = 180; pos >= 0; pos -= 5) { 
        myservo2.write(pos);
        delay(10);
      }
      servo2 = false;
    } else if ( servo2 == false ) {
      for (pos = 0; pos <= 180; pos += 5) {
        myservo2.write(pos);
        delay(10);
      }
      servo2 = true;
    }
    digitalWrite(9,LOW);
  }
  else if ( x == 3 ) {
    digitalWrite(10,HIGH);
    if ( servo3 == true ) {
      for (pos = 180; pos >= 0; pos -= 5) { 
        myservo3.write(pos);
        delay(10);
      }
      servo3 = false;
    } else if ( servo3 == false ) {
      for (pos = 0; pos <= 180; pos += 5) {
        myservo3.write(pos);
        delay(10);
      }
      servo3 = true;
    }
    digitalWrite(10,LOW);
  }
  else if ( x == 4 ) {
    digitalWrite(11,HIGH);
    if ( servo4 == true ) {
      for (pos = 180; pos >= 0; pos -= 5) { 
        myservo4.write(pos);
        delay(10);
      }
      servo4 = false;
    } else if ( servo4 == false ) {
      for (pos = 0; pos <= 180; pos += 5) {
        myservo4.write(pos);
        delay(10);
      }
      servo4 = true;
    }
    digitalWrite(11,LOW);
  }
  else if ( x == 5 ) {
    digitalWrite(12,HIGH);
    if ( servo5 == true ) {
      for (pos = 180; pos >= 0; pos -= 5) { 
        myservo5.write(pos);
        delay(10);
      }
      servo5 = false;
    } else if ( servo5 == false ) {
      for (pos = 0; pos <= 180; pos += 5) {
        myservo5.write(pos);
        delay(10);
      }
      servo5 = true;
    }
    digitalWrite(12,LOW);
  }

}
