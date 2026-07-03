#include <Servo.h>

Servo srf1, srf2, slf1, slf2,srb1, srb2, slb1, slb2;

float th1, th2, th3;
float ag1, ag2, ag3;


float theta1[3] = {0, 37.4804, -69.417};
float theta2[3] = {0, 45.9798, -84.664};
float theta3[3] = {0, 31.6837, -81.523};
float theta4[3] = {0, 24.3135, -66.04};

float angle1[3] = {0, -24.9512, 118.59};
float angle2[3] = {0, -23.06, 128.11};
float angle3[3] = {0, -64.177, 139.10};
float angle4[3] = {0, -59.93, 128.12};

int steps = 50;

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

  slf1.write(th2);
  slf2.write(th3 +210);
  // Serial.println(90+th2);
  Serial.println(th3+180);

  srb1.write(180 + ag2);
  srb2.write(ag3);  

  // Serial.println(ag3);


  srf1.write(180 + th2);
  srf2.write(th3);

  slb1.write(90 + ag2);
  slb2.write(ag3 - 90);

    delay(delay_ms);
  }
}


void setup() {
  Serial.begin(9600);

  slf1.attach(8);
  slf2.attach(9);
  srb1.attach(10);
  srb2.attach(11);
  slb1.attach(2);
  slb2.attach(3);
  srf1.attach(4);
  srf2.attach(5);
}

// void cubicMove_R(float a[3], float b[3], float t, int steps, int delay_ms) {

//   for (int j = 0; j <= steps; j++) {

//     float i = (t / steps) * j;

//     ag1 = a[0] + (3 * (b[0] - a[0]) / (t * t)) * i * i
//                       - (2 * (b[0] - a[0]) / (t * t * t)) * i * i * i;

//     ag2 = a[1] + (3 * (b[1] - a[1]) / (t * t)) * i * i
//                       - (2 * (b[1] - a[1]) / (t * t * t)) * i * i * i;

//     ag3 = a[2] + (3 * (b[2] - a[2]) / (t * t)) * i * i
//                       - (2 * (b[2] - a[2]) / (t * t * t)) * i * i * i;

//     // s1.write(th1);

//     applyServos();



//   //  Serial.println(180+ag2);
//   // //  Serial.println(180+th2);

//     delay(delay_ms);
//   }
// }

void loop() {

  cubicMove(theta1, theta2, angle1, angle2, 1.0, steps, 8);
  cubicMove(theta2, theta3, angle2, angle3, 1.0, steps, 8);
  cubicMove(theta3, theta4, angle3, angle4, 1.0, steps, 8);
  cubicMove(theta4, theta1, angle4, angle1, 1.0, steps, 8);

}

