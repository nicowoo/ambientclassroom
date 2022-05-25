#include <FastLED.h>

#define LED_PIN     5
#define NUM_LEDS    20

CRGB leds[NUM_LEDS];
int x;

void setup() {
 Serial.begin(9600);
 Serial.setTimeout(1);
 FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
}
void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();
 
 if (x < 3 && x > 0) {
  for (int i = 0; i <= 19; i++) {
    leds[i] = CRGB (0, 255, 0);
    FastLED.show();
    delay(40);
  }
 } else if (x >= 3) {
  for (int i = 19; i >= 0; i--) {
    leds[i] = CRGB ( 0, 0, 255);
    FastLED.show();
    delay(40);
  }
 } else if (x == 0) {
//  digitalWrite(redLED, LOW);
//  digitalWrite(blueLED, LOW);
 }
 Serial.print(x + 1);
}
