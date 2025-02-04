"""
Daniel Saravia
STG-452: Capstone Project II
February 2, 2025
Citations:
- `pynput`: https://pypi.org/project/pynput/
- `websocket-client`: https://pypi.org/project/websocket-client/
- Python `socket` library documentation: https://docs.python.org/3/library/socket.html

This script connects to a QLC+ WebSocket server and allows the user to control pan and tilt DMX values using arrow keys.
"""

from pynput import keyboard  # Alternative library for key detection
import time
import websocket
import socket

def get_host_ip():
    """Retrieve the local host computer's IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as e:
        print(f"Error determining host IP: {e}")
        return "127.0.0.1"

# Determine QLC+ WebSocket server IP address dynamically
QLC_IP = get_host_ip()
QLC_WS_URL = f"ws://{QLC_IP}:9999/qlcplusWS"

# Establish WebSocket connection to QLC+
ws = websocket.WebSocket()
ws.connect(QLC_WS_URL)
print(f"Connected to QLC+ WebSocket at {QLC_WS_URL}.")

# Initialize pan and tilt DMX values
pan_value = 128  # Default value for pan (channel 1)
tilt_value = 128  # Default value for tilt (channel 3)

def send_dmx_value(channel, value):
    """Send a DMX value to the specified channel through the WebSocket connection."""
    ws.send(f"CH|{channel}|{value}")
    print(f"Sent: CH|{channel}|{value}")

def on_press(key):
    """Handle key press events to adjust DMX pan and tilt values."""
    global pan_value, tilt_value

    try:
        if key == keyboard.Key.right:
            pan_value = min(pan_value + 50, 255)  # Increase pan within limits
            send_dmx_value(1, pan_value)
        elif key == keyboard.Key.left:
            pan_value = max(pan_value - 50, 0)  # Decrease pan within limits
            send_dmx_value(1, pan_value)
        elif key == keyboard.Key.up:
            tilt_value = min(tilt_value + 50, 255)  # Increase tilt within limits
            send_dmx_value(3, tilt_value)
        elif key == keyboard.Key.down:
            tilt_value = max(tilt_value - 50, 0)  # Decrease tilt within limits
            send_dmx_value(3, tilt_value)
    except AttributeError:
        pass  # Ignore keys without special functions

def on_release(key):
    """Handle key release events to exit the program when 'q' is pressed."""
    if key == keyboard.KeyCode.from_char('q'):
        print("Exiting...")
        return False  # Stop the key listener

# Display usage instructions to the user
print("Use arrow keys to control pan (left/right) and tilt (up/down). Press 'q' to quit.")

# Start the keyboard listener to detect key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Close the WebSocket connection when exiting
ws.close()
print("WebSocket closed.")
