import tkinter as tk


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def shoelace_algorithm(self, n, points):
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += points[i][0] * points[j][1] - points[i][1] * points[j][0]
        area /= 2
        if area < 0:
            points.reverse()
            area = -area
        return f"The polygon has an area of {area}"

    def liang_barsky_algorithm(self, points, clip_x_min, clip_x_max, clip_y_min, clip_y_max):
        clipped_polygon = []
        n = len(self.matrix[0])
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            dx = x2 - x1
            dy = y2 - y1
            p = [-dx, dx, -dy, dy]
            q = [x1 - clip_x_min, clip_x_max - x1, y1 - clip_y_min, clip_y_max - y1]
            u1 = 0
            u2 = 1
            for j in range(4):
                if p[j] == 0:
                    if q[j] < 0:
                        break
                else:
                    r = q[j] / p[j]
                    if p[j] < 0:
                        u1 = max(u1, r)
                    else:
                        u2 = min(u2, r)
                    if u1 > u2:
                        break
            else:
                x1_clip = x1 + u1 * dx
                y1_clip = y1 + u1 * dy
                x2_clip = x1 + u2 * dx
                y2_clip = y1 + u2 * dy
                if [x1_clip, y1_clip] not in clipped_polygon:
                    clipped_polygon.append([x1_clip, y1_clip])
                if [x2_clip, y2_clip] not in clipped_polygon:
                    clipped_polygon.append([x2_clip, y2_clip])
        return clipped_polygon

    def draw_polygon(self, color, clipped_color, clip_x_min, clip_x_max, clip_y_min, clip_y_max):
        if len(self.matrix) != 2:
            raise ValueError('The matrix needs to have 2 rows')
        n = len(self.matrix[0])
        if len(self.matrix[1]) != n:
            raise ValueError('The matrix needs to have the same number of columns in both rows')

        points = [(self.matrix[0][i], self.matrix[1][i]) for i in range(n)]

        x_min = min(p[0] for p in points)
        x_max = max(p[0] for p in points)
        y_min = min(p[1] for p in points)
        y_max = max(p[1] for p in points)

        window = tk.Tk()
        canvas = tk.Canvas(window, width=600, height=900)
        canvas.pack()

        canvas.create_polygon(points, fill=color)
        canvas.create_rectangle(x_min, y_min, x_max, y_max, outline="black")
        canvas.create_rectangle(clip_x_min, clip_y_min, clip_x_max, clip_y_max, outline="black")

        clipped_polygon = self.liang_barsky_algorithm(points, clip_x_min, clip_x_max, clip_y_min, clip_y_max)

        print("The clipped polygon has", len(clipped_polygon), "points")
        print(clipped_polygon)

        canvas.create_polygon(clipped_polygon, fill=clipped_color, outline='black')

        print("Original:", self.shoelace_algorithm(len(self.matrix[0]), points))
        print("Clipped:", self.shoelace_algorithm(len(clipped_polygon), clipped_polygon))
        window.mainloop()


m = Matrix([[100, 200, 300, 200], [100, 200, 100, 50]])
m.draw_polygon('blue', 'red', 100, 300, 75, 150)
