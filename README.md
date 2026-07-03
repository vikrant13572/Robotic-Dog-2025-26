# Quadruped Robot Movement Control

A collection of Arduino programs for controlling the movement of a quadruped robot using servo motors. This repository includes different movement patterns, servo testing programs, and a Python simulation for validating leg motions.

## Features

- Individual servo angle testing
- Control of all four legs simultaneously
- Straight walking implementation
- Multiple movement/gait patterns
- Python simulation for movement visualization and testing

## Repository Structure

| File | Description |
|------|-------------|
| `90_degtest.ino` | Tests servo movement at 90° position for calibration. |
| `all_legs_pp.ino` | Controls all four legs together for coordinated motion. |
| `movement1.ino` | Implements the first walking/movement sequence. |
| `movement2.ino` | Implements an alternative walking/movement sequence. |
| `straight_final.ino` | Final implementation for straight-line walking. |
| `ppfinalsim_new.py` | Python simulation for testing and visualizing robot movement logic. |

## Hardware Requirements

- ESP32 / ESP8266
- Servo Motors (SG90/MG90S or equivalent)
- Quadruped robot chassis
- External power supply for servos
- Jumper wires

## Software Requirements

- Arduino IDE
- Python 3.x
- Required Python libraries (if any)

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

2. Open the required `.ino` file in Arduino IDE.

3. Select the correct:
   - Board
   - COM Port

4. Upload the program to the ESP32/ESP8266.

5. Power the robot and observe the movement.

## Project Workflow

1. Calibrate servos using `90_degtest.ino`
2. Test coordinated leg movement using `all_legs_pp.ino`
3. Experiment with different gait algorithms:
   - `movement1.ino`
   - `movement2.ino`
4. Run the optimized walking program:
   - `straight_final.ino`
5. Use `ppfinalsim_new.py` to simulate and verify movements before deployment.

## Future Improvements

- Obstacle avoidance
- Bluetooth/Wi-Fi control
- Camera-based navigation
- Face tracking
- IMU-based balancing
- Multiple gait algorithms (crawl, trot, bound)

## Author

**Vikrant Kumar Singh**

---

Feel free to contribute by suggesting improvements or optimizing the gait algorithms.
