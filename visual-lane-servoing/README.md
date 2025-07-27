
# **Duckietown**

# **Visual Lane servoing**

Visual lane servoing is a real-time control method used in autonomous vehicles or robotic systems to dynamically adjust the vehicles path based on visual feedbacks specifally using lane markings detected through a camera. This documment will give the reader a high level overview of some key concepts needed for this task and a step-by-step work through of how the duckiebot navigates it's duckietown world. 

# Table of content

- [Overview](#overview)
- [Prerequisite](#prerequisite)
- [Instruction setup](#instruction-setup)
     - [clone Rpository](#clone-repository)
- [Procedure and high-level explanation](#procedure-and-high-level-explanation)
     - [1. Camera calibration](#camera-calibration)
     - [2. Image filtering](#image-filtering)
     - [3. Visual Servoing](#visuala-servoing)
- [Apply the theory](#apply-the-theory)
- [Testing in simulation](#testing-in-simulation)
- [Testing in phyiscal robot](#testing-in-physical-robot)
- [Conclusion](#conclusion)

# Overview

The duckiebot uses it's mounted camera to perceive the duckietown and generate real-time commands inorder to navigate. Found in this task is a notebook with detail explanation on key concepts used to archieve this task such as; 
- camera parameters
- Image filtering techniques
- Visual servoing 

## Prerequisite 

- Python 3.x
- Jupyter Notebook
- Opencv
- duckiebot
- duckietown
- Camera model


## Instruction setup

1. Clone Repository

   '''bash
   git clone https://github.com/N-Pierro/duckiebot005
   cd visual-lane-servoing
   '''

 Login to the duckietown dashboard and verify that all the packages are installed and system health checks are ok

##  Procedure and high-level explanation 

### 1. Camera Calibration

The camera does a linear transformation, that projects a 3D world point onto a 2D image using using a multiplication matrix that relys on: 
1.1 Intrinsic matrix: internal properties of the camera (lens, resolution, etc)
1.2 Extrinsic matrix: describes the cameral position and orientation

   - Make sure the duckiebot is charged and powered on
   - Use a checkboard image to extract:
        - focal lenght
        - optical center
        - lense distortion effiecency 
   follow the `camer_calibration.ipynb ` documment and save the results.

   - verfy the changes have been saved:
        - Go to Dashboard > File Manages > config > calibrations > ( camera_intrinsic or camera_extrinsic page)
   - in addition to the default.yml there will be a ROBOTNAME.yml file

### 2. Image Filtering 

The duckiebot uses it's camera to extract useful features, particulary for task like lane detection, object localization or visual servoing. By using several image filtering methods such as the: 
   - Gaussian blur: for noise reduction and smooth image
   - Thresholding: convert grayscal to image binary
   - Edge detection: for lane detection or object contours

For more detail guide refer to the `image_filtering.ipynb` in the notebook section

### 3. Visual Servoing

The goal is to design a control policy that uses only images streamed from the Duckiebot's camera to keep it in the lane as it drives forward at a fixed velocity. 
- Place the duckiebot in the center of it's lane
- By using the camera the dockiebot is able to process the images that are constantly captured as it drives
- The processed image is used to detect the lane center and compute the steer error
- The PID controller is used to generate real-time commands combined with the procedded image keeps the duckiebot within the lane.

## Apply the theory

The duckiebot comes witha a simulation enviroment which gives the possibility to try out modifications before applying on the actual duckiebot. 

### Testing in simulation

To test in simulation, use the command 

```bash

dts code workbench --sim
`
```

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

At the end of this task the duckiebot is able to follow a single lane by using camera calibration and multiple image processing techniques. 

## Author: Njomeny Pierro M.M 







