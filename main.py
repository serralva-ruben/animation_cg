import tkinter as tk
from obj_handler import parse_obj_file
from operations import rotate_y, translate
from math import pi
window = tk.Tk()
window.title("3D Rotation of Teapot")

# Create a canvas and pack it
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

FOV = pi/3
ASPECT_RATIO = canvas_width/canvas_height
near = 0.1
far = 1000

vertices, faces = parse_obj_file('./shapes/teapot.obj')

def render(vertices, faces, canvas, canvas_width, canvas_height):
    # Clear the current canvas
    canvas.delete("all")

    # Scale and translate the coordinates to the canvas system
    projected_vertices = [(x * canvas_width/2 + canvas_width/2, -y * canvas_height/2 + canvas_height/2) for x, y, _ in vertices]

    # Draw the new vertices on the canvas
    for face in faces:
        for i in range(len(face)):
            x1, y1 = projected_vertices[face[i - 1]]
            x2, y2 = projected_vertices[face[i]]
            # Draw the line
            canvas.create_line(x1, y1, x2, y2)


def animate_rotation(angle):
    angle += 10
    
    # Perform the rotation and get the new vertices
    rotated_vertices = rotate_y(vertices, angle, FOV, ASPECT_RATIO, near, far)
    translated_vertices = translate(rotated_vertices, [0,0,-100], FOV, ASPECT_RATIO, near, far)
    # Call the render functio
    render(translated_vertices, faces, canvas, canvas_width, canvas_height)

    window.after(10, animate_rotation, angle)


animate_rotation(0)
window.mainloop()