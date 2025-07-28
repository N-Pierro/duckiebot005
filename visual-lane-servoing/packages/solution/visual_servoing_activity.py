from typing import Tuple

import numpy as np
import cv2


def get_steer_matrix_left_lane_markings(shape: Tuple[int, int]) -> np.ndarray:
    """
    Args:
        shape:              The shape of the steer matrix.

    Return:
        steer_matrix_left:  The steering (angular rate) matrix for Braitenberg-like control
                            using the masked left lane markings (numpy.ndarray)
    """
      height, width = shape
    steer_matrix_left = np.zeros((height, width))

    # Higher values on the left side of the image to steer away from left lane
    for i in range(height):
        for j in range(width):
            steer_matrix_left[i, j] = -1 * ( j / width) 

    return steer_matrix_left
    

def get_steer_matrix_right_lane_markings(shape: Tuple[int, int]) -> np.ndarray:
    """
    Args:
        shape:               The shape of the steer matrix.

    Return:
        steer_matrix_right:  The steering (angular rate) matrix for Braitenberg-like control
                             using the masked right lane markings (numpy.ndarray)
    """
    height, width = shape
    steer_matrix_right = np.zeros((height, width))

    # Higher values on the right side of the image to steer away from right lane
    for i in range(height):
        for j in range(width):
            steer_matrix_right[i, j] = (j / width)  # steer to left

    return steer_matrix_right


def detect_lane_markings(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Args:
        image: An image from the robot's camera in the BGR color space (numpy.ndarray)
    Return:
        mask_left_edge:   Masked image for the dashed-yellow line (numpy.ndarray)
        mask_right_edge:  Masked image for the solid-white line (numpy.ndarray)
    """
    h, w, _ = image.shape

     # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Yellow for left (dashed)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([35, 255, 255])
    mask_left_edge = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # White for right (solid)
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 40, 255])
    mask_right_edge = cv2.inRange(hsv, lower_white, upper_white)

    # Normalize masks to float32
    mask_left_edge = mask_left_edge.astype(np.float32) / 255.0
    mask_right_edge = mask_right_edge.astype(np.float32) / 255.0

    return mask_left_edge, mask_right_edge

def compute_steering(image: np.ndarray) -> float:
    """
    Computes the steering command for the Duckiebot based on lane detection using 
    Braitenberg-style control.

    Args:
        image (np.ndarray): BGR image from the robot's front-facing camera.

    Returns:
        float: Steering command (positive = turn left, negative = turn right).
    """
    # Detect lane edges
    mask_left, mask_right = detect_lane_markings(image)

    # Get steering influence matrices for both lane edges
    left_weights = get_steer_matrix_left_lane_markings(mask_left.shape)
    right_weights = get_steer_matrix_right_lane_markings(mask_right.shape)

    # Calculate weighted sums of activations for left and right
    influence_left = np.sum(left_weights * mask_left)
    influence_right = np.sum(right_weights * mask_right)

    # Combine the influences to produce the final steering value
    steering = influence_left + influence_right

    #normalize steering to keep within reasonable bounds
    #steering = np.clip(steering, -1.0, 1.0)

    return steering
