from math import tan

def apply_perspective_projection(rotated_vertices, fov, aspect_ratio, near, far):
    # Esta função aplica a projeção perspectiva a vértices rotacionados.
    # 'rotated_vertices' são os vértices após as transformações de rotação.
    # 'fov' é o campo de visão em radianos.
    # 'aspect_ratio' é a razão entre a largura e a altura da tela.
    # 'near' e 'far' são os planos de corte da câmera, representando as distâncias mínima e máxima, respectivamente, que a câmera pode ver.

    # Cria a matriz de projeção perspectiva.
    proj_matrix = [
        [aspect_ratio * (1/tan(fov/2)), 0, 0, 0],
        [0, 1 / tan(fov/2), 0, 0],
        [0, 0, -(far + near) / (far - near), -2*far*near / (far - near)],
        [0, 0, -1, 0]
    ]

    projected_vertices = []
    
    for vertex in rotated_vertices:
        x, y, z = vertex
        # Converte o vértice para coordenadas homogêneas.
        vertex_4d = [x, y, z, 1]
        # Aplica a matriz de projeção ao vértice.
        vertex_proj = [sum([vertex_4d[i]*proj_matrix[j][i] for i in range(4)]) for j in range(4)]

        # Converte de volta para coordenadas 3D se o valor de w (vertex_proj[3]) for diferente de 0.
        if vertex_proj[3] != 0:
            vertex_proj = [i / vertex_proj[3] for i in vertex_proj[:-1]]
        else:
            vertex_proj = vertex_proj[:-1]

        projected_vertices.append(vertex_proj)

    return projected_vertices
