import tkinter as tk
from Cor import Cor

# Constants: Define the initial RGB vector, window title, and window size
VECTOR_RGB = (0.9, 0.3, 0.5)
TITLE = "Cor"
GEOMETRY = "300x300"

def create_input_widget(root, text, initial_value):
    # Function to create an input widget with a label, used for RGB value inputs
    tk.Label(root, text=text).pack(side="top", anchor="center")
    var = tk.StringVar()
    var.set(str(initial_value))
    entry = tk.Entry(root, textvariable=var)
    entry.pack(side="top", anchor="center")
    return entry

def change_color():
    # Function to create a new color object and display its components, called when the "Enter" button is pressed
    red_value = float(red_entry.get())
    green_value = float(green_entry.get())
    blue_value = float(blue_entry.get())

    # Create new color object
    new_color = Cor((red_value, green_value, blue_value), root, TITLE, GEOMETRY)
    # Display RGB and CMYK components of the new color
    new_color.display_rgb_components()
    new_color.display_cmyk_components()

    # Print RGB vector and all components to the console
    print(f"vetor RGB = {new_color.get_vector255()}")
    for component in ['r', 'g', 'b', 'bw_noise', 'c', 'm', 'y', 'k']:
        print(f"{component} = {new_color.get_component(component)}")

if __name__ == "__main__":
    # Main function: set up the root and widgets, then start the Tkinter event loop
    root = tk.Tk()

    tk.Label(root, text="\nEscolha uma nova cor (digite um valor entre 0 e 1)\n").pack(side="top", anchor="center")

    # Create input widgets for red, green, and blue values
    red_entry = create_input_widget(root, "Vermelho (R)", VECTOR_RGB[0])
    green_entry = create_input_widget(root, "Verde (G)", VECTOR_RGB[1])
    blue_entry = create_input_widget(root, "Azul (B)", VECTOR_RGB[2])

    # Create "Enter" button, which calls the change_color function when pressed
    button = tk.Button(root, text=" ENTER ", command=change_color)
    button.pack(side="top", pady=10)

    # Start the Tkinter event loop
    root.mainloop()
