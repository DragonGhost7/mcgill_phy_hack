//#include <WiFi.h>
#include <ESP8266WiFi.h>
#include <DHTesp.h>

char* ssid = "McGill Physics Hackathon";
const char* password =  "McGillPhysHack18";
const uint16_t port = 6666;
const char * host = "172.16.90.69";
 DHTesp dht;
 int id = 0;
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
    WiFiClient client;
 
    if (!client.connect(host, port)) {
        Serial.println("Connection to host failed");
 
        delay(1000);
        return;
    }
 if(id >= 31){
    client.stop();
 }
TempAndHumidity lastValues = dht.getTempAndHumidity();
String data = String(id) + ","+ String(lastValues.temperature,0) +","+ String(lastValues.humidity,0) + "\n";
  client.println(data);
  id = id + 1;
  
  delay(1000);
 
    
 
    
}
