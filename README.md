# Advanced Keylogger (Educational Only)

This is an **educational Python keylogger** built with `pynput` for learning about keyboard event monitoring and logging.


##  DISCLAIMER
⚠️ **This project is for ethical, educational, and personal learning use only.**  
Never run a keylogger on any device that you do not own or without clear, explicit consent.


##  Features
- Logs all keystrokes with timestamps.
- Saves logs daily in a `logs/` folder.
- Handles special keys like `[ENTER]`, `[SPACE]`, etc.
- Stop logging safely by pressing the `ESC` key.


##  How to Run

```bash
# 1. Install dependencies
pip install pynput

# 2. Run the keylogger
python advanced_keylogger.py

# 3. To stop, press ESC.
