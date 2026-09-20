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
TIME_LIMIT = 5  # Slouch duration in seconds before alert

# Connect to the ESP32
ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
ser.dtr = True
ser.rts = True

slouch_start = None

print(f"Listening on {COM_PORT}...")

while True:
    if ser.in_waiting > 0:
        # Read and clean incoming line from ESP32
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        
        if "Distance:" in line:
            try:
                # Extract integer distance reading
                distance = int(line.split()[1])
            except (IndexError, ValueError):
                continue

            print(f"Distance: {distance} mm")

            # Posture check logic
            if distance < DISTANCE_LIMIT:
                if slouch_start is None:
                    slouch_start = time.time()  # Start slouch timer
                elif time.time() - slouch_start >= TIME_LIMIT:
                    # Trigger popup window on top of all screens
                    root.attributes('-topmost', True)
                    messagebox.showwarning("Posture Alert", "You are sitting too close. Sit back!")
                    slouch_start = None  # Reset timer after closing alert
            else:
                slouch_start = None  # Reset timer when posture is good