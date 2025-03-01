# QLC+ WebSocket Controller
![image](https://github.com/user-attachments/assets/8a3ad0e1-aebd-4ec4-83d7-920381c55baf)
https://www.youtube.com/watch?v=x1sY_NfgiZQ&ab_channel=DanielSaravia
This Python script connects to a QLC+ WebSocket server and demonstrates interactive control of DMX channels using the keyboard arrow keys. It dynamically determines the host machine’s IP address, allowing seamless integration with the local QLC+ server.

## Features

- **Dynamically resolves** the host computer’s IP address.  
- **Connects** to a QLC+ WebSocket server for remote DMX control.  
- **Real-time key-based DMX control** using arrow keys:
  - Left/Right arrows adjust **pan** (Channel 1).  
  - Up/Down arrows adjust **tilt** (Channel 3).  
- **Increment/Decrement** values in steps of 50.  
- **Press ‘q’** to exit the script gracefully.

## File Structure

Here’s what the workspace might look like:

```
.
├── dmx_control.py        # Python script for controlling QLC+ via WebSocket
├── keypad.html           # HTML file for keypad interface
├── qlight_workspace.qxw  # QLC+ workspace file
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## Prerequisites

### Python Requirements

- **Python 3.x**  
- Install the dependencies from `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

### QLC+ Setup

1. **Install and run** QLC+ on the host machine.  
2. Start QLC+ with the web interface enabled:
   ```bash
   qlcplus -w
   ```
3. By default, QLC+ listens on port **9999** for WebSocket connections.

## How It Works

1. The script uses the `socket` module to determine your **local IP address** automatically.  
2. A **WebSocket** connection is established to the QLC+ server at `ws://<LOCAL_IP>:9999/qlcplusWS`.  
3. The script **listens** for keyboard arrow key presses:
   - **Left/Right** adjust **Pan** (Channel 1).
   - **Up/Down** adjust **Tilt** (Channel 3).
4. Each press **sends** the updated DMX value to QLC+.  
5. Press **‘q’** to **quit** the script and close the WebSocket connection.

## Usage

1. **Clone** or **download** the project files.  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python dmx_control.py
   ```
4. Use the **arrow keys** to control **Pan** (left/right) and **Tilt** (up/down).  
5. Press **‘q’** at any time to **exit**.

## Example Output

```
Connected to QLC+ WebSocket at ws://192.168.1.50:9999/qlcplusWS.
Use arrow keys to control pan (left/right) and tilt (up/down). Press 'q' to quit.
Sent: CH|1|178
Sent: CH|1|228
Sent: CH|3|178
Exiting...
WebSocket closed.
```

## Requirements

Dependencies listed in **requirements.txt**:

```
certifi==2024.12.14
charset-normalizer==3.4.1
idna==3.10
requests==2.32.3
urllib3==2.3.0
websocket-client==1.8.0
pynput==1.7.6
```

Install them using:

```bash
pip install -r requirements.txt
```

## Code Overview

### `dmx_control.py`

- **Imports**:
  - `socket` for obtaining the local IP address.
  - `websocket` from `websocket-client` for WebSocket communication.
  - `pynput.keyboard` for **arrow key** detection.
- **`get_host_ip()`**:
  - Dynamically retrieves the local IP address by connecting to an external host (8.8.8.8).
- **Global Variables**:
  - `pan_value` and `tilt_value` start at `128`.
  - Each arrow key press increments or decrements by `50`, bounded between `0` and `255`.
- **Key Handlers**:
  - Arrow keys **update** DMX channel 1 (Pan) or 3 (Tilt).
  - `'q'` key **exits** the script.
- **WebSocket Connection**:
  - Connects to `ws://<LOCAL_IP>:9999/qlcplusWS`.
  - Sends DMX channel updates in the format: `CH|<channel>|<value>`.

## Customization

- **Channel Assignments**: Adjust the pan/tilt channels in `dmx_control.py` if your fixture uses different channel numbers.
- **Step Size**: Modify the increment/decrement amount (`50`) to achieve finer or coarser control.
- **WebSocket URL**: Change `QLC_WS_URL` to point to a different IP or port if needed.

## Error Handling

- If the local IP cannot be determined, the script **defaults** to `127.0.0.1`.
- Exceptions during WebSocket connection or key handling are **caught and printed** to the console.

## License

This script is open-source and available under the **MIT License**. Feel free to modify and distribute it as needed.

