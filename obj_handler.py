def parse_obj_file(filename):
    vertices = []
    faces = []

    for line in open(filename, 'r'):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue

        if values[0] == 'v':
            vertices.append(list(map(float, values[1:4])))
        elif values[0] == 'f':
            face = []
            for v in values[1:]:
                w = v.split('/')
                face.append(int(w[0]) - 1)
            faces.append(face)
    return vertices, faces