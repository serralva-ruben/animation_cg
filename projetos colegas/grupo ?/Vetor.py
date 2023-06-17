from typing import List

class Vector:
    def __init__(self, point_a: List[float], point_b: List[float]):
        if len(point_a) != 3 or len(point_b) != 3:
            raise ValueError("A point must have X, Y, Z coordinates")

        self.point_a = point_a
        self.point_b = point_b
        self.vector = [point_b[i] - point_a[i] for i in range(3)]

    def __add__(self, other: "Vector") -> "Vector":
        if len(other.get_vector()) == 3:
            new_vector = [self.vector[i] + other.get_vector()[i] for i in range(3)]
            return Vector([0, 0, 0], new_vector)
        
        raise ValueError("The other vector must have X, Y, Z coordinates")

    def __mul__(self, other: "Vector") -> float:
        return sum(self.vector[i] * other.get_vector()[i] for i in range(len(self.vector)))

    def get_vector(self) -> List[float]:
        return self.vector

    def get_point_a(self) -> List[float]:
        return self.point_a

    def get_point_b(self) -> List[float]:
        return self.point_b

    def calculate_plane_from_vectors(self, other: "Vector") -> tuple:
        x1, x2, x3 = self.point_a[0], self.point_b[0], other.get_point_b()[0]
        y1, y2, y3 = self.point_a[1], self.point_b[1], other.get_point_b()[1]
        z1, z2, z3 = self.point_a[2], self.point_b[2], other.get_point_b()[2]

        A = (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1)
        B = (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1)
        C = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        D = - (A * x1 + B * y1 + C * z1)

        return A, B, C, D

    def __str__(self):
        return str(self.vector)


if __name__ == '__main__':
    vector_ab = Vector([0, 0, 0], [1, 1, 1])
    vector_cd = Vector([0, 0, 0], [2, 2, 2])

    print(vector_ab + vector_cd)
    print(vector_ab * vector_cd)
    print(vector_ab.calculate_plane_from_vectors(vector_cd))
