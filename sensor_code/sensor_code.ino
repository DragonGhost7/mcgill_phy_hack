
#include <DHTesp.h>

//#include <dht.h>
DHTesp dht;

#define DHT11_PIN 2
void setup(){
dht.setup(DHT11_PIN, DHTesp::DHT11);
    Serial.begin(9600);
}
void loop(){
    TempAndHumidity lastValues = dht.getTempAndHumidity();
  Serial.print("Temperature = ");
  Serial.println(lastValues.temperature,0);
  Serial.print("Humidity = ");
  Serial.println(lastValues.humidity,0);
  delay(1000);
}
