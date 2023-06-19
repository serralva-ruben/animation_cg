from math import sin, cos, pi
from utils import apply_perspective_projection
from transformation import rotation_x, rotation_y, rotation_z, dilation, translation
import numpy as np

def rotate_around_world_y(vertices, angle, fov, aspect_ratio, near, far):
    rotation_matrix = rotation_y(angle)
    homogeneous_vertices = [np.append(vertex, 1) for vertex in vertices]
    rotated_vertices = [np.dot(rotation_matrix, vertex) for vertex in homogeneous_vertices]
    rotated_vertices = [list(vertex[:3]) for vertex in rotated_vertices]
    return apply_perspective_projection(rotated_vertices, fov, aspect_ratio, near, far)

def rotate_around_object_y(vertices, angle, position):
    # Determine the geometric center of the object
    center = np.mean(vertices, axis=0)

    # Translate the object so its center is at the world's origin
    translated_to_origin_vertices = vertices - center

    # Add the homogeneous coordinate to each vertex
    homogeneous_vertices = np.array([np.append(vertex, 1) for vertex in translated_to_origin_vertices])

    # Rotate the object around its local origin (center)
    rotation_matrix = rotation_y(angle)
    rotated_vertices = np.dot(homogeneous_vertices, rotation_matrix.T)

    # Remove the homogeneous coordinate
    rotated_vertices = rotated_vertices[:, :3]

    # Translate the object back to its original position
    repositioned_vertices = rotated_vertices + center

    return repositioned_vertices



def scale(vertices, scale_vector, fov, aspect_ratio, near, far):
    scale_matrix = dilation(scale_vector)
    homogeneous_vertices = [np.append(vertex, 1) for vertex in vertices]
    scaled_vertices = [np.dot(scale_matrix, vertex) for vertex in homogeneous_vertices]
    scaled_vertices = [list(vertex[:3]) for vertex in scaled_vertices]
    return apply_perspective_projection(scaled_vertices, fov, aspect_ratio, near, far)

def translate(vertices, translation_vector, fov, aspect_ratio, near, far):
    translation_matrix = translation(translation_vector)
    homogeneous_vertices = [np.append(vertex, 1) for vertex in vertices]
    
    translated_vertices = [np.dot(translation_matrix, vertex) for vertex in homogeneous_vertices]
    translated_vertices = [list(vertex[:3]) for vertex in translated_vertices]
    return apply_perspective_projection(translated_vertices, fov, aspect_ratio, near, far)
