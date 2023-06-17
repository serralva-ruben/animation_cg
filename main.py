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
ASPECT_RATIO = canvas_height/canvas_width
near = 0.1
far = 1000

vertices, faces = parse_obj_file('./shapes/teapot.obj')
translated_vertices = translate(vertices, [0,0,-20], FOV, ASPECT_RATIO, near, far)


def render(vertices, faces, canvas, canvas_width, canvas_height, near, far):
    # Clear the current canvas
    canvas.delete("all")

    # Scale and translate the coordinates to the canvas system
    projected_vertices = [(x * canvas_width/2 + canvas_width/2, -y * canvas_height/2 + canvas_height/2, z) for x, y, z in vertices]

    # Draw the new vertices on the canvas
    for face in faces:
        # Get the vertices of the current face
        v1, v2, v3 = [projected_vertices[i] for i in face]

        # Perform clipping against the near and far planes
        if v1[2] < near or v2[2] < near or v3[2] < near or v1[2] > far or v2[2] > far or v3[2] > far:
            continue

        # Calculate the normal vector of the face
        normal = (v2[0] - v1[0]) * (v3[1] - v1[1]) - (v2[1] - v1[1]) * (v3[0] - v1[0])

        # Perform backface culling check
        if normal <= 0:
            continue

        # Draw the lines of the face
        for i in range(len(face)):
            x1, y1, _ = projected_vertices[face[i - 1]]
            x2, y2, _ = projected_vertices[face[i]]
            # Draw the line
            canvas.create_line(x1, y1, x2, y2)





def animate_rotation(angle):
    angle += 1
    
    # Perform the rotation and get the new vertices
    rotated_vertices = rotate_y(translated_vertices,angle,FOV,ASPECT_RATIO,near, far)
    # Call the render functio
    render(rotated_vertices , faces, canvas, canvas_width, canvas_height, near, far)

    window.after(10, animate_rotation, angle)


animate_rotation(0)
window.mainloop()