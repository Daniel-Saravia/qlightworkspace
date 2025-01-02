import time
import websocket
import socket

def get_host_ip():
    """Retrieve the local host computer's IP address."""
    try:
        # Create a socket connection to determine the local IP address
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Use a dummy address; the IP won't actually connect
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as e:
        print(f"Error determining host IP: {e}")
        return "127.0.0.1"  # Default to localhost on failure

# Replace with the IP or hostname of the machine running QLC+,
# and ensure QLC+ is started with the web interface enabled (qlcplus -w).
QLC_IP = get_host_ip()
QLC_WS_URL = f"ws://{QLC_IP}:9999/qlcplusWS"

def main():
    try:
        # Create a WebSocket connection to QLC+
        ws = websocket.WebSocket()
        ws.connect(QLC_WS_URL)
        print(f"Connected to QLC+ WebSocket at {QLC_WS_URL}.")

        # Example 1: Set channel 1 (Pan) to full (255)
        ws.send("CH|1|255")
        print("Sent: CH|1|255 (Channel 1 -> 255)")
        time.sleep(2)

        # Example 2: Set channel 1 (Pan) to zero (0)
        ws.send("CH|1|0")
        print("Sent: CH|1|0   (Channel 1 -> 0)")
        time.sleep(2)

        # Example 3: Reset entire universe (like pressing the Reset button in Simple Desk)
        # This uses the QLC+API command format:
        ws.send("QLC+API|sdResetUniverse")
        print("Sent: QLC+API|sdResetUniverse (Reset all channels in current Universe)")
        time.sleep(2)

        # Close the connection
        ws.close()
        print("WebSocket closed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
