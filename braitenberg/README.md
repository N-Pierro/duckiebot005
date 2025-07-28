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

### 1. Adjusting HSV Settings

The first step involves adjusting HSV settings for image processing to help the robot detect obstacles effectively. HSV color space is beneficial as it separates color information from intensity, making it easier to detect objects under varying lighting conditions.

- **Procedure**:
  - Start with an image of a duck and adjust the HSV values using the `braitenberg02.ipynb` notebook.
  - Fine-tune the HSV parameters to filter out the background and isolate the duck.

- **Code Snippet**:
  ```python
  # Example from braitenberg02.ipynb
  def adjust_hsv(image):
      hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
      mask = cv2.inRange(hsv, lower_bound, upper_bound)
      result = cv2.bitwise_and(image, image, mask=mask)
      return result
  ```

### 2. Fine-Tuning Preprocessing

Once the optimal HSV values are determined, adjust these parameters in the preprocessing file to apply them to the robot's vision system.

- **Procedure**:
  - Use the `preprocessing.py` script to set the optimal HSV values for detecting ducks.
  - Fine-tune the preprocessing steps to ensure the robot can effectively filter out unnecessary elements and focus on detecting ducks.

- **Code Snippet**:
  ```python
  # Example from preprocessing.py
  def preprocess_image(image):
      hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
      mask = cv2.inRange(hsv, optimal_lower_bound, optimal_upper_bound)
      processed_image = cv2.bitwise_and(image, image, mask=mask)
      return processed_image
  ```

### 3. Configuring Robot's Behavior

After preprocessing is fine-tuned, the next step is to configure how the robot's motors respond to the processed images, dictating how the robot reacts when a duck is detected.

- **Procedure**:
  - Adjust motor response settings in the `connections.py` file.
  - Experiment with different configurations to ensure smooth navigation around detected obstacles.

- **Code Snippet**:
  ```python
  # Example from connections.py
  def control_motors(sensor_input):
      if sensor_input == "duck_detected":
          left_motor_speed = calculate_speed_left()
          right_motor_speed = calculate_speed_right()
          apply_motor_control(left_motor_speed, right_motor_speed)
  ```


