
# **Duckietown Challenge**

# **Modcon**

The aim of this task is to demonstrate modeling and control.  This includes calculating odometry, visualizing the estimation of robot agent's pose in the world,wheel calibration and tuning the PID controller.

# Table of content

- [Overview](#overview)
- [Prerequisite](#prerequisite)
- [Instruction setup](#instruction-setup)
  - [1. Clone Repository](#1-clone-repository)
  - [2. Wheel Calibration](#wheel-calibration)
  - [3. Odometry](#3-odometry)
  - [4. PID controller](#4-pid-controller)
- [Apply the theory](#apply-the-theory)
- [Testing in simulation](#testing-in-simulation)
- [Testing in physical robot](#testing-in-physical-robot)



# Overview

Three key concepts widely used in robicts system will be covered in this task. Implementing knowledge from this concepts permits the duckiebot to navigate the duckietown. These concepts include:
- Wheel calibration: calibrates the motor/wheel assemblies of the robots by determining two calibration parameters, ensuring the duckiebot goes straight when commanded to do so and the wheels do not slip.
- Odometry: is the measuring of the path or pose in time of the robot.
- PID Control: is incharge of the robots decision makin by sending commands as signals to the robots actuators. 

## Prerequisite 

- Python 3.x
- Jupyter Notebook
- Go through the notebook
- Make sure all ROS packages are installed
- Duckiebot (properly configured and charged)


## Instruction setup

### 1. Clone Repository

   ```bash
   git clone https://github.com/N-Pierro/duckiebot005
   cd modcon
   ```

 Login to the duckietown dashboard and verify that all the packages are installed and system health checks are ok


### 2. Wheel Calibration 

This will be the entry poin to this task. Two assumptions are introduced:
- The wheels of the robot do not slip
- The robot is symmetrical along the longitudinal axes

The two parameters of focus at this step are: 
- Calibrating the gian (g) 
- Calibrating the trim (t)

Follow the wheel calibration steps described in the `wheels-calibration.ipynb` of the notebook. The default values for the wheel gian is set to 1 and the trim is set to 0. Adjust these values if needed and save them.

- **code snippet**
```python
# example code for wheel calibration
def calibrate_wheels():
    # Adjust wheel speeds
    left_wheel_speed = adjust_speed(left_initial_speed)
    right_wheel_speed = adjust_speed(right_initial_speed)
    
    # Apply the calibration
    apply_calibration(left_wheel_speed, right_wheel_speed)
```

### 3. Odometry

As mentioned earlier this concept is used to measure the robots position and orientation in the world. 
- Power on the duckiebot and drive it; as the robot moves wheel encoders measure the rotation of each wheel.
- The distance traveled by each wheel is calculated based on the wheels circumfrence and the number of rotation.
- The robot's position is updated using the distances traveled by the left and right wheels, taking into account the robot's orientation.

### 4. PID Controller

The PID controller is the part of the duckiebot designed to send control signals (commands) to the motors of the robot, causing it to increase, decrease or maintain speed, coordinate with the camera sensor making it to move on a specific path.
- Follow the exercises inthe notebook and run the `pid_controller.py `

  
## Apply the theory

The duckiebot comes witha a simulation enviroment which gives the possibility to try out modifications before applying on the actual duckiebot. 

### Testing in simulation

To test in simulation, use the command 
    
    $ dts code workbench --sim

In this case you should use the link for the VNC environment. It should look something like 

```commandline
================================================================
|                                                              |
|    VNC running at http://127.0.0.1:32768                     |
|                                                              |
================================================================
```

Click on that link (note that the port number 32768 will probably be different but that's ok).

### Testing on physical robot

1. Test on physical robot using the command

```bash
dts code workbench --duckiebot YOUR_DUCKIEBOT
```

This runs both the duckiebot drivers and agent on the robot.

2. You can also test using

```bash
dts code workbench --duckiebot YOUR_DUCKIEBOT --local
```

This command runs the duckiebot drivers on the robot while the agent runs on the laptop

## Author: Njomeny Pierro M.M 





