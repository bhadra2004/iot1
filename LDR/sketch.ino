
#define LDRPIN 34

void setup() {
  Serial.begin(115200);
}

void loop() {
  int lightValue = analogRead(LDRPIN);

  Serial.print("Light Intensity: ");
  Serial.println(lightValue);

  delay(1000);
}
