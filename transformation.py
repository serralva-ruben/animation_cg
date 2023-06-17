import numpy as np
import math

def translation(v):
    # Creates a translation matrix based on a translation vector.
    size = len(v)
    value = np.eye(size + 1)
    value[:-1, -1] = v
    return value

def dilation(v):
    # Creates a dilation matrix based on a dilation vector.
    size = len(v)
    value = np.eye(size + 1)
    value[:-1, :-1] = np.diag(v)
    return value

def rotation_x(angle):
    # Create a rotation matrix around the X-axis
    angle = np.radians(angle)
    value = np.array([[1, 0, 0, 0],
                      [0, np.cos(angle), -np.sin(angle), 0],
                      [0, np.sin(angle), np.cos(angle), 0],
                      [0, 0, 0, 1]])
    return value

def rotation_y(angle):
    # Create a rotation matrix around the Y-axis
    angle = np.radians(angle)
    value = np.array([[np.cos(angle), 0, np.sin(angle), 0],
                      [0, 1, 0, 0],
                      [-np.sin(angle), 0, np.cos(angle), 0],
                      [0, 0, 0, 1]])
    return value

def rotation_z(angle):
    # Create a rotation matrix around the Z-axis
    angle = np.radians(angle)
    value = np.array([[np.cos(angle), -np.sin(angle), 0, 0],
                      [np.sin(angle), np.cos(angle), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
    return value
