import random
import time
from obj_handler import parse_obj_file
from PIL import Image
import numpy as np
from operations import translate, rotate_around_object_y, scale, rotate_around_object_x, rotate_around_object_z
from math import pi, tan

from utils import apply_perspective_projection

class Object3D:
    def __init__(self, obj_file_path, texture_path, position, fov, aspect_ratio, near, far, canvas_width, canvas_height, start_angle):
        self.original_vertices, self.faces = parse_obj_file(obj_file_path)
        self.texture_image = Image.open(texture_path)
        self.x, self.y, self.z = position
        print(position)
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.near = near
        self.far = far
        self.angle = start_angle
        self.canvas_width = canvas_width
        self.canvas_height = canvas_width
        self.last_color_change = time.time()
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

        self.xstep = 0

    def get_animated_polygons(self, step):
        self.angle += step
        self.xstep += 50
        self.vertices = np.copy(self.original_vertices)
        self.vertices = translate(self.vertices, [self.x, self.y, self.z], self.fov, self.aspect_ratio, self.near, self.far)
        # Convert the self.angle to radians and use it for the y-rotation
        angle_in_radians = self.angle * (pi / 180)

        self.vertices = rotate_around_object_y(self.vertices, 90 * (pi / 180), np.mean(self.vertices, axis=0))
        self.vertices = rotate_around_object_z(self.vertices, self.angle * (pi / 180), np.mean(self.vertices, axis=0))
        self.vertices = rotate_around_object_x(self.vertices, 0 * (pi / 180), np.mean(self.vertices, axis=0))

        self.vertices = apply_perspective_projection(self.vertices, self.fov, self.aspect_ratio, self.near, self.far)
        screen_vertices = [(x * self.canvas_width/2 + self.canvas_width/2, -y * self.canvas_height/2 + self.canvas_height/2, z) for x, y, z in self.vertices]

        polygons = []
        fill_color = '#%02x%02x%02x' % (self.r, self.g, self.b)

        for face in self.faces:
            if len(face) > 3:
                for i in range(1, len(face) - 1):
                    vertices = [screen_vertices[face[0]], screen_vertices[face[i]], screen_vertices[face[i+1]]]
                    polygons.append((vertices, fill_color))
            else:
                vertices = [screen_vertices[i] for i in face]
                polygons.append((vertices, fill_color))
        return polygons