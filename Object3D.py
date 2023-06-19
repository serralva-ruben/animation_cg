import random
import time
from obj_handler import parse_obj_file
import numpy as np
from operations import translate, rotate_around_object_y, scale, rotate_around_object_x, rotate_around_object_z
from math import pi, tan

from utils import apply_perspective_projection

class Object3D:
    def __init__(self, obj_file_path, position, fov, aspect_ratio, near, far, canvas_width, canvas_height, start_angle):
        # Carregar vértices e faces do arquivo .obj
        self.original_vertices, self.faces = parse_obj_file(obj_file_path)
        # Definir a posição inicial do objeto 3D
        self.x, self.y, self.z = position
        # Definir os parâmetros da projeção de perspectiva
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.near = near
        self.far = far
        # Definir o ângulo inicial de rotação do objeto
        self.angle = start_angle
        # Definir a largura e altura do canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_width
        # Inicializar os parâmetros para a mudança de cor
        self.last_color_change = time.time()
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def get_animated_polygons(self, step):
        # Atualizar o ângulo de rotação
        self.angle += step
        # Copiar os vértices originais para transformação
        self.vertices = np.copy(self.original_vertices)
        # Mover os vértices para a posição do objeto
        self.vertices = translate(self.vertices, [self.x, self.y, self.z])
        # Aplicar rotações em torno dos eixos
        self.vertices = rotate_around_object_y(self.vertices, 90 * (pi / 180))
        self.vertices = rotate_around_object_z(self.vertices, self.angle * (pi / 180))
        # Aplicar projeção de perspectiva nos vértices
        self.vertices = apply_perspective_projection(self.vertices, self.fov, self.aspect_ratio, self.near, self.far)
        # Mapear vértices para as coordenadas da tela
        screen_vertices = [(x * self.canvas_width/2 + self.canvas_width/2, -y * self.canvas_height/2 + self.canvas_height/2, z) for x, y, z in self.vertices]

        # Inicializar a lista para armazenar polígonos
        polygons = []
        # Converter as cores RGB para o formato hexadecimal
        fill_color = '#%02x%02x%02x' % (self.r, self.g, self.b)

          # Para cada face, gerar os polígonos correspondentes
        for face in self.faces:
            if len(face) > 3:  # Se a face tem mais de 3 vértices, geramos múltiplos triângulos
                for i in range(1, len(face) - 1):
                    vertices = [screen_vertices[face[0]], screen_vertices[face[i]], screen_vertices[face[i+1]]]
                    polygons.append((vertices, fill_color))
            else:  # Caso contrário, geramos um único polígono para a face
                vertices = [screen_vertices[i] for i in face]
                polygons.append((vertices, fill_color))
        # Retorna a lista de polígonos para renderização
        return polygons  