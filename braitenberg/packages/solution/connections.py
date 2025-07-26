from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # Generate weighted marix for the left motor
    res = np.zeros(shape=shape, dtype="float32")
    # This enable the selection of the right section of the image for the left motor
    res[:shape[0]//2, :] = 1     
    res[shape[0]:, :] = 0.5     
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # Matrix design/generation for the left motor
    res = np.zeros(shape=shape, dtype="float32")
    # This enable the selection of the right section of the image for the right motor
    res[:shape[0]//2, :] = 0.5
    res[shape[0]:, :] = 1
    return res
