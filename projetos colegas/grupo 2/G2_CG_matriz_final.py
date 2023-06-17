import math

# Constantes usadas na classe e função menu.
BLACK = "\033[0m"

RED = "\033[31m"

C = RED + "\nEnter para continuar"

GRAUS_ = "\nIndique o ângulo de rotação em graus: "

S = RED + "A matriz não é uma matriz de transformação."


class Matriz:

    def __init__(self, value_list):
        # verifique se a valueList é não vazio com um promeiro elemento não vazio
        if type(value_list) != list or len(value_list) < 1 or type(value_list[0]) != list or len(value_list[0]) < 1:
            # Quando não é devolve uma matriz vazia
            self.value = [[]]
            return
            # verifica se os restantes elementos tenham o mesmo tamanho que o primeiro
        for i in range(len(value_list)):
            if type(value_list[i]) != list or len(value_list[i]) != len(value_list[0]):
                # Quando não é devolve uma matriz vazia
                self.value = [[]]
                return

        # Sendo uma matriz válida podemos copiar os valores de entrada para a matriz atual
        self.value = []
        for i in range(len(value_list)):
            line = []
            for j in range(len(value_list[0])):
                line.append(value_list[i][j])
            self.value.append(line)


    def show_matrix(self):
        # Apresenta no ecrã todos os valores da matriz linha-a-linha
        for i in range(len(self.value)):
            print(self.value[i])

    def dim(self):
        #Dimensão da matriz
        if len(self.value) <= 0 or len(self.value[0]) <= 0: return 0,0
        return len(self.value), len(self.value[0])

    def get_value(self, line, column):
        return self.value[line][column]

    def __add__(self, b):
        # Verifique se ambas as matrizes têm o mesmo formato
        if len(self.value) != len(b.value) or len(self.value[0]) != len(b.value[0]):
            return Matriz([[]])  # Não tem o mesmo formato → retourno é a matriz vázia
        else:
            r = []  # Defina a lista externa do resultado

        # Definição da dimensão de ambas as matrizes
        lin = len(self.value)  # O númbero das linhas
        col = len(self.value[0])  # O númbero das colunas

        # Calucula a soma
        for i in range(lin):  # passa todas as linhas de A respetivamente de B
            val = []  # cria uma linha para a matriz resultando
            for j in range(col):  # passa todas as colunas de A respetivamente de B
                val.append(
                    self.value[i][j] + b.value[i][j])  # insere em cada coluna a soma dos elementos da mesma
            r.append(val)  # insere a linha na matriz resultando

        return Matriz(r)  # Retorna o resultado


    def get_matriz(self):
        """
        Função que retorna os valores da matriz, para ser usado em outros contextos

        :return: a matriz
        """
        return self.value

    def get_transposta(self):
        """
        Retorna uma matriz, onde as linhas são as colunas da matriz dada

        :return: a transposta da matriz dada
        """
        numero_linhas = len(self.value)
        numero_colunas = len(self.value[0])
        nova_matriz = []
        for coluna in range(numero_colunas):
            col = []
            for linha in range(numero_linhas):
                col.append(self.value[linha][coluna])
            nova_matriz.append(col)

        return Matriz(nova_matriz)

    def __mul__(self, matriz2):
        """
        Faz a multiplicação de duas matrizes

        :param matriz2: segunda matriz para fazer a multiplicação
        :return: Matriz resultante da multiplicação das duas primeiras
        """

        # linhas = len(self.value)
        # colunas = len(self.value[0])
        # cria a transposta da segunda matriz
        matriz2: Matriz = matriz2.get_transposta()

        linhas_matriz1 = len(self.value)
        colunas_matriz1 = len(self.value[0])

        colunas_matriz2 = len(matriz2.value)
        linhas_matriz2 = len(matriz2.value[0])

        if linhas_matriz1 == colunas_matriz2 or colunas_matriz1 == linhas_matriz2:
            r = []
            # itera sobre as linhas da primeira matriz
            for linha_m1 in range(linhas_matriz1):
                mult = []
                # itera sobre as linhas da transposta da segunda matriz
                for linha_m2 in range(colunas_matriz2):
                    soma = 0
                    # itera sobre o número de colunas das matrizes (como é igual em ambas, não importa qual é a matriz)
                    for coluna in range(colunas_matriz1):
                        # faz a multiplicação
                        soma = soma + self.value[linha_m1][coluna] * matriz2.value[linha_m2][coluna]
                    # faz append da soma à lista mult
                    mult.append(soma)
                r.append(mult)

            return Matriz(r)
        else:
            return Matriz([[]])

    def mul_escalar(self, escalar):
        """
        Faz a multiplicação escalar entre uma matriz e um valor real

        :param escalar: Valor real para realizar a multiplicação escalar
        :return: Matriz resultante da multiplicação escalar entre uma matriz e um valor real
        """
        linhas = len(self.value)
        resultado = []
        for i in range(linhas):
            linha = [escalar * x for x in self.value[i]]
            resultado.append(linha)
        return Matriz(resultado)

    def canonica_para_homogeneas(self):
        """
        Converte uma matriz canônica numa matriz homogênea.

        :return: Uma nova matriz homogênea criada a partir da matriz canônica atual.
        :rtype: Matriz
        """
        linhas = len(self.value)
        colunas = len(self.value[0])
        homogeneas = []
        for i in range(linhas):
            linha = self.value[i] + [0]
            homogeneas.append(linha)
        homogeneas.append([0] * colunas + [1])
        return Matriz(homogeneas)

    def homogeneas_para_canonica(self):
        """
        Converte uma matriz homogênea numa matriz canônica.

        :return: Uma nova matriz canônica criada a partir da matriz homogênea atual.
        :rtype: Matriz
        """
        linhas = len(self.value)
        colunas = len(self.value[0])
        canonicas = []
        for i in range(linhas - 1):
            linha = self.value[i][:(colunas-1)]
            canonicas.append(linha)
        return Matriz(canonicas)

    def translacao(self, vetor):
        """
        Realiza uma transformação de translação na matriz atual.

        :param vetor: O vetor de translação, dado por uma lista de três valores numéricos.
        :type vetor: list

        :return: A nova matriz transformada pela translação.
        :rtype: Matriz
        """
        mx = self.canonica_para_homogeneas()
        linhas = len(mx.value)
        colunas = len(mx.value[0])
        if linhas != 4 or colunas != 4:
            print(S)
            input(C)
        translacao = Matriz([
            [1, 0, 0, vetor[0]],
            [0, 1, 0, vetor[1]],
            [0, 0, 1, vetor[2]],
            [0, 0, 0, 1]
        ])

        resultado = translacao.__mul__(mx)
        return resultado

    def dilatar(self, escala):
        """
        Realiza uma transformação de dilatação na matriz atual.

        :param escala: O vetor de escala, dado por uma lista de três valores numéricos.
        :type escala: list

        :return: A nova matriz transformada pela dilatação.
        :rtype: Matriz
        """
        mx = self.canonica_para_homogeneas()
        linhas = len(mx.value)
        colunas = len(mx.value[0])
        if linhas != 4 or colunas != 4:
            print(S)
            input(C)
        dilatacao = Matriz([
        [escala[0], 0, 0, 0],
        [0, escala[1], 0, 0],
        [0, 0, escala[2], 0],
        [0, 0, 0, 1]
        ])

        resultado = mx.__mul__(dilatacao)
        return resultado.homogeneas_para_canonica()

    def rotacao_x(self, angulo):
        """
        Retorna a matriz resultante da rotação em torno do eixo X com o ângulo especificado.

        :param angulo: ângulo de rotação em graus
        :return: matriz resultante da rotação em torno do eixo X
        """
        mx = self.canonica_para_homogeneas()
        rad = math.radians(angulo)
        c = math.cos(rad)
        s = math.sin(rad)

        rotacao_x = Matriz([
            [1, 0, 0, 0],
            [0, c, s, 0],
            [0, -s, c, 0],
            [0, 0, 0, 1]
        ])

        return rotacao_x * mx * rotacao_x.get_transposta()

    def rotacao_y(self, angulo):
        """
        Retorna a matriz resultante da rotação em torno do eixo Y com o ângulo especificado.

        :param angulo: ângulo de rotação em graus
        :return: matriz resultante da rotação em torno do eixo Y
        """
        mx = self.canonica_para_homogeneas()
        rad = math.radians(angulo)
        c = math.cos(rad)
        s = math.sin(rad)

        rotacao_y = Matriz([
            [c, 0, -s, 0],
            [0, 1,  0, 0],
            [s, 0,  c, 0],
            [0, 0,  0, 1]
        ])

        return rotacao_y * mx * rotacao_y.get_transposta()

    def rotacao_z(self, angulo):
        """
        Retorna a matriz resultante da rotação em torno do eixo Z com o ângulo especificado.

        :param angulo: ângulo de rotação em graus
        :return: matriz resultante da rotação em torno do eixo Z
        """
        mx = self.canonica_para_homogeneas()
        rad = math.radians(angulo)
        c = math.cos(rad)
        s = math.sin(rad)

        rotacao_z = Matriz([
            [c,  s, 0, 0],
            [-s, c, 0, 0],
            [0,  0, 1, 0],
            [0,  0, 0, 1]
        ])

        return rotacao_z * mx * rotacao_z.get_transposta()


