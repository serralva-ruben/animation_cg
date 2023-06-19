import tkinter as tk
from Object3D import Object3D
from obj_handler import parse_obj_file
from operations import translate
from math import pi
import numpy as np

# Criando a janela
window = tk.Tk()
window.title("3D Rotation of Gears")

# Crie um canvas e o coloque na janela
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg='#1E555C')
canvas.pack()

# Configurações de perspectiva
FOV = pi/3
ASPECT_RATIO = canvas_width/canvas_height
near = 0.1
far = 1000

# Carregando os modelos das engrenagens
GEAR_MODEL = './shapes/gearL.obj'
GEAR_MODEL1 = './shapes/gear.obj'

# Criando as engrenagens
gear0 = Object3D(GEAR_MODEL, [4.6*5,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gear1 = Object3D(GEAR_MODEL, [4.6*4,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gear2 = Object3D(GEAR_MODEL, [4.6*3,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gear3 = Object3D(GEAR_MODEL, [4.6*2,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gear4 = Object3D(GEAR_MODEL, [4.6,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gear5 = Object3D(GEAR_MODEL, [0,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gear6 = Object3D(GEAR_MODEL, [-4.6,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gear7 = Object3D(GEAR_MODEL, [-4.6*2,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gear8 = Object3D(GEAR_MODEL, [-4.6*3,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gear9 = Object3D(GEAR_MODEL, [-4.6*4,0,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gearB0 = Object3D(GEAR_MODEL1, [-2*9.4,-14.2,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gearB1 = Object3D(GEAR_MODEL1, [-9.4,-14.5,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gearB2 = Object3D(GEAR_MODEL1, [0,-14.9,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gearB3 = Object3D(GEAR_MODEL1, [9.4,-15.4,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)
gearB4 = Object3D(GEAR_MODEL1, [9.4*2,-16,40], FOV, ASPECT_RATIO,near, far , canvas_width, canvas_height,0)

# Centro da tela
center_x, center_y = canvas_width / 2, canvas_height / 2  # Screen center

# Função para calcular a distância ao centro
def distance_to_center(vertex):
    dx = center_x - vertex[0]
    dy = center_y - vertex[1]
    return dx*dx + dy*dy

# Função para renderizar os polígonos
def render_polygons(polygons, canvas, near, far):
    for vertices, color in polygons:
        # Fazendo o clipping contra os planos near e far
        if all((near <= vertex[2] <= far) for vertex in vertices):
            # Calculando o vetor normal da face
            u = np.array([vertices[1][0] - vertices[0][0], vertices[1][1] - vertices[0][1], vertices[1][2] - vertices[0][2]])
            v = np.array([vertices[2][0] - vertices[0][0], vertices[2][1] - vertices[0][1], vertices[2][2] - vertices[0][2]])
            normal = np.cross(u, v)

            # Checando se a face está virada para trás
            if normal[2] > 0:
                # Desenhando as linhas da face
                polygon_coords = [coord for vertex in vertices for coord in vertex[:2]]
                canvas.create_polygon(polygon_coords, fill=color, outline='black')
                
# Função para animar as engrenagens
def animate():
    # Limpar o canvas no início de cada frame
    canvas.delete("all")
    polygons = []

    speed = 90

    # Gerando os polígonos para cada engrenagem
    polygons += gear0.get_animated_polygons(speed)
    polygons += gear1.get_animated_polygons(-speed)
    polygons += gear2.get_animated_polygons(speed)
    polygons += gear3.get_animated_polygons(-speed)
    polygons += gear4.get_animated_polygons(speed)
    polygons += gear5.get_animated_polygons(-speed)
    polygons += gear6.get_animated_polygons(speed)
    polygons += gear7.get_animated_polygons(-speed)
    polygons += gear8.get_animated_polygons(speed)
    polygons += gear9.get_animated_polygons(-speed)
    polygons += gearB0.get_animated_polygons(-speed)
    polygons += gearB1.get_animated_polygons(speed)
    polygons += gearB2.get_animated_polygons(-speed)
    polygons += gearB3.get_animated_polygons(speed)
    polygons += gearB4.get_animated_polygons(-speed)

    # Ordenar os polígonos pela média da distância quadrada de seus vértices até o centro da tela
    polygons.sort(key=lambda x: -np.mean([distance_to_center(vertex) for vertex in x[0]]))

    # Renderizar os polígonos
    for polygon in polygons:
        render_polygons([polygon], canvas, near, far)

    # Chamando a função animate novamente após uma pausa
    canvas.after(int(1000/60), animate)

# Iniciar a animação
animate()
# Iniciar o loop principal da janela
window.mainloop()
