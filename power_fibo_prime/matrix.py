class Matrix():
    @staticmethod
    def _matrix_list(n, m, numbers_list):
        i = 0
        matrix = []
        while i < n*m:
            matrix.append(numbers_list[i:i+m])
            i += m
        return matrix

    def __init__(self, n, m, numbers_list):
        self.rows = n
        self.columns = m
        if len(numbers_list) != n*m:
            raise ValueError(
                f"List length must be {n*m}, got {len(numbers_list)}")
        self.matrix = self._matrix_list(n, m, numbers_list)

    def __getitem__(self, i):
        return self.matrix[i]

    def __str__(self):
        return self.matrix.__str__()

    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError(
                f"Cannot multiply matrix {self.rows} x {self.columns} and matrix {other.rows} x {other.columns}")
        result_list = []
        i_self = 0
        while i_self < self.rows:
            i_other = 0
            while i_other < other.columns:
                j = 0
                result = 0
                while j < self.columns:
                    result += self.matrix[i_self][j]*other.matrix[j][i_other]
                    j += 1
                result_list.append(result)
                i_other += 1
            i_self += 1
            # result_list+=result_list
        return Matrix(self.rows, other.columns, result_list)

    def power(self, pow):
        if self.rows != self.columns:
            raise ValueError(
                f"Only square matrix can be powered")
        if pow == 1:
            return self
        if pow == 0:
            return 1
        result = self.power(pow//2)
        if pow % 2 == 0:
            return result.multiply(result)
        else:
            return self.multiply(result.multiply(result))
