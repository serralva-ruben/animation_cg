import numpy as np
from math import atan

cubo_points = [[0, 0, 0, 1], [100, 0, 0, 1], [100, 100, 0, 1], [0, 100, 0, 1],
               [0, 0, 100, 1], [100, 0, 100, 1], [100, 100, 100, 1], [0, 100, 100, 1]]


def translate_matrix(M):
    translation_matrix = [[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [-500, -500, -500, 1]]
    return M @ np.matrix(translation_matrix)


def rotate_y_matrix(M, angle):
    rotation_matrix_y = [[np.cos(angle), 0, -np.sin(angle), 0],
                         [0, 1, 0, 0],
                         [np.sin(angle), 0, np.cos(angle), 0],
                         [0, 0, 0, 1]]
    return M @ np.matrix(rotation_matrix_y)


def rotate_x_matrix(M, angle):
    rotation_matrix_x = [[1, 0, 0, 0],
                         [0, np.cos(angle), -np.sin(angle), 0],
                         [0, np.sin(angle), np.cos(angle), 0],
                         [0, 0, 0, 1]]
    return M @ np.matrix(rotation_matrix_x)


def translate_z_matrix(M):
    translation_z_matrix = [[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, -122.47, 1]]
    return M @ np.matrix(translation_z_matrix)


def perspective_matrix(M, C_Z):
    perspective_matrix = [[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 0, -1 / C_Z],
                          [0, 0, 0, 1]]
    return M @ np.matrix(perspective_matrix)


def divide_by_w(M):
    print(M)
    divided_points = []
    for i in range(len(M)):
        divided_points.append([M[i][0] / M[i][3], M[i][1] / M[i][3]])
    return divided_points


def camera_transform(M):
    angle_x = atan(-50 / -50)
    angle_y = atan(-100 / 70.71)
    C_Z = -122.47
    M = np.matrix(M)
    M = translate_matrix(M)
    M = rotate_y_matrix(M, angle_x)
    M = rotate_y_matrix(M, angle_y)
    M = translate_z_matrix(M)
    M = perspective_matrix(M, C_Z)
    return M


print(camera_transform(cubo_points))
