import serial
import time
import tkinter as tk
from tkinter import messagebox

# Hide main root window
root = tk.Tk()
root.withdraw()

COM_PORT = 'COM3'
BAUD_RATE = 115200
DISTANCE_LIMIT = 375 
TIME_LIMIT = 5       

# Initialize serial connection
while True:
    try:
        ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
        break
    except Exception:
        time.sleep(1)

slouch_start = None

# Main data processing loop
while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            
            if "Distance:" in line:
                try:
                    # Extract integer distance value from string
                    distance = int(line.split()[1])
                except (IndexError, ValueError):
                    continue

                # Filter invalid sensor spikes
                if distance > 2000:
                    continue

                # Check posture threshold
                if distance < DISTANCE_LIMIT:
                    
                    # Initialize timestamp on first detection
                    if slouch_start is None:
                        slouch_start = time.time()  
                    
                    # Display warning upon exceeding time limit
                    elif time.time() - slouch_start >= TIME_LIMIT:
                        root.attributes('-topmost', True)
                        messagebox.showwarning("Posture Alert", "Distance threshold exceeded.")
                        slouch_start = None  
                
                else:
                    # Clear timestamp on proper posture
                    slouch_start = None  

    except Exception:
        # Reset state on connection drop
        slouch_start = None
        time.sleep(1)