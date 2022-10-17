#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include "DHT.h"

DHT dht(5, DHT11);

const char* ssid = "komster.net-4jtTvoAx"; // CGA2121_fnwWXP9
const char* password = "ihubea737NGR841s"; // PNfCJ5xV7qY8eSA9Ag
const char* host = "192.168.0.18:5000";

//WiFiServer server(80);

//String header;
String message;
void setup_wifi(){
    WiFi.begin(ssid, password);
    Serial.print("Connecting");
    while(WiFi.status() != WL_CONNECTED){
        Serial.print(".");
        digitalWrite(2, HIGH);
        delay(250);
        digitalWrite(2, LOW);
        delay(250);
    }
    Serial.print("\nSuccessfully connected to: ");
    Serial.println(ssid);
    Serial.print("Ip address: ");
    Serial.println(WiFi.localIP());
}
void setup()
{
    Serial.begin(115200);
    dht.begin();

    delay(500);

    //WiFi.mode(WIFI_STA); //station mode - after losing connection it will try to connect to last access point
    

	pinMode(2, OUTPUT);
    //Serial.setTimeout(10);
    setup_wifi();
    digitalWrite(2, LOW);
}

void loop()
{

    
    int humidity = dht.readHumidity();
    Serial.print(humidity);
    Serial.print("RH% | ");

    int temperature = dht.readTemperature();
    Serial.print(temperature);
    Serial.println("*C");

    if(WiFi.status() != WL_CONNECTED){
        setup_wifi();
    }
    else{
        WiFiClient client;
        HTTPClient http;

        http.begin(client, "http://192.168.0.182:5000/projects/1/push");
        http.addHeader("Content-Type", "text/plain");

        int httpCode = http.POST(String(temperature));
        http.end();
    }
    delay(2500);   
}

/*void serialEvent()
{
    message = Serial.readStringUntil('\n');

    if(message == "on"){
        digitalWrite(2, HIGH);
    }
    else if (message == "off"){
        digitalWrite(2, LOW);
    }
}*/