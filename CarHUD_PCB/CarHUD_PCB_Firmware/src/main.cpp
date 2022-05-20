#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  pinMode(33, INPUT);
}

void loop() {
  delay(1000);
  Serial.println(analogRead(33));
}