import tkinter as tk
import numpy as np
import copy

def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"

def process_octants(p1, p2, dx, dy, dz):
    p1_copy, p2_copy = copy.deepcopy(p1), copy.deepcopy(p2)
    dx, dy, dz = abs(dx), abs(dy), abs(dz)
    
    if dx < 0:
        p1_copy[0], p2_copy[0] = p2_copy[0], p1_copy[0]
        dx, dy, dz = -dx, -dy, -dz
    if dy < 0:
        p1_copy[1], p2_copy[1] = p2_copy[1], p1_copy[1]
        dy = -dy
    if dz < 0:
        p1_copy[2], p2_copy[2] = p2_copy[2], p1_copy[2]
        dz = -dz
    return p1_copy, p2_copy, dx, dy, dz

def bresenham3D(endpoints):
    pixel_coords = []

    for i in endpoints:
        i[0], i[1], dx, dy, dz = process_octants(i[0], i[1], abs(i[1][0] - i[0][0]), abs(i[1][1] - i[0][1]), abs(i[1][2] - i[0][2]))
        x1, y1, z1 = i[0]
        x2, y2, z2 = i[1]

        x_step, y_step, z_step = np.sign(x2 - x1), np.sign(y2 - y1), np.sign(z2 - z1)
        x, y, z = x1, y1, z1

        if dx >= dy and dx >= dz:
            p1, p2 = 2 * dy - dx, 2 * dz - dx
            while x != x2:
                x += x_step
                y += (p1 >= 0) * y_step
                z += (p2 >= 0) * z_step
                p1, p2 = p1 + 2 * dy - 2 * dx * (p1 >= 0), p2 + 2 * dz - 2 * dx * (p2 >= 0)
                pixel_coords.append((x, y, z))

        elif dy >= dx and dy >= dz:
            p1, p2 = 2 * dx - dy, 2 * dz - dy
            while y != y2:
                y += y_step
                x += (p1 >= 0) * x_step
                z += (p2 >= 0) * z_step
                p1, p2 = p1 + 2 * dx - 2 * dy * (p1 >= 0), p2 + 2 * dz - 2 * dy * (p2 >= 0)
                pixel_coords.append((x, y, z))

        else:
            p1, p2 = 2 * dy - dz, 2 * dx - dz
            while z != z2:
                z += z_step
                y += (p1 >= 0) * y_step
                x += (p2 >= 0) * x_step
                p1, p2 = p1 + 2 * dy - 2 * dz * (p1 >= 0), p2 + 2 * dx - 2 * dz * (p2 >= 0)
                pixel_coords.append((x, y, z))
    return pixel_coords

def generate_vertex_pairs(vertices, faces):
    pairs = [[vertices[i], vertices[j]] for face in faces for i, j in zip(face, face[1:] + [face[0]])]
    return pairs

def draw(canvas, vertices, faces, color):
    pairs = generate_vertex_pairs(vertices, faces)
    pixels = bresenham3D(pairs)
    for pixel in pixels:
        x, y, _ = pixel
        canvas.create_line(x, y, x+1, y+1, fill=rgb_to_hex(color))

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=900, height=600)
    canvas.pack()

    vertices = [[310, 210, 1], [450, 210, 1], [450, 350, 1], [310, 350, 1], [360, 260, 1], [500, 260, 1], [500, 400, 1], [360, 400, 1]]
    faces = [[0, 1, 2, 3], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7], [4, 5, 6, 7]]

    draw(canvas, vertices, faces, (0, 0, 255))
    root.mainloop()
