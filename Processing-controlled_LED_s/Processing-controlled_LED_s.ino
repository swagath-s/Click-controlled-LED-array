int led1 = 2;
int led2 = 3;
int led3 = 4;
int led4 = 5;
int led5 = 6;
int led6 = 7;

void setup() {
Serial.begin(9600);
pinMode(led1, OUTPUT);
pinMode(led2, OUTPUT);
pinMode(led3, OUTPUT);
pinMode(led4, OUTPUT);
pinMode(led5, OUTPUT);
pinMode(led6, OUTPUT);
}

int writePin = 0;

void loop() {
char incoming;
if (Serial.available()){
  incoming = Serial.read();
  int inPin = int(incoming)+1;
  if (writePin == inPin) 
    digitalWrite(writePin, !digitalRead(writePin));        //toggling the pin
  else {
  writePin = inPin;
  digitalWrite(writePin, HIGH);
  delay(25);
  }
}
}


