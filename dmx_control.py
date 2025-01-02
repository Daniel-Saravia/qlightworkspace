import time
import requests

# QLC+ Web Interface settings
QLC_URL = "http://192.168.1.100:9999/keypad.html"   # or replace with the IP of your QLC+ machine
UNIVERSE_ID = 1
API_ENDPOINT = f"{QLC_URL}/api/universe/{UNIVERSE_ID}/set_dmx"

def set_dmx(channel, value):
    """
    Sends a DMX value (0-255) to a specific channel via QLC+ Web API.
    """
    payload = {channel: value}
    try:
        response = requests.post(API_ENDPOINT, json=payload)
        if response.status_code == 200:
            print(f"Channel {channel} -> {value}")
        else:
            print(f"[Error] Failed to set DMX value: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[Error] Could not reach QLC+: {e}")

def pan_sweep():
    """
    Continuously sweeps pan channel (channel 1) from 0 to 255 and back.
    Press Ctrl+C to stop the script.
    """
    try:
        while True:
            # Sweep up (left to right)
            for val in range(0, 256, 5):
                set_dmx(1, val)
                time.sleep(0.05)  # Adjust speed as needed

            # Sweep down (right to left)
            for val in range(255, -1, -5):
                set_dmx(1, val)
                time.sleep(0.05)
    except KeyboardInterrupt:
        print("\nStopping pan sweep. Goodbye!")

if __name__ == "__main__":
    print("Starting pan sweep. Press Ctrl+C to stop.")
    pan_sweep()
