import time
import keyboard
import tkinter as tk
from threading import Thread
from PIL import ImageGrab
import pytesseract
import pyautogui

# Global state
running = False
start_mission_running = False
f9_running = False

# Function to toggle the running state when F12 is pressed
def toggle_running():
    global running
    running = not running
    update_gui_state()

# Function to toggle the Start Mission functionality when F10 is pressed
def toggle_start_mission():
    global start_mission_running
    start_mission_running = not start_mission_running
    update_gui_state()

# Function to toggle the F9 state when F9 is pressed
def toggle_f9_running():
    global f9_running
    f9_running = not f9_running
    update_gui_state()

# Function to update GUI state
def update_gui_state():
    # Update status for Colossi Restart (F12)
    if running:
        state_label.config(text="Colossi Restart (F12): ON", fg="green")
    else:
        state_label.config(text="Colossi Restart (F12): OFF", fg="red")
    
    # Update status for Restart Field Mission (F10)
    if start_mission_running:
        start_mission_label.config(text="Restart Field Mission (F10): ON", fg="green")
    else:
        start_mission_label.config(text="Restart Field Mission (F10): OFF", fg="red")

    # Update status for Infiltration Operation Restart (F9)
    if f9_running:
        f9_label.config(text="Infiltration Operation Restart (F9): ON", fg="green")
    else:
        f9_label.config(text="Infiltration Operation Restart (F9): OFF", fg="red")

# Function to extract text from a specific region of the screen
def extract_text_from_screen(region):
    screenshot = ImageGrab.grab(bbox=region)
    text = pytesseract.image_to_string(screenshot, config='--psm 6')
    return text.strip()

# Function that performs the automated key presses for the first task
def automation_loop():
    last_state_update = time.time()  # Track last state update time
    r_key_held = False  # Flag to track if the R key is held down

    while True:
        if running:
            # Update state every 1 second
            if time.time() - last_state_update > 1:
                update_gui_state()
                last_state_update = time.time()

            # Check for "Restart Mission" text
            region = (1623, 536, 1770, 566)
            detected_text = extract_text_from_screen(region)
            
            if "Restart Mission" in detected_text:
                if not r_key_held:  # Only press R if it's not already held
                    pyautogui.keyDown('r')  # Hold R down
                    r_key_held = True
            else:
                if r_key_held:  # Release R if the text is no longer detected
                    pyautogui.keyUp('r')
                    r_key_held = False

            # Press 'F' after the R key logic
            pyautogui.press('f')
            time.sleep(3)  # Wait for the rest of the cycle

        time.sleep(0.1)  # Prevent excessive CPU usage

# Function that performs the automated key presses for Start Mission task
def start_mission_loop():
    key_held = False  # Flag to track if the E key is already held down

    while True:
        if start_mission_running:
            # Check for "Start Mission" text in the specific region
            region = (1052, 632, 1181, 660)
            detected_text = extract_text_from_screen(region)

            if "Start Mission" in detected_text:
                if not key_held:  # Only press E if it's not already held
                    pyautogui.keyDown('e')  # Hold E down
                    key_held = True
            else:
                if key_held:  # Release E if the text is no longer detected
                    pyautogui.keyUp('e')
                    key_held = False

        time.sleep(0.1)  # Prevent excessive CPU usage

# New function for F9 that mimics F12 functionality and presses 'n' every 7 seconds
def f9_automation_loop():
    last_state_update = time.time()  # Track last state update time
    last_n_time = time.time()  # Track the last time the 'n' key was pressed
    last_slash_time = time.time()  # Track the last time the '/' key was pressed
    last_f_key_time = time.time()  # Track the last time the F key was pressed
    r_key_held = False  # Flag to track if the R key is held down

    while True:
        if f9_running:
            # Update state every 1 second
            if time.time() - last_state_update > 1:
                update_gui_state()
                last_state_update = time.time()

            # Check for "Restart Mission" text
            region = (1623, 536, 1770, 566)
            detected_text = extract_text_from_screen(region)

            if "Restart Mission" in detected_text:
                if not r_key_held:  # Only press R if it's not already held
                    pyautogui.keyDown('r')  # Hold R down
                    r_key_held = True
            else:
                if r_key_held:  # Release R if the text is no longer detected
                    pyautogui.keyUp('r')
                    r_key_held = False

            # Press '/' every 7 seconds
            if time.time() - last_slash_time >= 7:
                pyautogui.keyDown('/')  # Press '/' key
                pyautogui.keyUp('/')    # Release '/' key
                last_slash_time = time.time()  # Update the time when '/' was last pressed

            # Press 'n' every 15 seconds
            if time.time() - last_n_time >= 15:
                pyautogui.keyDown('n')  # Press 'n' key
                pyautogui.keyUp('n')    # Release 'n' key
                last_n_time = time.time()  # Update the time when 'n' was last pressed

            # Wait 1 second before pressing F after 'n'
            if time.time() - last_f_key_time >= 30:  # Ensure F key is pressed only every 12 seconds after 'n'
                pyautogui.press('f')
                last_f_key_time = time.time()  # Update time when F key is pressed

        time.sleep(0.1)  # Prevent excessive CPU usage and allow the loop to check the time more frequently

