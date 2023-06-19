import numpy as np
import math
from math import cos, sin

def translation(v):
    # Esta função cria uma matriz de translação com base num vetor de translação v.
    # 'v' é uma lista ou array de valores representando a translação em cada dimensão.
    size = len(v)
    value = np.eye(size + 1)
    value[:-1, -1] = v
    return value

def dilation(v):
    # Esta função cria uma matriz de dilatação com base num vetor de dilatação v.
    # 'v' é uma lista ou array de valores representando a dilatação em cada dimensão.
    size = len(v)
    value = np.eye(size + 1)
    value[:-1, :-1] = np.diag(v)
    return value

def rotation_x(angle):
    # Esta função cria uma matriz de rotação em torno do eixo X com base num ângulo fornecido.
    # 'angle' é o ângulo de rotação em graus.
    angle = np.radians(angle)
    value = np.array([[1, 0, 0, 0],
                      [0, np.cos(angle), -np.sin(angle), 0],
                      [0, np.sin(angle), np.cos(angle), 0],
                      [0, 0, 0, 1]])
    return value

def rotation_y(angle):
    # Esta função cria uma matriz de rotação em torno do eixo Y com base num ângulo fornecido.
    # 'angle' é o ângulo de rotação em graus.
    return np.array([[cos(angle), 0, sin(angle), 0],
                     [0, 1, 0, 0],
                     [-sin(angle), 0, cos(angle), 0],
                     [0, 0, 0, 1]])

def rotation_z(angle):
    # Esta função cria uma matriz de rotação em torno do eixo Z com base num ângulo fornecido.
    # 'angle' é o ângulo de rotação em graus.
    angle = np.radians(angle)
    value = np.array([[np.cos(angle), -np.sin(angle), 0, 0],
                      [np.sin(angle), np.cos(angle), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
    return value