def menu_matriz():
    matriz = Matriz([[]])

    while True:
        print("\n" + RED + "Menu de Operações de Matrizes" + BLACK)
        print("\nEscolha uma opção:\n")
        print("1 - Definir uma nova matriz")
        print("2 - Apresentar a matriz atual")
        print("3 - Somar a matriz atual com outra matriz")
        print("4 - Multiplicar a matriz atual com outra matriz")
        print("5 - Multiplicação escalar da matriz atual")
        print("6 - Translação da matriz atual através de um vetor 3D")
        print("7 - Dilatar a matriz atual segundo um vetor 3D")
        print("8 - Rotação da matriz atual segundo um dos eixos XYZ")
        print("H - Passagem da representação canónica para coordenadas homogéneas (matriz atual)")
        print("0 - Sair")

        opcao = input(RED+"\nDigite a opção desejada: "+BLACK)

        if opcao == "1":
            print("\nDigite os valores da matriz, separados por espaço e linha por linha:")
            valores = []
            linha = input().split()
            while linha:
                valores.append([int(x) for x in linha])
                linha = input().split()
            matriz = Matriz(valores)

        elif opcao == "2":
            print(RED+"\nMatriz atual:"+BLACK)
            matriz.show_matrix()
            input(C)

        elif opcao == "3":
            print("\nDigite os valores da segunda matriz, separados por espaço e linha por linha:")
            valores = []
            linha = input().split()
            while linha:
                valores.append([int(x) for x in linha])
                linha = input().split()
            matriz2 = Matriz(valores)

            matriz_soma = matriz.__add__(matriz2)

            print(RED+"\nResultado da soma:"+BLACK)
            matriz_soma.show_matrix()
            input(C)

        elif opcao == "4":
            print("\nDigite os valores da segunda matriz, separados por espaço e linha por linha:")
            valores = []
            linha = input().split()
            while linha:
                valores.append([int(x) for x in linha])
                linha = input().split()
            matriz2 = Matriz(valores)

            matriz_mult = matriz.__mul__(matriz2)

            print(RED+"\nResultado da multiplicação:"+BLACK)
            matriz_mult.show_matrix()
            input(C)

        elif opcao == "5":
            print("\nDigite o valor real que deseja utilizar para concretizar a multiplicação escalar:")
            num = int(input())
            mult_escalar = matriz.mul_escalar(num)
            print(RED+"\nResultado da multiplicação escalar:"+BLACK)
            mult_escalar.show_matrix()
            input(C)

        elif opcao == "6":
            # Translação com vetor personalizado
            vetor = input("\nInsira o vetor de translação no formato 'x,y,z': ")
            vetor = vetor.split(",")
            vetor = [int(i) for i in vetor]
            resultado = matriz.translacao(vetor)

            print(RED+"\nResultado da translação da matriz usando o vetor",vetor,":"+BLACK)
            resultado.show_matrix()
            input(C)

        elif opcao == "7":
            # Dilatar com vetor de escala personalizado
            escala = input("\nInsira o vetor de escala no formato 'x,y,z': ")
            escala = escala.split(",")
            escala = [int(i) for i in escala]
            resultado = matriz.dilatar(escala)
            print(RED+"\nResultado da dilatação da matriz usando o vetor",escala,":"+BLACK)

            resultado.show_matrix()
            input(C)

        elif opcao == "8":
            # Rodar com angulo e eixo personalizado
            opcao = str(input("\nSelecione o eixo para efetuar a rotação (x, y ou z): "))

            if opcao == "x" or opcao =="X":
                angulo = (int(input(GRAUS_)))
                resultado = matriz.rotacao_x(angulo)
                print(RED + "\nRotacao de", angulo, "graus sobre o eixo dos xx:" + BLACK)
                resultado.show_matrix()
                input(C)

            elif opcao == "y" or opcao == "Y":
                angulo = (int(input(GRAUS_)))
                resultado = matriz.rotacao_y(angulo)
                print(RED + "\nRotacao de", angulo, "graus sobre o eixo dos yy:" + BLACK)
                resultado.show_matrix()
                input(C)

            elif opcao == "z" or opcao == "Z":
                angulo = (int(input(GRAUS_)))
                resultado = matriz.rotacao_z(angulo)
                print(RED + "\nRotacao de", angulo, "graus sobre o eixo dos xx:" + BLACK)
                resultado.show_matrix()
                input(C)

            else:
                print(RED+"\nOpção inválida!"+BLACK)
                input(C)
                menu_matriz()

        elif opcao == "H" or opcao == "h":
            homogeneas = matriz.canonica_para_homogeneas()
            print(RED + "\nPassagem da representação canónica para coordenadas homogéneas:" + BLACK)
            homogeneas.show_matrix()
            input(C)

        elif opcao == "0":
            print("\n" + RED + "Obrigado!" + BLACK)
            break

        else:
            print("\n" + RED + "Erro. Opção escolhida não existe. Por favor escolha de novo." + BLACK)



def __main__():
    menu_matriz()

# Executa a função __main__() quando o programa é executivel,
# mas não quando e importado
if __name__ == "__main__":
    __main__()
