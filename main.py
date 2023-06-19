import tkinter as tk
from Object3D import Object3D
from obj_handler import parse_obj_file
from operations import translate
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
translated_vertices = translate(vertices, [0,0,-20], FOV, ASPECT_RATIO, near, far)

def animate_rotation(angle):
    angle = 1

    #teapot.render(canvas, canvas_width, canvas_height, near, far, FOV, angle)
    teapot.render(canvas, angle)
    # Perform the rotation and get the new vertices
    #rotated_vertices = rotate(translated_vertices,angle,FOV,ASPECT_RATIO,near, far)
    # Call the render functio
    #render(rotated_vertices, faces, canvas, canvas_width, canvas_height)

    window.after(10, animate_rotation, angle)
    
teapot = Object3D('./shapes/teapot.obj','./model/hammer/hammerTexture.jpg', [0,0,20], FOV, ASPECT_RATIO,near, far, canvas_width, canvas_height)
hammer = Object3D('./model/hammer/hammer.obj','./model/hammer/hammerTexture.jpg', [0,0,10], FOV, ASPECT_RATIO,near, far, canvas_width, canvas_height )
gear = Object3D('./shapes/gears.obj','./model/hammer/hammerTexture.jpg', [0,0,20], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height)

animate_rotation(0)
window.mainloop()