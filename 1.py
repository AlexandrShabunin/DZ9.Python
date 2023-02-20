from typing import List


class matrix33:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        w_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(w_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Недопустимый размер матрицы")

    def __add__(self, other: "matrix33") -> "matrix33":
        if not isinstance(other, matrix33):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"недопустимый тип объекта")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Matrix sizes difference")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return matrix33(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':
    matrixwow = matrix33([[1, 2], [3, 4]])
    print(matrixwow, '\n')

    matrixwow2 = matrix33([[10, 20], [30, 40]])
    print(matrixwow2, '\n')

    print(matrixwow + matrixwow2)
