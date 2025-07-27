
# **Duckietown**

# **Visual Lane servoing**

Visual lane servoing is a real-time control method used in autonomous vehicles or robotic systems to dynamically adjust the vehicles path based on visual feedbacks specifally using lane markings detected through a camera. This documment will give the reader a high level overview of some key concepts needed for this task and a step-by-step work through of how the duckiebot navigates it's duckietown world. 

# Table of content

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

## Software setup

1. Clone Repository
   '''bash
   git clone https://github.com/N-Pierro/duckiebot005
   cd visual-lane-servoing
   '''

2. Login to the duckietown dashboard and verify that all the packages are installed and system health checks ae ok

## Procedure and high-level explanation 

### 1. Camera Calibration

The camera does a linear transformation, that projects a 3D world point onto a 2D image using using a multiplication matrix that relys on: 
- Intrinsic matrix: internal properties of the camera (lens, resolution, etc)
- Extrinsic matrix: describes the cameral position and orientation
  



