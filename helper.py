import time
import keyboard
import tkinter as tk
from threading import Thread, Lock
from PIL import ImageGrab, Image
import pytesseract
import pyautogui
import sys
import os
import json
import itertools
import numpy as np
import cv2

# Lock for shared variables
running_lock = Lock()
f9_running_lock = Lock()

# Path for settings file
SETTINGS_FILE = "settings.json"

# Default hotkeys
default_hotkeys = {
    "super_fist": "f",
    "mission_tp": "n",
    "aim_teleport": "/",
    "start_mission": "f4"
}

# Error handling for tesseract path
if getattr(sys, 'frozen', False):
    # If running as a bundled executable, get the Tesseract path from the bundled files
    tesseract_path = os.path.join(sys._MEIPASS, 'tesseract.exe')
    tessdata_prefix = os.path.join(sys._MEIPASS, 'tessdata')
else:
    # If running as a normal script, use the system installation of Tesseract
    tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    tessdata_prefix = r"C:\Program Files\Tesseract-OCR\tessdata"
    if not os.path.exists(tesseract_path):
        raise FileNotFoundError(f"Tesseract executable not found at {tesseract_path}")

# Set the environment variable for Tesseract
os.environ['TESSDATA_PREFIX'] = tessdata_prefix

# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Function to load or set up hotkeys
def load_or_setup_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)  # Load existing settings
    else:
        # Ask user for hotkeys
        hotkeys = {}
        for action, default in default_hotkeys.items():
            key = input(f"Enter hotkey for {action.replace('_', ' ').title()} (Default: {default}): ").strip()
            hotkeys[action] = key if key else default  # Use input if provided, else use default
        
        # Save settings
        with open(SETTINGS_FILE, "w") as file:
            json.dump(hotkeys, file, indent=4)
        
        return hotkeys  # Return the new hotkeys

# Load the settings
hotkeys = load_or_setup_settings()

# Global state
running = False
start_mission_running = False
f9_running = False
result_search_running = False  # For F8 toggle

# Function to update the GUI state
def update_gui_state():
    root.after(0, _update_gui_state)

def _update_gui_state():
    state_label.config(text=f"Colossi Restart (F12): {'ON' if running else 'OFF'}", fg="green" if running else "red")
    start_mission_label.config(text=f"Restart Field Mission (F10): {'ON' if start_mission_running else 'OFF'}", fg="green" if start_mission_running else "red")
    f9_label.config(text=f"Infiltration Operation Bot (F9): {'ON' if f9_running else 'OFF'}", fg="green" if f9_running else "red")
    result_search_label.config(text=f"Auto Outposts (F8): {'ON' if result_search_running else 'OFF'}", fg="green" if result_search_running else "red")

