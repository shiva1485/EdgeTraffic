/*
 * code version 1.4.0
 * commands to be sent to the arduino using serial communication
 * set serial port to 9600 baud rate
*/



#include "Adafruit_GFX.h"// Hardware-specific library
#include <MCUFRIEND_kbv.h>
MCUFRIEND_kbv tft;
#include"utils.h"

void setup() 
{
  Serial.begin(9600);
  Serial.println("Welcome to Traffic Controller Program");
  
  pinMode(10,OUTPUT); //for green led
  pinMode(11,OUTPUT); //for red led
  pinMode(12,OUTPUT); //for buzzer
  pinMode(13,OUTPUT); //for alert bluetooth

  // for not making wrong trigger when on
  digitalWrite(10,LOW);
  digitalWrite(11,LOW);
  digitalWrite(12,LOW);
  digitalWrite(13,LOW);

  tft.begin(0x9486); // turning on the display
  tft.setRotation(0);
  tft.fillScreen(black);

  texts("Welcome to Traffic Controller Program",normal,white,0,0);
}

void loop() 
{
  String msg = Serial.readString(); //reading the inputs from user

  if(msg == "buzzerOn"){
    cls(0,240,320,50)
    texts("Alert Accident Detected!",big,yellow,0,240);

    digitalWrite(13,HIGH); //sending the message to phone for alert
    delay(250);
    digitalWrite(13,LOW);
    
    Serial.println("red led on");
    digitalWrite(11,HIGH);
    digitalWrite(10,LOW);
    
    Serial.println("buzzer on");
    digitalWrite(12,HIGH);
    delay(2000);
    digitalWrite(12,LOW);
  }
  else if(msg == "greenOn"){
    Serial.println("green led on");
    digitalWrite(10,HIGH);
    digitalWrite(11,LOW);

    cls(0,240,320,50)
    texts("GO",big,green,158,240);
  }
  else if(msg == "redOn"){
    Serial.println("red led on");
    digitalWrite(11,HIGH);
    digitalWrite(10,LOW);

    cls(0,240,320,50)
    texts("STOP!",big,red,158,240);
  }
  else if(msg == "ledOff"){
    Serial.println("leds off");
    digitalWrite(11,LOW);
    digitalWrite(10,LOW);

    cls(0,240,320,50)
    texts("Traffic under Maintenance",big,yellow,0,240);
  }
}
