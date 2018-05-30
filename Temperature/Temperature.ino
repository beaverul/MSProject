#include <dht.h>
#include <Firebase.h>
#include <FirebaseArduino.h>
#include <FirebaseCloudMessaging.h>
#include <FirebaseError.h>
#include <FirebaseHttpClient.h>
#include <FirebaseObject.h>
#define DHT11_PIN 13

#include  <ESP8266WiFi.h>

dht DHT;


#define FIREBASE_HOST "smartalarmclock-5ad4f.firebaseio.com"
#define WIFI_SSID "Smart" // Change the name of your WIFI
#define WIFI_PASSWORD "puiuchu96" // Change the password of your WIFI


void setup() {
  
  Serial.begin(9600);
   WiFi.begin (WIFI_SSID, WIFI_PASSWORD);
   while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  Firebase.begin(FIREBASE_HOST);
}

void tempSens()
{
  DHT.read11(DHT11_PIN);
  float temperature = DHT.temperature;
  delay(200);
  Firebase.setFloat("Temp",temperature);
  while(WiFi.status() != WL_CONNECTED){
    WiFi.begin (WIFI_SSID, WIFI_PASSWORD);
    delay(500);
  }
  delay(3000);
 
}

void loop() {
         
     tempSens();   

}