# Rainbow effect for GUI labels
def rainbow_text():
    colors = itertools.cycle(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    while True:
        for color in colors:
            if running:
                state_label.config(fg=color)
            if start_mission_running:
                start_mission_label.config(fg=color)
            if f9_running:
                f9_label.config(fg=color)
            if result_search_running:
                result_search_label.config(fg=color)
            time.sleep(0.1)

# Extract text from a specific screen region
def extract_text_from_screen(region):
    try:
        screenshot = ImageGrab.grab(bbox=region)
        img = np.array(screenshot)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        pil_img = Image.fromarray(binary_image)
        return pytesseract.image_to_string(pil_img, config='--psm 6').strip()
    except Exception as e:
        return ""

# Automation loop for "Colossi Restart"
def automation_loop():
    try:
        while running:
            update_gui_state()
            region = (1623, 536, 1770, 566)
            detected_text = extract_text_from_screen(region)
            if "Restart Mission" in detected_text:
                pyautogui.keyDown('r')
            else:
                pyautogui.keyUp('r')

            pyautogui.press(hotkeys["super_fist"])
            time.sleep(3)
    except Exception as e:
        pass

# Start mission loop
def start_mission_loop():
    while start_mission_running:
        region = (1052, 632, 1181, 660)
        detected_text = extract_text_from_screen(region)
        if "Start Mission" in detected_text:
            pyautogui.keyDown('e')
        else:
            pyautogui.keyUp('e')
        time.sleep(0.1)

# F9 automation loop
def f9_automation_loop():
    last_n_time = time.time()  # Track time for mission_tp press
    last_slash_time = time.time()  # Track time for aim_teleport press
    last_f_time = time.time()  # Track time for super_fist press

    while f9_running:
        update_gui_state()  # Update GUI state if f9 is running
        
        # Region where "Restart Mission" text is detected
        region = (1623, 536, 1770, 566)
        detected_text = extract_text_from_screen(region)

        # Check for the text and trigger restart mission action
        if "Restart Mission" in detected_text:
            pyautogui.keyDown('r')  # Hold down the 'r' key
        else:
            pyautogui.keyUp('r')  # Release the 'r' key

        # Ensure aim_teleport hotkey is pressed down for a short period (every 5 seconds)
        if time.time() - last_slash_time >= 5:
            pyautogui.keyDown(hotkeys["aim_teleport"])  # Press and hold the aim_teleport key
            time.sleep(0.1)  # Hold the key for 0.1 seconds
            pyautogui.keyUp(hotkeys["aim_teleport"])  # Release the aim_teleport key
            last_slash_time = time.time()

        # Ensure mission_tp hotkey is pressed down for a short period (every 12 seconds)
        if time.time() - last_n_time >= 12:
            pyautogui.keyDown(hotkeys["mission_tp"])  # Press and hold the mission_tp key
            time.sleep(0.1)  # Hold the key for 0.1 seconds
            pyautogui.keyUp(hotkeys["mission_tp"])  # Release the mission_tp key
            last_n_time = time.time()

        # Ensure super_fist hotkey is pressed every 20 seconds
        if time.time() - last_f_time >= 20:
            pyautogui.press(hotkeys["super_fist"])  # Simulate a quick press of super_fist
            last_f_time = time.time()

        time.sleep(0.1)  # Sleep briefly before checking again

# Result search loop
def result_search_loop():
    while result_search_running:
        # Define the region where "Result" will be searched for
        region = (1500, 868, 1759, 957)
        
        # Extract the text from the screen within the region
        detected_text = extract_text_from_screen(region)
        
        # Check if the word "Result" is found
        if "Result" in detected_text:
            pyautogui.keyDown(hotkeys["start_mission"])  # Press F4 if "Result" is found
            time.sleep(0.1)  # Hold the key for 0.1 seconds
            pyautogui.keyUp(hotkeys["start_mission"])  # Press F4 if "Result" is found
            time.sleep(0.5)  # Small delay to avoid spamming F4 too quickly

        time.sleep(0.1)  # Sleep briefly before checking again

# Hotkey functions to toggle automation
def toggle_running():
    global running
    running = not running
    update_gui_state()
    if running:
        Thread(target=automation_loop, daemon=True).start()

def toggle_start_mission():
    global start_mission_running
    start_mission_running = not start_mission_running
    update_gui_state()
    if start_mission_running:
        Thread(target=start_mission_loop, daemon=True).start()

def toggle_f9_running():
    global f9_running
    f9_running = not f9_running
    update_gui_state()
    if f9_running:
        Thread(target=f9_automation_loop, daemon=True).start()

def toggle_result_search():
    global result_search_running
    result_search_running = not result_search_running
    update_gui_state()
    if result_search_running:
        Thread(target=result_search_loop, daemon=True).start()

# Toggle GUI visibility (draggable cross behavior)
def toggle_gui_visibility():
    if root.state() == 'normal':
        root.withdraw()  # Hide the window
    else:
        root.deiconify()  # Show the window

# Tkinter window setup
root = tk.Tk()
root.title("Mission Helper")
root.attributes("-topmost", 1)
root.configure(bg="#2e2e2e")
root.overrideredirect(True)
root.wm_attributes("-transparentcolor", "#2e2e2e")

# Window dimensions and position
window_width, window_height = 400, 200
screen_width, screen_height = 1920, 1080
x_position, y_position = screen_width - window_width, 0
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

# Labels for GUI
state_label = tk.Label(root, text="Colossi Restart (F12): OFF", font=("Bahnschrift", 10), fg="red", bg="#2e2e2e")
state_label.pack(pady=10)

start_mission_label = tk.Label(root, text="Restart Field Mission (F10): OFF", font=("Bahnschrift", 10), fg="red", bg="#2e2e2e")
start_mission_label.pack(pady=10)

f9_label = tk.Label(root, text="Infiltration Operation Bot (F9): OFF", font=("Bahnschrift", 10), fg="red", bg="#2e2e2e")
f9_label.pack(pady=10)

result_search_label = tk.Label(root, text="Auto Outposts (F8): OFF", font=("Bahnschrift", 10), fg="red", bg="#2e2e2e")
result_search_label.pack(pady=10)

drag_label = tk.Label(root, text="+", font=("Bahnschrift", 12), fg="white", bg="#2e2e2e")
drag_label.place(x=0, y=0)
drag_label.bind('<B1-Motion>', lambda event: root.geometry(f'+{event.x_root}+{event.y_root}'))

# Threads for the rainbow effect and other functions
Thread(target=rainbow_text, daemon=True).start()

# Adding hotkey bindings
keyboard.add_hotkey('f12', toggle_running)  # Toggle the "Colossi Restart" state
keyboard.add_hotkey('f10', toggle_start_mission)  # Toggle the "Restart Field Mission" state
keyboard.add_hotkey('f9', toggle_f9_running)  # Toggle the "Infiltration Operation Bot" state
keyboard.add_hotkey('f8', toggle_result_search)  # Toggle the "Search for 'Result'" state
keyboard.add_hotkey('`', toggle_gui_visibility)  # Toggle the visibility of the GUI (backtick key)

root.mainloop()
