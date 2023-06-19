from math import sin, cos, pi
from utils import apply_perspective_projection
from transformation import rotation_x, rotation_y, rotation_z, dilation, translation
import numpy as np

# Aqui vamos rodar os vértices ao redor do eixo y do mundo
def rotate_around_world_y(vertices, angle):
    rotation_matrix = rotation_y(angle)  # Pega a matriz de rotação
    homogeneous_vertices = [np.append(vertex, 1) for vertex in vertices]  # Transforma os vértices para coordenadas homogêneas
    rotated_vertices = [np.dot(rotation_matrix, vertex) for vertex in homogeneous_vertices]  # Aplica a matriz de rotação
    rotated_vertices = [list(vertex[:3]) for vertex in rotated_vertices]  # Volta para coordenadas não homogêneas
    return rotated_vertices

# Agora a gente roda os vértices ao redor do eixo y do objeto
def rotate_around_object_y(vertices, angle):
    center = np.mean(vertices, axis=0)  # Descobre o centro do objeto
    translated_to_origin_vertices = vertices - center  # Translada o objeto para a origem
    homogeneous_vertices = np.array([np.append(vertex, 1) for vertex in translated_to_origin_vertices])  # Transforma os vértices para coordenadas homogêneas
    rotation_matrix = rotation_y(angle)  # Pega a matriz de rotação
    rotated_vertices = np.dot(homogeneous_vertices, rotation_matrix.T)  # Aplica a matriz de rotação
    rotated_vertices = rotated_vertices[:, :3]  # Volta para coordenadas não homogêneas
    repositioned_vertices = rotated_vertices + center  # Reposiciona o objeto
    return repositioned_vertices

# E aqui roda os vértices ao redor do eixo x do objeto
def rotate_around_object_x(vertices, angle):
    center = np.mean(vertices, axis=0)  # Descobre o centro do objeto
    translated_to_origin_vertices = vertices - center  # Translada o objeto para a origem
    homogeneous_vertices = np.array([np.append(vertex, 1) for vertex in translated_to_origin_vertices])  # Transforma os vértices para coordenadas homogêneas
    rotation_matrix = rotation_x(angle)  # Pega a matriz de rotação
    rotated_vertices = np.dot(homogeneous_vertices, rotation_matrix.T)  # Aplica a matriz de rotação
    rotated_vertices = rotated_vertices[:, :3]  # Volta para coordenadas não homogêneas
    repositioned_vertices = rotated_vertices + center  # Reposiciona o objeto
    return repositioned_vertices

# E agora a gente roda os vértices ao redor do eixo z do objeto
def rotate_around_object_z(vertices, angle):
    center = np.mean(vertices, axis=0)  # Descobre o centro do objeto
    translated_to_origin_vertices = vertices - center  # Translada o objeto para a origem
    homogeneous_vertices = np.array([np.append(vertex, 1) for vertex in translated_to_origin_vertices])  # Transforma os vértices para coordenadas homogêneas
    rotation_matrix = rotation_z(angle)  # Pega a matriz de rotação
    rotated_vertices = np.dot(homogeneous_vertices, rotation_matrix.T)  # Aplica a matriz de rotação
    rotated_vertices = rotated_vertices[:, :3]  # Volta para coordenadas não homogêneas
    repositioned_vertices = rotated_vertices + center  # Reposiciona o objeto
    return repositioned_vertices

# Aqui é para escalar os vértices, tipo aumentar ou diminuir o tamanho do objeto
def scale(vertices, scale_vector):
    scale_matrix = dilation(scale_vector)  # Pega a matriz de escala
    homogeneous_vertices = [np.append(vertex, 1) for vertex in vertices]  # Transforma os vértices para coordenadas homogêneas
    scaled_vertices = [np.dot(scale_matrix, vertex) for vertex in homogeneous_vertices]  # Aplica a matriz de escala
    scaled_vertices = [list(vertex[:3]) for vertex in scaled_vertices]  # Volta para coordenadas não homogêneas
    return scaled_vertices

# E por fim, uma função para transladar os vértices, ou seja, mover o objeto para lá e para cá
def translate(vertices, translation_vector):
    translation_matrix = translation(translation_vector)  # Pega a matriz de translação
    homogeneous_vertices = [np.append(vertex, 1) for vertex in vertices]  # Transforma os vértices para coordenadas homogêneas
    translated_vertices = [np.dot(translation_matrix, vertex) for vertex in homogeneous_vertices]  # Aplica a matriz de translação
    translated_vertices = [list(vertex[:3]) for vertex in translated_vertices]  # Volta para coordenadas não homogêneas
    return translated_vertices
