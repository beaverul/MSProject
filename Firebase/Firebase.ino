#include <BH1750.h>
#include <Firebase.h>
#include <FirebaseArduino.h>
#include <FirebaseCloudMessaging.h>
#include <FirebaseError.h>
#include <FirebaseHttpClient.h>
#include <FirebaseObject.h>
#include <Wire.h>

#include  <ESP8266WiFi.h>

#define FIREBASE_HOST "smartalarmclock-5ad4f.firebaseio.com"
#define WIFI_SSID "Hamnet" // Change the name of your WIFI
#define WIFI_PASSWORD "1234567890" // Change the password of your WIFI

BH1750 lightMeter;
void setup() {
  Serial.begin(9600);
   WiFi.begin (WIFI_SSID, WIFI_PASSWORD);
   while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  Wire.begin(5,4);
  delay(200);
  lightMeter.begin();
  Firebase.begin(FIREBASE_HOST);
  
}
int i;
void loop() {
  uint16_t lux = lightMeter.readLightLevel();
  Firebase.setFloat("Light",lux);
  while(WiFi.status() != WL_CONNECTED){
    WiFi.begin (WIFI_SSID, WIFI_PASSWORD);
    delay(500);
  }
  delay(3000);
}
