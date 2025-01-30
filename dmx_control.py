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

QLC_IP = get_host_ip()
QLC_WS_URL = f"ws://{QLC_IP}:9999/qlcplusWS"

ws = websocket.WebSocket()
ws.connect(QLC_WS_URL)
print(f"Connected to QLC+ WebSocket at {QLC_WS_URL}.")

pan_value = 128  # Initial value for pan (channel 1)
tilt_value = 128  # Initial value for tilt (channel 3)

def send_dmx_value(channel, value):
    """Send a DMX value to the specified channel."""
    ws.send(f"CH|{channel}|{value}")
    print(f"Sent: CH|{channel}|{value}")

def on_press(key):
    global pan_value, tilt_value

    try:
        if key == keyboard.Key.right:
            pan_value = min(pan_value + 50, 255)
            send_dmx_value(1, pan_value)
        elif key == keyboard.Key.left:
            pan_value = max(pan_value - 50, 0)
            send_dmx_value(1, pan_value)
        elif key == keyboard.Key.up:
            tilt_value = min(tilt_value + 50, 255)
            send_dmx_value(3, tilt_value)
        elif key == keyboard.Key.down:
            tilt_value = max(tilt_value - 50, 0)
            send_dmx_value(3, tilt_value)
    except AttributeError:
        pass  # Ignore non-special keys

def on_release(key):
    if key == keyboard.KeyCode.from_char('q'):
        print("Exiting...")
        return False  # Stop the listener

print("Use arrow keys to control pan (left/right) and tilt (up/down). Press 'q' to quit.")

# Set up the key listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Close the WebSocket connection``
ws.close()
print("WebSocket closed.")