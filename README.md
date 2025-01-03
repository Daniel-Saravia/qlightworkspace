
# QLC+ WebSocket Controller

This Python script connects to a QLC+ WebSocket server and demonstrates basic control of DMX channels and universe resets. It dynamically determines the host machine's IP address, allowing seamless integration with the local QLC+ server.

## Features

- Dynamically resolves the host computer's IP address.
- Connects to QLC+ WebSocket server for remote control.
- Demonstrates the following QLC+ actions:
  - Set a channel value to full (255).
  - Reset a channel value to zero (0).
  - Reset the entire universe of channels.

## File Structure

Here’s what the workspace looks like:
```
.
├── dmx_control.py        # Python script for controlling QLC+ via WebSocket
├── keypad.html           # HTML file for keypad interface
├── qlight_workspace.qxw  # QLC+ workspace file
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## Prerequisites

1. **Python Requirements**:
   - Python 3.x
   - Install the dependencies from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

2. **QLC+ Setup**:
   - Ensure QLC+ is installed and running on the host machine.
   - Start QLC+ with the web interface enabled:
     ```bash
     qlcplus -w
     ```
   - Default WebSocket port: `9999`.

## How It Works

1. The script uses the `socket` module to determine the host machine's IP address.
2. Establishes a WebSocket connection to the QLC+ server.
3. Sends example commands to demonstrate channel control and universe reset.

## Usage

1. Clone or download the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python dmx_control.py
   ```
4. The script will:
   - Automatically determine the local IP address.
   - Connect to the QLC+ WebSocket server.
   - Execute example actions (channel control and universe reset).

## Example Output

```plaintext
Connected to QLC+ WebSocket at ws://192.168.1.100:9999/qlcplusWS.
Sent: CH|1|255 (Channel 1 -> 255)
Sent: CH|1|0   (Channel 1 -> 0)
Sent: QLC+API|sdResetUniverse (Reset all channels in current Universe)
WebSocket closed.
```

## Requirements

Dependencies listed in `requirements.txt`:
```
certifi==2024.12.14
charset-normalizer==3.4.1
idna==3.10
requests==2.32.3
urllib3==2.3.0
websocket-client==1.8.0
```

Install them using:
```bash
pip install -r requirements.txt
```

## Code Overview

### `dmx_control.py`
- Python script for connecting to QLC+ via WebSocket and sending control commands.

### `get_host_ip()`
- Dynamically retrieves the host machine's IP address using a dummy connection to an external address.

### `main()`
- Establishes a WebSocket connection to QLC+.
- Sends example commands to control DMX channels.

## Customization

- **QLC+ WebSocket URL**: Modify the `QLC_WS_URL` in `dmx_control.py` if using a custom IP or port.
- **Commands**: Replace the example commands with desired QLC+ WebSocket messages.

## Error Handling

- If the local IP cannot be determined, the script defaults to `127.0.0.1`.
- Catches and prints any exceptions during execution.

## License

This script is open-source and available under the MIT License.