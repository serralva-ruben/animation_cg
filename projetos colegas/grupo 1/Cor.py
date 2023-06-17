import tkinter as tk


class Cor:
    def __init__(self, rgb_v, root, title="Cor", geometry="300x300"):
        # Constructor: Initializes the color object with RGB values, root, title, and geometry
        self.rgb_v = rgb_v
        self.root = root
        self.vector255 = self.rgb_to_255(rgb_v)  # RGB values converted to 0-255 scale

        # Split color into its individual components: black and white noise, and RGB components
        self.bw_noise, self.r, self.g, self.b = self.divide_color(self.rgb_v)
        # Convert RGB values to CMYK color space
        self.c, self.m, self.y, self.k = self.rgb_to_cmyk(self.rgb_v)

        # Set up the root's title and geometry
        self.root.title(title)
        self.root.geometry(geometry)

    def rgb_to_255(self, rgb_v):
        # Convert RGB values to 0-255 scale
        return tuple(int(255 * i) for i in rgb_v)

    def divide_color(self, rgb_v):
        # Split color into its individual RGB components and black and white noise
        min_rgb = min(rgb_v)
        self.bw_noise = (min_rgb, min_rgb, min_rgb)
        self.r = (rgb_v[0] - min_rgb, 0, 0)
        self.g = (0, rgb_v[1] - min_rgb, 0)
        self.b = (0, 0, rgb_v[2] - min_rgb)

    def rgb_to_cmyk(self, rgb_v):
        # Convert RGB values to CMYK color space
        cmy_v = tuple(1 - i for i in rgb_v)
        k = min(cmy_v)

        if k == 1:
            return 0, 0, 0, 1
        else:
            c, m, y = ((i - k) / (1 - k) for i in cmy_v)
            return c, m, y, k

    def get_vector255(self):
        # Getter: Returns RGB values converted to 0-255 scale
        return self.vector255

    def get_component(self, component):
        # Getter: Returns a specific color component based on the provided key
        components = {
            "r": self.r,
            "g": self.g,
            "b": self.b,
            "bw_noise": self.bw_noise,
            "c": self.c,
            "m": self.m,
            "y": self.y,
            "k": self.k
        }
        return components.get(component, "Component not found")
