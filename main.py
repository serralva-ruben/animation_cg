import tkinter as tk
from Object3D import Object3D
from obj_handler import parse_obj_file
from operations import translate
from math import pi
import numpy as np


window = tk.Tk()
window.title("3D Rotation of Teapot")

# Create a canvas and pack it
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg='#00FFFF')
canvas.pack()

FOV = pi/3
ASPECT_RATIO = canvas_width/canvas_height
near = 0.1
far = 1000

vertices, faces = parse_obj_file('./shapes/teapot.obj')
translated_vertices = translate(vertices, [0,0,-20], FOV, ASPECT_RATIO, near, far)

GEAR_MODEL = './shapes/gears.obj'
GEAR_TEXTURE = './model/hammer/hammerTexture.jpg'
    
gear0 = Object3D(GEAR_MODEL,GEAR_TEXTURE, [10,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,90)
gear1 = Object3D(GEAR_MODEL,GEAR_TEXTURE, [0.6,0.2,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,90)
gear2 = Object3D(GEAR_MODEL,GEAR_TEXTURE, [-8.8,0.85,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)

def render_polygons(polygons, canvas, near, far):
    for vertices, color in polygons:
        # Perform clipping against the near and far planes
        if all((near <= vertex[2] <= far) for vertex in vertices):
            # Calculate the normal vector of the face
            u = np.array([vertices[1][0] - vertices[0][0], vertices[1][1] - vertices[0][1], vertices[1][2] - vertices[0][2]])
            v = np.array([vertices[2][0] - vertices[0][0], vertices[2][1] - vertices[0][1], vertices[2][2] - vertices[0][2]])
            normal = np.cross(u, v)

            # Perform backface culling check
            if normal[2] > 0:
                # Draw the lines of the face
                polygon_coords = [coord for vertex in vertices for coord in vertex[:2]]
                canvas.create_polygon(polygon_coords, fill=color, outline='black')


def animate():
    canvas.delete("all")  # Clear the canvas at the beginning of each frame
    polygons = []
    polygons += gear1.get_animated_polygons(-40)   # Adjust step value as needed
    polygons += gear2.get_animated_polygons(40)   # Adjust step value as needed
    polygons += gear0.get_animated_polygons(40)   # Adjust step value as needed
    # Sort the polygons by the average z value of their vertices
    polygons.sort(key=lambda x: -np.mean([vertex[2] for vertex in x[0]]))
    # Render the polygons
    for polygon in polygons:
        render_polygons([polygon], canvas, near, far)

    canvas.after(int(1000/60), animate)


animate()  # Start the animation
window.mainloop()
