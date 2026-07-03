#include <Servo.h>

Servo srf1, srf2,srf3, slf1, slf2, slf3, srb1, srb2, srb3, slb1, slb2, slb3;

float th1, th2, th3;
float ag1, ag2, ag3;


float theta1[3] = {0, 37.4804, -69.417}; //A
float theta2[3] = {0, 45.9798, -84.664};  //B
float theta3[3] = {6.3933, 46.7308, -85.997};  //C
float theta4[3] = {5.7493, 38.2589, -70.8229};  //D

float angle1[3] = {6.3933, 46.7308, -85.997};  //D
float angle2[3] = {5.7493, 38.2589, -70.8229};  //C

float angle3[3] = {0, 45.9798, -84.664};  //A
float angle4[3] = {0, 37.4804, -69.417};   //B
int steps = 60;

void cubicMove(float aL[3], float bL[3],
               float aR[3], float bR[3],
               float t, int steps, int delay_ms) {

  for (int j = 0; j <= steps; j++) {

    float i = (t / steps) * j;

    // ---- LEFT LEG (th) ----
    th1 = aL[0] + (3 * (bL[0] - aL[0]) / (t * t)) * i * i
                    - (2 * (bL[0] - aL[0]) / (t * t * t)) * i * i * i;

    th2 = aL[1] + (3 * (bL[1] - aL[1]) / (t * t)) * i * i
                    - (2 * (bL[1] - aL[1]) / (t * t * t)) * i * i * i;

    th3 = aL[2] + (3 * (bL[2] - aL[2]) / (t * t)) * i * i
                    - (2 * (bL[2] - aL[2]) / (t * t * t)) * i * i * i;

    // ---- RIGHT LEG (ag) ----
    ag1 = aR[0] + (3 * (bR[0] - aR[0]) / (t * t)) * i * i
                    - (2 * (bR[0] - aR[0]) / (t * t * t)) * i * i * i;

    ag2 = aR[1] + (3 * (bR[1] - aR[1]) / (t * t)) * i * i
                    - (2 * (bR[1] - aR[1]) / (t * t * t)) * i * i * i;

    ag3 = aR[2] + (3 * (bR[2] - aR[2]) / (t * t)) * i * i
                    - (2 * (bR[2] - aR[2]) / (t * t * t)) * i * i * i;


/// ================= LEFT SIDE (FORWARD) =================

// FRONT LEFT
slf1.write(105 + th1);
slf2.write(90 + th2);
slf3.write(th3 + 225);

// BACK LEFT
slb1.write(90);
slb2.write(12 + th2);
slb3.write(th3 + 215);


// ================= RIGHT SIDE (BACKWARD) =================

// FRONT RIGHT
srf1.write(105 + ag1);
srf2.write(65 + ag2);
srf3.write(ag3 + 78);

// BACK RIGHT
srb1.write(90);
srb2.write(105 + ag2);
srb3.write(ag3 + 125);

    delay(delay_ms);
  }
}


void setup() {
  Serial.begin(9600);

  slf1.attach(2);
  slf2.attach(3);
  slf3.attach(4);

  srb1.attach(5);
  srb2.attach(6);
  srb3.attach(7);

  slb1.attach(9);   
  slb2.attach(8);
  slb3.attach(10);

  srf1.attach(11);
  srf2.attach(12);
  srf3.attach(13);
}



void loop() {

  cubicMove(theta1, theta2, angle1, angle2, 1.5, steps, 8);
  cubicMove(theta2, theta3, angle2, angle3, 1.5, steps, 8);
  cubicMove(theta3, theta4, angle3, angle4, 1.5, steps, 8);
  cubicMove(theta4, theta1, angle4, angle1, 1.5, steps, 8);

}