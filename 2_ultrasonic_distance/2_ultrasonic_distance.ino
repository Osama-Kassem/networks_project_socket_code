int trig1 = 4;
int echo1 = 5;
int trig2 = 6;
int echo2 = 7;

void setup() {
  Serial.begin (9600);
  pinMode (trig1, OUTPUT);
  pinMode (echo1, INPUT);
  pinMode (trig2, OUTPUT);
  pinMode (echo2, INPUT);

//  Serial.println("Calibrate");
}

void loop() {

   digitalWrite(trig1, LOW);
   delayMicroseconds(2);
   digitalWrite(trig1, HIGH);
   delayMicroseconds(10);
   digitalWrite(trig1, LOW);
   
   long d1 = microsecondsToCentimeters(pulseIn(echo1, HIGH));

   delay(100);

   digitalWrite(trig2, LOW);
   delayMicroseconds(2);
   digitalWrite(trig2, HIGH);
   delayMicroseconds(10);
   digitalWrite(trig2, LOW);
   
   long d2 = microsecondsToCentimeters(pulseIn(echo2, HIGH));

  delay(100);

  Serial.print("0: ");
  Serial.println(d1);
  Serial.print("1: ");
  Serial.println(d2);
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
