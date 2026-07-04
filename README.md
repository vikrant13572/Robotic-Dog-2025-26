# Quadruped Robot Movement Control

A collection of Arduino programs, simulation tools, and kinematics implementations for controlling a quadruped robot using servo motors. This repository includes Arduino-based gait control, Python simulations for path planning and motion visualization, and forward/inverse kinematics implementations for leg movement analysis.

## Features

* Forward and inverse kinematics implementation
* Path planning simulation
* Individual servo angle testing
* Coordinated control of all four legs
* Multiple walking/gait algorithms
* Straight-line walking implementation
* Python-based visualization and movement validation

## Repository Structure

| Folder        | Description                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| `Simulation/` | Contains all Python simulation files for path planning, trajectory generation, and movement visualization.        |
| `Kinematics/` | Contains the implementation of forward and inverse kinematics used for leg position and joint angle calculations. |
| `Arduino/`    | Contains all Arduino (`.ino`) programs for servo control, gait generation, testing, and robot movement.           |

### Arduino Folder Contents

| File                 | Description                                                   |
| -------------------- | ------------------------------------------------------------- |
| `90_degtest.ino`     | Tests servo movement at the 90° position for calibration.     |
| `all_legs_pp.ino`    | Controls all four legs simultaneously for coordinated motion (made for testing callibration). |
| `movement1.ino`      | Implements the first gait sequence.                   |
| `movement2.ino`      | Implements an standing move sequence .              |
| `straight_final.ino` | Final implementation for straight-line walking.   |
| `inversekinematics_left and inverse kinematics_right` | Contains python code for inverse kinematics |
|`pplfinalsim.py` | contains path planning simulation |

## Hardware Requirements

* Arduino UNO
* MG996R Servo Motors
* PLA filament (for 3D-printed parts)
* High-current regulated SMPS
* Jumper wires
* Servo mounting hardware

## Software Requirements

* Arduino IDE
* Python 
* NumPy
* Matplotlib
* MATLAB (optional, for analysis)

## Getting Started

1. Clone this repository.
2. Open the desired Arduino sketch from the `Arduino/` folder using Arduino IDE.
3. Select the appropriate:

   * Board
   * COM Port
4. Upload the program to the Arduino UNO.
5. Power the robot and verify the movement.
6. Run the Python scripts inside the `Simulation/` folder to visualize and validate path planning before deployment.
7. Use the scripts in the `Kinematics/` folder to test forward and inverse kinematics calculations.

## Project Workflow

1. Calibrate all servos using `90_degtest.ino`.
2. Verify coordinated leg movement with `all_legs_pp.ino`.
3. Experiment with different gait implementations (`movement1.ino` and `movement2.ino`).
4. Run `straight_final.ino` for optimized straight-line walking.
5. Validate trajectories using the `Simulation/` folder.
6. Use the `Kinematics/` folder to compute and verify leg joint angles and end-effector positions.

## Future Improvements

* Obstacle avoidance
* Bluetooth/Wi-Fi control
* Camera-based navigation
* Face tracking
* IMU-based balancing
* Additional gait algorithms (crawl, trot, bound, pace)
* ROS integration
* Real-time path planning

## Author

**Vikrant Kumar Singh**

---

Contributions, suggestions, and optimizations for gait algorithms, simulations, and kinematics are always welcome.
