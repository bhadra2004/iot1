
#define PIRPIN 13

void setup() {
  Serial.begin(115200);
  pinMode(PIRPIN, INPUT);

  Serial.println("============================");
  Serial.println(" PIR MOTION DETECTION SYSTEM ");
  Serial.println("============================");
}

void loop() {
  int motion = digitalRead(PIRPIN);

  Serial.println("------ MOTION STATUS ------");

  if (motion == HIGH) {
    Serial.println("Motion Detected!");
  } else {
    Serial.println("No Motion Detected");
  }

  Serial.println("---------------------------");

  delay(1000);
}
