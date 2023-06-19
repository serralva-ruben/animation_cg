def parse_obj_file(filename):
    vertices = []  # Inicializar a lista para armazenar os vértices
    faces = []  # Inicializar a lista para armazenar as faces

    # Abrir o arquivo .obj para leitura
    for line in open(filename, 'r'):
        # Ignorar comentários
        if line.startswith('#'): continue
        # Dividir a linha em valores separados por espaço
        values = line.split()
        # Se a linha estiver vazia, ignorá-la
        if not values: continue

        # Se a linha começar com 'v', então é uma definição de vértice
        if values[0] == 'v':
            # Adicionar os valores de vértice à lista (convertidos para float)
            vertices.append(list(map(float, values[1:4])))
        # Se a linha começar com 'f', então é uma definição de face
        elif values[0] == 'f':
            face = []  # Inicializar a lista para armazenar os índices dos vértices da face
            # Para cada índice de vértice na definição de face
            for v in values[1:]:
                # Os índices podem ser separados por '/', então precisamos dividir novamente
                w = v.split('/')
                # Subtrair 1 dos índices porque o Python indexa a partir de 0, enquanto os arquivos .obj indexam a partir de 1
                face.append(int(w[0]) - 1)
            # Adicionar a face à lista de faces
            faces.append(face)
    # Retornar as listas de vértices e faces
    return vertices, faces
