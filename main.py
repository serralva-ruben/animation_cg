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
    
teapot = Object3D('./shapes/teapot.obj','./model/hammer/hammerTexture.jpg', [0,0,20], FOV, ASPECT_RATIO,near, far, canvas_width, canvas_height)
hammer = Object3D('./model/hammer/hammer.obj','./model/hammer/hammerTexture.jpg', [0,0,10], FOV, ASPECT_RATIO,near, far, canvas_width, canvas_height )
gear = Object3D('./shapes/gears.obj','./model/hammer/hammerTexture.jpg', [0,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height)
gear2 = Object3D('./shapes/gears.obj','./model/hammer/hammerTexture.jpg', [-9.5,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height)


def animate():
    canvas.delete("all")  # Clear the canvas at the beginning of each frame
    gear.animate(canvas, 10)
    gear2.animate(canvas, -10)
    canvas.after(int(1000/60), animate)

animate()  # Start the animation
window.mainloop()


window.mainloop()