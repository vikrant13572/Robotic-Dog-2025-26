#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;

void setup() {
  servo1.attach(3);  // attach servo to pin 3
  servo2.attach(5);  // attach servo to pin 5
  servo3.attach(6);  // attach servo to pin 6

  // Move all servos to 90 degrees
  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
}

void loop() {
  // nothing needed here
}