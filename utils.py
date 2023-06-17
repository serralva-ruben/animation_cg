from math import tan

def apply_perspective_projection(rotated_vertices, fov, aspect_ratio, near, far):
    proj_matrix = [
        [aspect_ratio * (1/tan(fov/2)), 0, 0, 0],
        [0, 1 / tan(fov/2), 0, 0],
        [0, 0, -(far + near) / (far - near), -2*far*near / (far - near)],
        [0, 0, -1, 0]
    ]

    projected_vertices = []
    
    for vertex in rotated_vertices:
        x, y, z = vertex
        vertex_4d = [x, y, z, 1]
        vertex_proj = [sum([vertex_4d[i]*proj_matrix[j][i] for i in range(4)]) for j in range(4)]

        if vertex_proj[3] != 0:
            vertex_proj = [i / vertex_proj[3] for i in vertex_proj[:-1]]
        else:
            vertex_proj = vertex_proj[:-1]

        projected_vertices.append(vertex_proj)

    return projected_vertices
