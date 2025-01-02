import time
import websocket

# Replace with the IP or hostname of the machine running QLC+,
# and ensure QLC+ is started with the web interface enabled (qlcplus -w).
QLC_IP = "192.168.1.100"
QLC_WS_URL = f"ws://{QLC_IP}:9999/qlcplusWS"

def main():
    try:
        # Create a WebSocket connection to QLC+
        ws = websocket.WebSocket()
        ws.connect(QLC_WS_URL)
        print("Connected to QLC+ WebSocket.")

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
