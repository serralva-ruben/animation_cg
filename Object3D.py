import random
from obj_handler import parse_obj_file
from PIL import Image
import numpy as np
from operations import translate, rotate_around_object_y, scale, rotate_around_object_x, rotate_around_object_z
from math import pi, tan

from utils import apply_perspective_projection

class Object3D:
    def __init__(self, obj_file_path, texture_path, position, fov, aspect_ratio, near, far, canvas_width, canvas_height):
        self.original_vertices, self.faces = parse_obj_file(obj_file_path)
        self.texture_image = Image.open(texture_path)
        self.x, self.y, self.z = position
        print(position)
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.near = near
        self.far = far

        self.canvas_width = canvas_width
        self.canvas_height = canvas_width

        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def start_animation(self, canvas, step):
        self.angle = 0  # Initial rotation angle
        self.animate(canvas, step)

    def animate(self, canvas, step):
        self.angle += step
        self.render(canvas, self.angle)
        canvas.after(int(1000/60), self.animate, canvas, step)

    def render(self, canvas, angle):
        # Clear the current canvas
        canvas.delete("all")
        self.vertices = np.copy(self.original_vertices)
        # Translate, then rotate
        self.vertices = translate(self.vertices, [self.x, self.y, self.z], self.fov, self.aspect_ratio, self.near, self.far)
        angle_in_radians = angle * (pi / 180)
        self.vertices = rotate_around_object_x(self.vertices, angle_in_radians, np.mean(self.vertices, axis=0))
        self.vertices = rotate_around_object_y(self.vertices, 90 * (pi / 180), np.mean(self.vertices, axis=0))
        self.vertices = apply_perspective_projection(self.vertices, self.fov, self.aspect_ratio, self.near, self.far)
        # Convert to screen space coordinates
        screen_vertices = [(x * self.canvas_width/2 + self.canvas_width/2, -y * self.canvas_height/2 + self.canvas_height/2, z) for x, y, z in self.vertices]
        # Draw the faces
        for face in self.faces:
            if len(face) > 3:
                for i in range(1, len(face) - 1):
                    vertices = [screen_vertices[face[0]], screen_vertices[face[i]], screen_vertices[face[i+1]]]
                    self.render_triangle(vertices, canvas, self.near, self.far)
            else:
                vertices = [screen_vertices[i] for i in face]
                self.render_triangle(vertices, canvas, self.near, self.far)

    def render_triangle(self, vertices, canvas, near, far):
        v1, v2, v3 = vertices
        # Perform clipping against the near and far planes
        if v1[2] < near or v2[2] < near or v3[2] < near or v1[2] > far or v2[2] > far or v3[2] > far:
            return

        # Calculate the normal vector of the face
        u = np.array([v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]])
        v = np.array([v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2]])
        normal = np.cross(u, v)

        # Perform backface culling check
        if normal[2] <= 0:
            return

        # Generate random RGB values
        fill_color = '#%02x%02x%02x' % (self.r, self.g, self.b)

        # Draw the lines of the face
        polygon_coords = [v1[0], v1[1], v2[0], v2[1], v3[0], v3[1]]
        canvas.create_polygon(polygon_coords, fill=fill_color)
        canvas.create_line(v1[0], v1[1], v2[0], v2[1])
        canvas.create_line(v2[0], v2[1], v3[0], v3[1])
        canvas.create_line(v3[0], v3[1], v1[0], v1[1])
        #print(f"{v1[0]},{v1[1]},{v2[0]},{v2[1]}")
