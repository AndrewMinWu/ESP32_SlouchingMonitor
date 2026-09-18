#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_VL53L0X.h"

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup() {
    Serial.begin(115200);
    
    // Delay for the serial monitor
    delay(2000); 
    
    Serial.println("Booting");
    Serial.println("Initializing VL53L0X on SDA=0, SCL=1...");

    // SDA and SCL GPIO pins on ESP32-C3
    Wire.begin(0, 1); 

    if (!lox.begin()) {
        Serial.println("Failed to boot VL53L0X. Check wiring!");
        while (1) { 
            delay(10); 
        } 
    }
    
    Serial.println("VL53L0X Ready!");
}

void loop() {
    VL53L0X_RangingMeasurementData_t measure;
    
    lox.rangingTest(&measure, false); 

    if (measure.RangeStatus != 4) {  
        Serial.print("Distance: ");
        Serial.print(measure.RangeMilliMeter);
        Serial.println(" mm");
    } else {
        Serial.println("Out of range");
    }
    
    delay(500); 
}