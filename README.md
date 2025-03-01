# Moving Headlight Controller

[![Demo Video](https://img.youtube.com/vi/x1sY_NfgiZQ/0.jpg)](https://www.youtube.com/watch?v=x1sY_NfgiZQ&ab_channel=DanielSaravia)

This Python script connects to a QLC+ WebSocket server, enabling automated DMX control and dynamic 3D visualization. It maps DMX pan and tilt values to visualize beam direction, movement paths, and a beam spread cone in real time.

> **Note:** Interactive keyboard control via arrow keys (`pynput`) can also be integrated if desired.

## Features
- **Dynamic IP Detection:** Automatically finds your computer’s IP.
- **WebSocket Connection:** Connects seamlessly to QLC+ at `ws://<LOCAL_IP>:9999/qlcplusWS`.
- **DMX Mapping:** Converts DMX pan/tilt values into 3D beam direction vectors.
- **3D Visualization:**
  - Scatter plot of beam directions.
  - Great circle reference path visualization.
  - Animated marker displaying live DMX positions.
  - Real-time rendered beam spread cone.
- **Automatic Movement:** Oscillates pan from 0°–360° with fixed tilt to demonstrate scanning.
- **Graceful Exit:** Safely terminates simulation with `Ctrl+C`.

## Project Structure
```
.
├── dmx_control.py        # Main script for DMX control and visualization
├── keypad.html           # Optional keypad HTML interface
├── qlight_workspace.qxw  # QLC+ workspace configuration
├── README.md             # Project documentation
└── requirements.txt      # Dependencies list
```

## Installation

### Python
Requires Python 3.x

Install dependencies:

```bash
pip install -r requirements.txt
```

### QLC+ Setup
- Install QLC+ software.
- Enable web interface with:

```bash
qlcplus -w
```

(Default WebSocket port: **9999**)

## Usage
1. Clone/download the project.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python dmx_control.py
```

4. Visualization appears automatically. Press `Ctrl+C` to exit.

## Example Output
```
Connected to QLC+ WebSocket at ws://192.168.1.50:9999/qlcplusWS.
Sent: CH|1|178
Sent: CH|3|0
...
Movement interrupted by user.
WebSocket closed.
```

## Dependencies
- certifi
- charset-normalizer
- idna
- requests
- urllib3
- websocket-client
- pynput

Install with:

```bash
pip install -r requirements.txt
```

## Code Overview
- **Dynamic IP Detection:** `get_host_ip()` retrieves the local IP via UDP.
- **DMX-to-XYZ Mapping:** Converts DMX values to 3D vectors.
- **Visualization:**
  - DMX grid converted to a 3D scatter field.
  - Plots reference great circle.
  - Animates beam marker and cone visualization.
- **Automatic DMX Movement:** Continuously updates pan for simulation.
- **Graceful Termination:** `KeyboardInterrupt` closes WebSocket safely.

## Citations
- [`pynput`](https://pypi.org/project/pynput/)
- [`websocket-client`](https://pypi.org/project/websocket-client/)
- [Python `socket`](https://docs.python.org/3/library/socket.html)
- [Starter code inspiration](https://chatgpt.com/share/67bb92eb-d380-8012-8681-535bc6395a02)

## License
Distributed under the [MIT License](LICENSE). Modify and distribute freely.
