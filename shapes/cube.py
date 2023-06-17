import numpy as np

def generate_cube_points(half_length):
    # Generate all 8 points of a cube
    points = [
        np.array([x, y, z])
        for x in (-half_length, half_length)
        for y in (-half_length, half_length)
        for z in (-half_length, half_length)
    ]
    return points