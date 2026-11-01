
#include <DHT.h>

#define DHTPIN 15
#define DHTTYPE DHT22
#define LDRPIN 34

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  Serial.println("================================");
  Serial.println(" ENVIRONMENT MONITORING SYSTEM ");
  Serial.println("================================");
}

void loop() {
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  int light = analogRead(LDRPIN);

  if (isnan(temp) || isnan(hum)) {
    Serial.println("Error reading DHT22!");
    delay(2000);
    return;
  }

  Serial.println();
  Serial.println("------ SENSOR READINGS ------");

  Serial.print("Temperature : ");
  Serial.print(temp);
  Serial.println(" C");

  Serial.print("Humidity    : ");
  Serial.print(hum);
  Serial.println(" %");

  Serial.print("Light Value : ");
  Serial.println(light);

  if (light > 2000) {
    Serial.println("Light Status: DARK");
  } else {
    Serial.println("Light Status: BRIGHT");
  }

  Serial.println("------ ALERT STATUS ------");

  if (temp < 30 && light > 2000) {
    Serial.println("ALERT: LOW TEMPERATURE AND DARK!");
  } else {
    Serial.println("STATUS: NORMAL");
  }

  Serial.println("-----------------------------");

  delay(2000);
}
