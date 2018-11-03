//#include <WiFi.h>
#include <ESP8266WiFi.h>
#include <DHTesp.h>

char* ssid = "McGill Physics Hackathon";
const char* password =  "McGillPhysHack18";
 
const uint16_t port = 7777;
const char * host = "172.16.90.69";
 DHTesp dht;
void setup()
{
 
  Serial.begin(9600);
 dht.setup(2, DHTesp::DHT11);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
 
}
 
void loop()
{
    TempAndHumidity lastValues = dht.getTempAndHumidity();
    WiFiClient client;
 
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
 
        delay(1000);
        return;
    }
 
    Serial.println("Connected to server successful!");
  String data = String(lastValues.temperature,0) + String(lastValues.humidity,0);
  client.println(data);
 
    
 
    delay(10000);
}
