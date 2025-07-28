
# **Duckietown Challenge**

# **State Estimation**

The objective of this task is to determine the state of the robot (it's position, orientation, velocity, etc) using sensor data and mathematical models. Widely used filter algorithims like; kalman-filter, particle filter will be discussed and altimately develope functions based on the histogram filter to accurately estimate the state of our robot. 

# Table of content

- [Overview](#overview)
- [Prerequisite](#prerequisite)
- [Instruction setup](#instruction-setup)
  - [Clone Repository](#clone-repository)
- [Procedure](#procedure)
  - [1. Define the Prior function](#1-define-the-prior-function)
    - [Step-by-step breakdown](#step-by-step-breakdown)
      - [Construct a grid of 2D coordinates](#construct-a-grid-of-2d-coordinates)
      - [Define the Gaussian distribution](#define-the-gaussian-distribution)
      - [Evaluate the PDF over the grid and return the belief](#evaluate-the-pdf-over-the-grid-and-return-the-belief)
  - [2. Prediction (motion update)](#2-prediction-motion-update)
  - [3. Update the robot's belief](#3-update-the-robots-belief)
- [Apply the theory](#apply-the-theory)
- [Testing in simulation](#testing-in-simulation)
- [Testing in physical robot](#testing-in-physical-robot)
- [Conclusion](#conclusion)


# Overview
1. Kalman filter: is a recursive bayesian filter that maintains the current mean and covariance of the state and update at each time step using the control input and measurement data.
2. Particle filter; uses a set of particles to represent the belief distribution where each particle represents the hypothesis of a state along with weight that represents how likely it is. Works well with non-linear and non-Gaussian systems but performance depends on the number of particles.
3. Histogram filter; is a discrete, grid-based state estimatiom algorithm used to estimate the probability distribution of the robot's position over a state space. It can handle non-Gaussian and multi modal distribution, highly used in 2D localization. 

## Prerequisite 

- Python 3.x
- Jupyter Notebook
- Opencv
- Go through the notebook
- Make sure all ROS packages are installed



## Instruction setup

1. Clone Repository

   ```bash
   git clone https://github.com/N-Pierro/duckiebot005
   cd state-estimation
   ```

 Login to the duckietown dashboard and verify that all the packages are installed and system health checks are ok

##  Procedure 

For this task we will rely on the belief update cycle of the Histogram filter

### 1. Define the Prior function 

Here we choose to initialize the historgram based on a Gaussian distribution around 
```python
def histogram_prior(belief, grid_spec, mean_0, cov_0):
```

- **Step-by-step breakdown:**
  - Construct a grid of 2D coordinates:

- **code snippet**
  ```python
  pos = np.empty(belief.shape + (2,))
    pos[:, :, 0] = grid_spec["d"]
    pos[:, :, 1] = grid_spec["phi"]
  ```
  - Define the Gaussian distribution

  - **code snippet**
  ```python
   RV = multivariate_normal(mean_0, cov_0)
  ```
  - Evaluate the PDF over the grid and return the belief

  - **code snippet**
  ```python
   RV = multivariate_normal(mean_0, cov_0)
    belief = RV.pdf(pos)
    return belief
  ```
### 2. Prediction (motion update) 

This function updates the current belief distribution by predicting the next state of the robot based on it's motion model and control input from wheel encoder

- **code snippet**
```python
def histogram_predict(belief, left_encoder_ticks, right_encoder_ticks, grid_spec, robot_spec, cov_mask):
    belief_in = belief
```

### 3. Update the robot's belief

This function produces a likelihood map, a grid that predicts would this sensor readings be if the robot where at this specific state 

- **code snippet**
```python

def histogram_update(belief, segments, road_spec, grid_spec):
    # prepare the segments for each belief array
    segmentsArray = prepare_segments(segments, grid_spec)
    # generate all belief arrays

    measurement_likelihood = generate_measurement_likelihood(segmentsArray, road_spec, grid_spec)

    if measurement_likelihood is not None:
        belief = belief * measurement_likelihood  # element-wise multiplication
        belief = belief / np.sum(belief)  # normalize
    return measurement_likelihood, belief
```
  
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

## Conclusion

State estimation is a fundamental challenge in robotics that determines how accurately a robot can determine it's own position, orientatin, and motion within an environment. Due to noise in both sensor measurements of the duckiebot and motion models, state estimation must fuse multiple uncertain sources of information over time. This is where bayesian filtering methods, sucnn as the kalman filter, histogram filter and partivle filter play a critical role. So following this guide will provide the reader with an understanding of state estimation as applicable in robotics.

## Author: Njomeny Pierro M.M 





