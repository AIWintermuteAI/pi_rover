#include <Servo.h>
#include <AFMotor.h>
int motorSpeedMax = 250;
int motorSpeedMed = 150;
int motorSpeedMin = 100;
int pos_t = 90; 
int pos_p = 90; 
int doOnce =0;
Servo pan;
Servo tilt;
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);
char incomingByte; // variable to receive data from the serial port

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps

  // turn on motor
  motor1.setSpeed(motorSpeedMed);
  motor2.setSpeed(motorSpeedMed);
  motor3.setSpeed(motorSpeedMed);
  motor4.setSpeed(motorSpeedMed);
  pan.attach(9); 
  tilt.attach(10); 
  pan.write(pos_p); 
  tilt.write(pos_t); 
  
}

void loop() {
  
  if( Serial.available() > 0 ) // if data is available to read
{
incomingByte = Serial.read(); // read it and store it in 'incomingByte'
doOnce = 0;
}

if( incomingByte == 'i' )
{
 motor1.setSpeed(motorSpeedMax);
 motor2.setSpeed(motorSpeedMax);
 motor3.setSpeed(motorSpeedMax);
 motor4.setSpeed(motorSpeedMax);
}

if( incomingByte == 'o' )
{
 motor1.setSpeed(motorSpeedMed);
 motor2.setSpeed(motorSpeedMed);
 motor3.setSpeed(motorSpeedMed);
 motor4.setSpeed(motorSpeedMed);
}

if( incomingByte == 'p' )
{
 motor1.setSpeed(motorSpeedMin);
 motor2.setSpeed(motorSpeedMin);
 motor3.setSpeed(motorSpeedMin);
 motor4.setSpeed(motorSpeedMin);
}

  if( incomingByte == '1' )
{
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}

  if( incomingByte == '2' )
{
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}

  if( incomingByte == '3' )
{
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}


 if( incomingByte == '4' )
{
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}
 
 if( incomingByte == 's' )
{
 motor1.run(RELEASE);
 motor2.run(RELEASE);
 motor3.run(RELEASE);
 motor4.run(RELEASE);
}

 if( incomingByte == 'q' && doOnce == 0)
{
pos_p = pos_p+10;
pan.write(pos_p); 
doOnce = 1;
}

 if( incomingByte == 'w' && doOnce == 0)
{
pos_p = pos_p-10;
pan.write(pos_p);
doOnce = 1;
}

 if( incomingByte == 'a' && doOnce == 0)
{
pos_t = pos_t+10;
tilt.write(pos_t); 
doOnce = 1;
}

 if( incomingByte == 'z' && doOnce == 0)
{
tilt.write(pos_t-10); 
pos_t = pos_t-10;
doOnce = 1;
}


}
