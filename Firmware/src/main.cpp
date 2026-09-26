#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_VL53L0X.h"

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup() {
    Serial.begin(115200);
    
    // Initializing i2c pins
    Wire.begin(0, 1); 

    // Halt execution on sensor if initialization fails
    if (!lox.begin()) {
        while (1); 
    }
}

void loop() {
    VL53L0X_RangingMeasurementData_t measure;
    
    // Sensor measurement
    lox.rangingTest(&measure, false); 

    // Status 4 indicates out of range; filter valid data
    if (measure.RangeStatus != 4) { 
        Serial.print("Distance: ");
        Serial.print(measure.RangeMilliMeter);
        Serial.println(" mm");
    }
    
    delay(500); 
}