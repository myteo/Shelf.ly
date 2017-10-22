/*************************************************
*** PIR Motion Sensor Servo Motor Mount ***
*************************************************/

// Servor motor
#include <Servo.h>
Servo camServo; // servo motor camera is mounted on
int currentPIRposition = 0; // set current angle of servo

// LED status lights
int LEDpin[] = {9, 10, 11, 12}; // LED pin numbers
int currentLEDpin = 9; // the current LED pin; begin with the first in the sequence above

// PIR sensors
int PIRpin[] = {2, 3, 4, 5}; // PIR pin numbers
int currentPIRpin = 2; // the current PIR pin; begin with the first in the sequence above
int PIRprevState[] = {1, 1, 1, 1}; // the previous state of the PIR (0 = LOW, 1 = HIGH)
int PIRposition[] = {157, 104.6, 52.3, 0}; // assign angles for servo motor (0-157 distributed equally between 5 PIR sensors)
boolean PIRstatus; // Set status of PIR sensor as either true or false

// Ultrasonic Sensor
#define trigPin 13
#define echoPin 8

// Ultrasonic Sensor LED Lights
#define Green 6
#define Red A1

///// SETUP //////////////////////////////////////
void setup()  {

  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(Green, OUTPUT);
  pinMode(Red, OUTPUT);
  camServo.attach(7); // assign servo pin

  for (int p = 0; p < 4; p++)  { // set all PIR sensors as INPUTS
    pinMode(PIRpin[p], INPUT);
  } // end 'p' for

  for (int l = 0; l < 4; l++)  { // set all LEDs as OUTPUTS
    pinMode(LEDpin[l], OUTPUT);
  } // end 'l' for

  /////// CALIBRATE PIR SENSORS ///////
  Serial.print("Calibrating PIR Sensors ");
  for (int c = 0; c < 15; c++) { // calibrate PIR sensors for 15 seconds (change from 10-60 sec depending on your sensors)
    Serial.print(".");
    delay(1000); // wait 1 second
  } // end calibration for
  Serial.println("PIR Sensors Ready");

  camServo.write(78.5); // move the servo to the center position to begin

} // end setup



///// MAIN LOOP //////////////////////////////////
void loop()  {
  long duration, distance;
  
  for (int PIR = 0; PIR < 4; PIR++) { // start this loop for each PIR sensor
    currentPIRpin = PIRpin[PIR]; // set current PIR pin to current number in 'for' loop
    currentLEDpin = LEDpin[PIR]; // set current LED pin to current number in 'for' loop
    PIRstatus = digitalRead(currentPIRpin);

    if (PIRstatus == HIGH) { // if motion is detected on current PIR sensor
      digitalWrite(currentLEDpin, HIGH); // turn corresponding LED on
      if (PIRprevState[PIR] == 0) { // if PIR sensor's previous state is LOW
        if (currentPIRposition != currentPIRpin && PIRprevState[PIR] == 0) { // if high PIR is different than current position PIR then move to new position
          camServo.write(PIRposition[PIR]);
          //Serial.print("Current angle : ");
          //Serial.println(PIRposition[PIR]);
          delay(50);
          currentPIRposition = currentPIRpin; // reset current PIR position to active [PIR] pin
          PIRprevState[PIR] = 1; // set previous PIR state to HIGH
        }
        PIRprevState[PIR] = 1; // set previous PIR state to HIGH if the current position is the same as the current PIR pin
      } // end PIRprevState if
    } // end PIRstatus if

    else  { //
      digitalWrite(currentLEDpin, LOW);  //the led visualizes the sensors output pin state
      PIRprevState[PIR] = 0;   // set previous PIR state to LOW
    } // end else

  } // end [PIR] for loop
  
  digitalWrite(trigPin, LOW);  // Added this line
  delayMicroseconds(2); // Added this line
  digitalWrite(trigPin, HIGH);
  //  delayMicroseconds(1000); - Removed this line
  delayMicroseconds(10); // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration / 2) / 29.1;
  if (distance <= 8) {  // This is where the LED On/Off happens
    digitalWrite(Green, HIGH); // When the Green condition is met, the Red LED should turn off
    digitalWrite(Red, LOW);
  } else {
    digitalWrite(Green, LOW);
    digitalWrite(Red, HIGH);
    Serial.println("LOW");
  }

  if (distance >= 200 || distance <= 0) {
    //Serial.println("Out of range");
  }
  else {
    //Serial.print(distance);
    //Serial.println(" cm");
  }
} // end main loop
