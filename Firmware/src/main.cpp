#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_VL53L0X.h"

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup() {
    Serial.begin(115200);
    
    // Set up I2C pins
    Wire.begin(0, 1); 

    // Start sensor and freeze if it fails
    if (!lox.begin()) {
        while (1); 
    }
}

void loop() {
    VL53L0X_RangingMeasurementData_t measure;
    
    // Read sensor
    lox.rangingTest(&measure, false); 

    // Print distance if valid
    if (measure.RangeStatus != 4) { 
        Serial.print("Distance: ");
        Serial.print(measure.RangeMilliMeter);
        Serial.println(" mm");
    }
    
    // Wait half a second
    delay(500); 
}