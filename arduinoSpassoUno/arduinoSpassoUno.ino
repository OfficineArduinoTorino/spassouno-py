/*
  (S)passoUno

  Hardware:
  https://123d.circuits.io/circuits/1926939-spassunouno-kids-interface

  8    Nuovo fotogramma             SPACE_KEY
  10   Diminuisci velocità          DOWN_KEY
  9    Aumenta velocità             UP_KEY
  11   Nuova storia                 SPACE_KEY
  12   Cancella ultimo fotogramma   X_KEY
  6 Buzzer

*/

#include "Keyboard.h"

int newFrame = 8;
int speedUp = 9;
int speedDown = 10;
int newStory = 11;
int deleteLastFrame = 12;


void setup() {

  Serial.begin(9600);

  pinMode(newFrame, INPUT);
  pinMode(speedUp, INPUT);
  pinMode(speedDown, INPUT);
  pinMode(newStory, INPUT);
  pinMode(deleteLastFrame, INPUT);

  Keyboard.begin();
}


void loop() {

  int stateNewFrame = digitalRead(newFrame);
  int stateSpeedUp = digitalRead(speedUp);
  int stateSpeedDown = digitalRead(speedDown);
  int stateNewStory = digitalRead(newStory);
  int stateDeleteLastFrame = digitalRead(deleteLastFrame);

  Serial.println(stateSpeedUp);


  if (stateNewFrame == 1) {
    tone(6, 20);
    #define SPACE (0x20)
    Keyboard.press(SPACE);
    Keyboard.release(SPACE);
    delay(10000);
    noTone(6);
  }
  else if (stateSpeedUp == 1) {
    tone(6, 200);
    Keyboard.press(KEY_UP_ARROW);
    delay(200);
    Keyboard.release(KEY_UP_ARROW);
    noTone(6);
  }

  else if (stateSpeedDown == 1) {
    tone(6, 200);
    Keyboard.press(KEY_UP_ARROW);
    delay(200);
    Keyboard.release(KEY_UP_ARROW);
    delay(200);
    noTone(6);
  }
  else if (stateNewStory == 1) {
    tone(6, 20);
    Keyboard.print("d");
    delay(500);
    noTone(6);
    delay(10000);
    
  }
  else if (stateDeleteLastFrame == 1) {
    tone(6, 20);
    Keyboard.print("x");
    delay(500);
    noTone(6);
    delay(3000);
    
  }

  delay(10);
}