# Function to start the automation in a separate thread
def start_automation():
    thread = Thread(target=automation_loop, daemon=True)
    thread.start()

# Function to start the Start Mission automation in a separate thread
def start_start_mission():
    thread = Thread(target=start_mission_loop, daemon=True)
    thread.start()

# Function to start the F9 automation in a separate thread
def start_f9_automation():
    thread = Thread(target=f9_automation_loop, daemon=True)
    thread.start()

# Keyboard listener to toggle Colossi Restart functionality when F12 is pressed
def listen_for_f12():
    keyboard.add_hotkey('f12', toggle_running)
    while True:
        keyboard.wait('f12')

# Keyboard listener to toggle Start Mission functionality when F10 is pressed
def listen_for_f10():
    keyboard.add_hotkey('f10', toggle_start_mission)
    while True:
        keyboard.wait('f10')

# Keyboard listener to toggle F9 functionality when F9 is pressed
def listen_for_f9():
    keyboard.add_hotkey('f9', toggle_f9_running)
    while True:
        keyboard.wait('f9')

# Keyboard listener to toggle GUI visibility when the "`" key is pressed
def listen_for_toggle_gui():
    keyboard.add_hotkey('`', toggle_gui_visibility)
    while True:
        keyboard.wait('`')

# Toggle the visibility of the GUI
def toggle_gui_visibility():
    if root.state() == 'normal':  # If the window is visible
        root.withdraw()  # Hide the window
    else:
        root.deiconify()  # Show the window

# Create the main window
root = tk.Tk()
root.title("Mission Helper")
root.attributes("-topmost", 1)
root.configure(bg="#2e2e2e")

# Hide the title bar and window controls (minimize, maximize, close)
root.overrideredirect(True)

# Make the window transparent
root.wm_attributes("-transparentcolor", "#2e2e2e")

# Set the size of the window
window_width = 400
window_height = 200

# Position the window at the top-right corner of a 1920x1080 screen
screen_width = 1920
screen_height = 1080

# Calculate the position to place the window at the top-right corner
x_position = screen_width - window_width  # Place it right at the edge of the screen
y_position = 0  # Align it to the top (0 pixels from the top edge)

# Set the geometry with new position
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

# GUI elements (Status labels only, no buttons)
state_label = tk.Label(root, text="Colossi Restart (F12): OFF", font=("Arial", 16), fg="red", bg="#2e2e2e")
state_label.pack(pady=10)

start_mission_label = tk.Label(root, text="Restart Field Mission (F10): OFF", font=("Arial", 16), fg="red", bg="#2e2e2e")
start_mission_label.pack(pady=10)

f9_label = tk.Label(root, text="Infiltration Operation Restart (F9): OFF", font=("Arial", 16), fg="red", bg="#2e2e2e")
f9_label.pack(pady=10)

# Start the automation in separate threads when the GUI is loaded
start_automation()
start_start_mission()
start_f9_automation()

# Start the keyboard listener for F12, F10, F9, and "`" in separate threads
keyboard_thread_f12 = Thread(target=listen_for_f12, daemon=True)
keyboard_thread_f12.start()

keyboard_thread_f10 = Thread(target=listen_for_f10, daemon=True)
keyboard_thread_f10.start()

keyboard_thread_f9 = Thread(target=listen_for_f9, daemon=True)
keyboard_thread_f9.start()

keyboard_thread_toggle_gui = Thread(target=listen_for_toggle_gui, daemon=True)
keyboard_thread_toggle_gui.start()

# Function to enable dragging of the window
def on_drag(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

# Bind mouse events to allow window dragging
root.bind('<B1-Motion>', on_drag)

# Start the Tkinter GUI loop
root.mainloop()
