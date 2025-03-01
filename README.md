# QLC+ WebSocket Controller

[![Demo Video](https://img.youtube.com/vi/x1sY_NfgiZQ/0.jpg)](https://www.youtube.com/watch?v=x1sY_NfgiZQ&ab_channel=DanielSaravia)

This Python script connects to a QLC+ WebSocket server and demonstrates DMX control with dynamic 3D visualization. It automatically maps DMX pan and tilt values to a 3D beam direction, visualizes the beam movement along a great circle path, and displays a light cone representing the beam’s spread.

> **Note:** Although earlier versions supported interactive control via keyboard arrow keys, this updated version automatically simulates pan movement (with a fixed tilt) and visualizes the results in real time. You can still integrate keyboard control (e.g., with `pynput`) if desired.

## Features
- **Dynamic IP Detection:** Automatically determines your local computer’s IP address.
- **WebSocket Connection:** Establishes a connection to QLC+ at `ws://<LOCAL_IP>:9999/qlcplusWS`.
- **DMX Mapping:** Converts DMX values for pan and tilt into a 3D unit vector using a custom mapping function.
- **3D Visualization:** 
  - Displays a scatter plot of DMX-to-direction mappings.
  - Plots a reference great circle path (with tilt fixed to 0°).
  - Animates a beam marker representing the current DMX values.
  - Renders a dynamic light cone showing the beam’s spread.
- **Automatic Movement:** Oscillates the pan value between 0° and 360° (with tilt fixed at 0°) to simulate a scanning motion.
- **Graceful Termination:** Interrupt the simulation with `Ctrl+C` to safely close the WebSocket connection.

## File Structure
```
.
├── dmx_control.py        # Python script for controlling QLC+ via WebSocket with 3D visualization
├── keypad.html           # (Optional) HTML file for a keypad interface (for interactive control)
├── qlight_workspace.qxw  # QLC+ workspace file
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## Prerequisites

### Python Requirements
- Python 3.x

Install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### QLC+ Setup
- Install and run QLC+ on your host machine.
- Start QLC+ with the web interface enabled:

  ```bash
  qlcplus -w
  ```
  
- By default, QLC+ listens on port **9999** for WebSocket connections.

## How It Works
1. **Dynamic IP Detection:**  
   The script uses the Python `socket` module to automatically determine your local IP address.

2. **WebSocket Connection:**  
   A connection is established to the QLC+ server at `ws://<LOCAL_IP>:9999/qlcplusWS`.

3. **DMX-to-XYZ Mapping:**  
   DMX values for pan and tilt are converted into a 3D unit vector representing the beam direction. The mapping assumes:
   - **Pan:** DMX (0–255) maps to 0°–540° rotation about the Z-axis.
   - **Tilt:** DMX (0–255) maps to 0°–205° rotation about the X-axis.

4. **Visualization:**  
   - A grid of DMX values is converted into corresponding 3D vectors and displayed as a background field.
   - A red great circle path is plotted as a reference.
   - An animated beam marker shows the current DMX-driven direction.
   - A dynamic light cone is computed and rendered to illustrate the beam’s spread.

5. **Automatic Movement:**  
   The script automatically oscillates the pan value (while keeping tilt at 0°), sending updated DMX commands to QLC+ in a loop. This simulates a continuous scanning motion.

6. **Graceful Exit:**  
   Use `Ctrl+C` (triggering a KeyboardInterrupt) to stop the simulation. The WebSocket connection will then be closed safely.

## Usage
1. Clone or download the project files.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python dmx_control.py
   ```
4. An interactive matplotlib window will open showing the 3D visualization.  
5. To exit, press `Ctrl+C` in the terminal.

## Example Output
```
Connected to QLC+ WebSocket at ws://192.168.1.50:9999/qlcplusWS.
Sent: CH|1|178
Sent: CH|3|0
...
Movement interrupted by user.
WebSocket closed.
```

## Requirements
Dependencies listed in `requirements.txt`:
- certifi==2024.12.14
- charset-normalizer==3.4.1
- idna==3.10
- requests==2.32.3
- urllib3==2.3.0
- websocket-client==1.8.0
- pynput==1.7.6

Install them using:
```bash
pip install -r requirements.txt
```

## Code Overview
The main script (`dmx_control.py`) includes:

- **Imports:**  
  Uses `numpy` for numerical operations, `matplotlib` (with `mpl_toolkits.mplot3d`) for 3D visualization, and `websocket` for WebSocket communication.

- **Dynamic IP Detection:**  
  The `get_host_ip()` function retrieves your local IP address by creating a UDP connection to a public DNS server.

- **DMX-to-XYZ Conversion:**  
  The `dmx_to_xyz()` function maps DMX values for pan and tilt to a 3D direction vector. This vector is then used to update the beam’s direction in the visualization.

- **Visualization Setup:**  
  The script:
  - Creates a grid of DMX values and maps them to 3D vectors.
  - Plots these as a scatter field.
  - Draws a reference great circle path.
  - Initializes an animated marker for the current beam direction.
  - Computes and displays a dynamic light cone based on the beam direction.

- **Automatic Movement:**  
  A loop updates the pan angle (oscillating between 0° and 360°), computes corresponding DMX values, sends them to QLC+, and updates the visualization in real time.

- **Graceful Termination:**  
  The script catches a `KeyboardInterrupt` to stop the movement and close the WebSocket connection.

## Citations
- `pynput`: https://pypi.org/project/pynput/
- `websocket-client`: https://pypi.org/project/websocket-client/
- Python `socket` library documentation: https://docs.python.org/3/library/socket.html
- Starter code inspiration: [ChatGPT Share](https://chatgpt.com/share/67bb92eb-d380-8012-8681-535bc6395a02)

## License
This project is open-source and available under the [MIT License](LICENSE). Feel free to modify and distribute it as needed.

