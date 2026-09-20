import serial
import time
import tkinter as tk
from tkinter import messagebox

# Initialize hidden Tkinter root window for popups
root = tk.Tk()
root.withdraw()

# Configuration settings
COM_PORT = 'COM3'
BAUD_RATE = 115200
DISTANCE_LIMIT = 375  # Distance threshold in mm
TIME_LIMIT = 5       # Slouch duration in seconds before alert

def connect_serial():
    while True:
        try:
            ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
            ser.dtr = True
            ser.rts = True
            print(f"Connected to {COM_PORT}...")
            return ser
        except Exception:
            print(f"Waiting for {COM_PORT}...")
            time.sleep(1)

ser = connect_serial()
slouch_start = None

while True:
    try:
        if ser.in_waiting > 0:
            # Read line from ESP32
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            
            if "Distance:" in line:
                try:
                    distance = int(line.split()[1])
                except (IndexError, ValueError):
                    continue

                # Ignore out of range readings (8191 mm)
                if distance > 2000:
                    continue

                print(f"Distance: {distance} mm")

                # Posture check logic
                if distance < DISTANCE_LIMIT:
                    if slouch_start is None:
                        slouch_start = time.time()  # Start slouch timer
                    elif time.time() - slouch_start >= TIME_LIMIT:
                        root.attributes('-topmost', True)
                        messagebox.showwarning("Posture Alert", "You are sitting too close. Sit back!")
                        slouch_start = None  # Reset timer
                else:
                    slouch_start = None  # Reset timer on good posture

    except (serial.SerialException, OSError):
        # Handle USB disconnects without crashing
        print("USB connection hiccuped. Reconnecting...")
        slouch_start = None
        time.sleep(1)
        ser = connect_serial()