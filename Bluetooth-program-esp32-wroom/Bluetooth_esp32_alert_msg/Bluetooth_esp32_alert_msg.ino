#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  pinMode(12,INPUT);
  
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
}

void loop() {
  if (digitalRead(12) == HIGH) {
    const char *myString = "accident location: Dawson St, Uttar Pradesh, India \n live location: https://www.google.com/maps/d/viewer?ie=UTF8&t=h&oe=UTF8&msa=0&mid=1QSDHFff59t5WxziPBBisLBGW9Kc&ll=53.3412506183315%2C-6.2581974252673245&z=21 \n time of accident:  05:17:49.496093";
    for(int x =0;x<strlen(myString);x++){
    uint8_t myByte = static_cast<uint8_t>(myString[x]); // Convert the first character of the string to uint8_t

    SerialBT.write(myByte);
    }
  }
  delay(20);
}
