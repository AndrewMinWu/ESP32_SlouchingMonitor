# Laptop Slouching Monitor

![KiCad](https://img.shields.io/badge/KiCad-FFFFFF?style=flat-square&logo=kicad&logoColor=blue)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Fusion 360](https://img.shields.io/badge/Fusion_360-0696D7?style=flat-square&logo=autodesk&logoColor=white)
![PlatformIO](https://img.shields.io/badge/PlatformIO-FE7A16?style=flat-square&logo=platformio&logoColor=white)
![VSCode](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)


<img width="3024" height="2430" alt="IMG_2121" src="https://github.com/user-attachments/assets/ffc90278-380d-4e48-b558-e46841144675" />


## Repository Structure

```text
├── hardware/          # Schematic, PCB, and gerbers
├── firmware/          # PlatformIO C++ code, and Python script
└── docs/              # Datasheets
```

## Purpose & Motivation:
Spending long hours working at a computer, I noticed my posture deteriorating as I constantly leaned closer to the monitor. Over time, this habit leads to back pain and eye strain (probably why my eyesight is so bad). Therefore, to prevent future issues and to force myself to build better sitting habits, I designed a PCB using an ESP32 and a Time-of-Flight (ToF) sensor to accurately monitor my distance from the screen and trigger a desktop popup whenever I slouch.

## Design

### Component List (BOM)
1. ESP32-C3-WROOM-02 ([Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3-wroom-02_datasheet_en.pdf))
2. AP2112K-3.3 LDO Voltage Regulator ([Datasheet](https://www.diodes.com/assets/Datasheets/AP2112.pdf))
3. GCT USB4105-GF-A USB-C Receptacle 16P SMD RA ([Datasheet](https://gct.co/files/drawings/usb4105.pdf))
4. VL53L0X Time-of-Flight Distance Sensor ([Datasheet](https://www.st.com/resource/en/datasheet/vl53l0x.pdf))
5. Passives & Miscellaneous Hardware:
   - Capacitors (0805, Ceramic)
   - Resistors (0805)
   - Push Buttons

### PCB, Schematic, Finished Board
The Schematic and PCB were designed in KiCad.

<img src="https://github.com/user-attachments/assets/d784b8aa-4701-43a2-b5ee-a8478c8316fc" alt="Schematic" width="100%"/>

<table width="100%">
  <tr>
    <td width="50%"><img src="https://github.com/user-attachments/assets/653912a7-6752-427d-9976-6d984a096c5b" alt="PCB Layout" width="100%"/></td>
    <td width="50%"><img src="https://github.com/user-attachments/assets/21de1d4f-35c5-4df6-b0a6-0c4cd98a5535" alt="3D Render" width="100%"/></td>

  </tr>
</table>


### Firmware & Software
* **Language & Framework:** C++ (Arduino IDE) and Python, done using VSCode with PlatformIO
* **I2C Configuration:** GPIO 0 (SDA), GPIO 1 (SCL)
* **Desktop Application:** Python script using pyserial and tkinter for the popup alerts

## Assembly & Demonstration

**Short Demo**  
<video src="https://github.com/user-attachments/assets/37af02e7-89a8-4d62-8e1a-ba28e2ae51d5" width="100%" controls></video>

* **Assembly:** Hand-soldered all parts and tested the board with a multimeter (checking continuity with the implemented testpoints) before flashing firmware.

## Active Development



* **Enclosure:** 3D printing a case to mount the PCB to the top of my monitor, using Fusion 360





