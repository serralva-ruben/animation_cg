import tkinter as tk


class Matrix:
    def __init__(self, data: list) -> None:
        self.data = data

    def project(self, d: int, width: int, height: int) -> list:
        projected_points = []

        for i in range(len(self.data[0])):
            x, y, z = self.data[0][i], self.data[1][i], self.data[2][i]
            xp = -d * x / z
            yp = -d * y / z
            projected_points.append((xp, yp))

        min_x, min_y = min(x for x, y in projected_points), min(y for x, y in projected_points)
        max_x, max_y = max(x for x, y in projected_points), max(y for x, y in projected_points)

        margin = 10
        scale_x = (width - 2 * margin) / (max_x - min_x)
        scale_y = (height - 2 * margin) / (max_y - min_y)

        resized_points = [(int(margin + (x - min_x) * scale_x), int(margin + (y - min_y) * scale_y)) for x, y in projected_points]

        return resized_points


def draw_polygon(canvas: tk.Canvas, points: list) -> None:
    canvas.create_polygon(points, fill="", outline="black", width=2)

# Create a matrix with data points
data = [[-100, 0, 100], [-50, 50, -50], [100, 100, 100]]
matrix = Matrix(data)

# Create the main window
root = tk.Tk()
root.geometry('600x900')

# Create a canvas in the window
canvas = tk.Canvas(root, width=600, height=900, bg='white')
canvas.pack()

# Project the matrix points onto a 2D plane
projected_points = matrix.project(200, 600, 900)

# Draw the polygon with the projected points on the canvas
draw_polygon(canvas, projected_points)

# Start the main tkinter event loop
root.mainloop()
