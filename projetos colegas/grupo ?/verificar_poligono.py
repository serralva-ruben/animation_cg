from Vetor import Vetor

class Matriz:
    def __init__(self, value_list):
        self._matriz = self.validate_and_copy_matrix(value_list)

    @staticmethod
    def validate_and_copy_matrix(value_list):
        if not value_list or not value_list[0]:
            return [[]]

        first_row_length = len(value_list[0])

        for row in value_list:
            if not row or len(row) != first_row_length:
                return [[]]

        matrix = [row.copy() for row in value_list]
        return matrix

    def is_polygon_in_3d_plane(self, tolerance_interval):
        row_count = len(self._matriz)
        col_count = len(self._matriz[0]) if self._matriz else 0

        if row_count < 3 or col_count != 3:
            return False

        if row_count == 3:
            return True

        A, B, C, D, i = 0, 0, 0, 0, 0

        while A == B == C == D == 0:
            if i + 2 > len(self._matriz[0]):
                raise ValueError("Error, couldn't calculate the plane equation. The given points form a line.")

            ab = Vetor(self._matriz[i], self._matriz[i + 1])
            ac = Vetor(self._matriz[i], self._matriz[i + 2])
            A, B, C, D = ab.calculate_plane_from_vectors(ac)
            i += 1

        for i in range(3, len(self._matriz)):
            test_point = self._matriz[i]

            if not -tolerance_interval < (test_point[0] * A + test_point[1] * B + test_point[2] * C + D) < tolerance_interval:
                return False

        return True


if __name__ == '__main__':
    m = Matriz([[3, 0, 1], [2, 1, 1], [3, 2, 2], [0, 1, 0]])
    m2 = Matriz([[3, 0, 1], [2, 1, 1], [3, 2, 2], [0, 1, 0], [5, 3, 1]])
    m3 = Matriz([[3, 0, 1], [2, 1, 1], [3, 2, 2], [0, 1, 0], [6, 0, 2]])
    m4 = Matriz([[0, 0, 0], [1, 1, 1], [2, 2, 2], [2.541, 3.541, 4.10]])

    print(m.is_polygon_in_3d_plane(0.2))
    print(m2.is_polygon_in_3d_plane(0.2))
    print(m3.is_polygon_in_3d_plane(0.2))
    print(m4.is_polygon_in_3d_plane(0.2))
