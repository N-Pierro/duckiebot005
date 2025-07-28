# Duckietown

# Braitenberg

This task studies how image processing is done, converting color to hsv which makes it easy to track. This is will be useful for the duckiebot to filter and track ducks in the robot world.

## Table of Content



## Overview

This task uses a multiple techniques designed to maninpulate and filter images by importoring and analyzing images, after which this technique will be programmed into the duckiebot to idenfify objects. 

1. Image Manipulation: This involve; loading and visualizing images, croping images and modifying images
2. Image Filtering: This initially converts an image to hsv color space and then apply a simple image processing technique to highlight the region corresponding to a certain color.
3. Braitenberg agent: A technique that is used to avoid collision with the ducks.

## Prerequisites

- Python 3.x
- Jupyter Notebook
- OpenCV
- Duckietown ROS Packages
- Basic understanding of image processing and robot control systems

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dadashbaylinurlan/duckie04.git
   cd braitenberg
   ```

## Steps

### 1. Image Manipulation 

Image manipulation involves several steps:
- Loading and Visualizing Images: It demonstrates how to load a JPEG image and visualize it using Python libraries. The image's dimensions and data type are examined.
- Cropping Images: Techniques for cropping images using multidimensional array notation are covered. Users can select specific portions of an image and visualize the cropped result.
- Color Channel Isolation: The notebook explains how to isolate and visualize individual color channels (Red, Green, Blue) and convert the image to grayscale.
- Modifying Images: Users learn to modify images by creating copies and drawing shapes, such as lines and rectangles, on them. Examples include drawing a red line and creating a yellow box.
- Activity: The notebook concludes with an activity where users are encouraged to make a copy of an image, draw a blue rectangle, and paste a section of the image into another location.

code snippets can found in the `braitenberg01.py` file of the notebook

### 2. Image Filtering

The focus is on applying image manipulation techniques for basic filtering to highlight duckies in images, which will aid in avoiding collisions with them. The steps include:
- Loading a Test Image: A sample image is loaded for processing.
- Color Space Conversion: The image is converted from RGB to HSV (Hue, Saturation, Value) color space, which simplifies color-based filtering.
- Defining Color Bounds
- Filtering the Image: The defined HSV bounds are used to filter the image, highlighting the regions corresponding to the specified color.

refere to the `image_filtering.py` of the notebook.

### 3. Braitenberg agent

The focus is on implementing a Braitenberg agent designed to avoid duckies using image filtering techniques. The steps involved include:
- Agent Setup: The agent's motor control is defined by the equations:
  ```python
   left_motor = const + gain * np.sum(LEFT * preprocess(image))
   right_motor = const + gain * np.sum(RIGHT * preprocess(image))
  ```
- Function Implementation: implement the functions `get_motor_left_matrix()` and `get_motor_right_matrix()` in the connections.py file, replacing the current random values with your own.
- Agent Functionality: The main functionality of the Braitenberg agent, including reading observations and creating motor commands, is contained in the `agent.py `file, which will utilize the motor matrix functions from `connections.py`.
- Visualization: Before modifying the code, visualize the output of the motor matrix functions by loading them into the notebook. This helps in understanding how the matrices will affect the agent's behavior.
- Image Processing: The code provided in `braitenberg03.py` allows for visualize the original images, preprocessed images, and the effects of the left and right motor matrices on the agent's control decisions.



## Conclusion

At the end of this task a model that can fine-tune the weight matrices so that the agent effectively avoids duckies by responding appropriately to the highlighted areas in the images is developed. This is essential for the duckiebot to navigate in the duckietown world. 


