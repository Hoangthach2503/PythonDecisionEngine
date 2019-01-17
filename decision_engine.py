import numpy as np

apple, banana, orange = (1.0, 2.0, 3.0)

choices = (float(apple), float(banana), float(orange))

array = np.ones((choices.__len__() + 1, choices.__len__() + 1))


def set_values(values, matrix):
    def get_inverse(a):
        x = np.reciprocal(a)
        return x
    count = 0
    for x in range(1, array[0].__len__()):
        for y in range(1, array[0].__len__()):
            if x >= y:
                continue
            value = values[count]
            if value < 0:
                absolute = abs(value)
                new_value = get_inverse(absolute)
                matrix[x][y] = new_value
                matrix[y][x] = absolute
            else:
                absolute = abs(value)
                new_value = get_inverse(absolute)
                matrix[x][y] = absolute
                matrix[y][x] = new_value
            count += 1
    return matrix


def create_eigen_vector_array(matrix, sums):
    for x in range(matrix.__len__()):
        for y in range(matrix.__len__()):
            matrix[x][y] = matrix[x][y] / sums[y]
    return matrix


def calculate_eigen_vectors(array):
    count = 0
    for i in array:
        array[count] = i / 4
        count += 1
    return array


set_values(choices, array)
eigen_array = create_eigen_vector_array(array, array.sum(axis=0))

print('EIGEN MATRIX\n', eigen_array)

print('\nPROBABILITIES')
vector_totals = 0
for vec in calculate_eigen_vectors(eigen_array.sum(axis=1)):
    print('{}%'.format(vec * 100))
    vector_totals += vec * 100

