# 1D array operations

def traverse_1d(array):
    index = 0
    while index < array.size:
        print(array.data[index], end=" ")
        index = index + 1
    print()


def insert_1d(array, position, value):
    if position < 0 or position > array.size:
        return

    index = array.size
    while index > position:
        array.data[index] = array.data[index - 1]
        index = index - 1

    array.data[position] = value
    array.size = array.size + 1


def delete_1d(array, position):
    if position < 0 or position >= array.size:
        return

    index = position
    while index < array.size - 1:
        array.data[index] = array.data[index + 1]
        index = index + 1

    array.size = array.size - 1


class OneDArray:
    def __init__(self, values, capacity):
        self.data = [0] * capacity
        self.size = 0

        for value in values:
            self.data[self.size] = value
            self.size = self.size + 1


numbers = OneDArray([10, 20, 30, 40], 10)

print("1D array:")
traverse_1d(numbers)

insert_1d(numbers, 2, 25)
print("After insertion:")
traverse_1d(numbers)

delete_1d(numbers, 1)
print("After deletion:")
traverse_1d(numbers)


# 2D array operations

class TwoDArray:
    def __init__(self, rows, columns):
        self.data = [[0] * columns for row in [0] * rows]
        self.rows = rows
        self.columns = columns


def traverse_2d(array):
    row = 0
    while row < array.rows:
        column = 0
        while column < array.columns:
            print(array.data[row][column], end=" ")
            column = column + 1
        print()
        row = row + 1


def insert_row(array, position, values):
    if position < 0 or position > array.rows:
        return
    if values.size != array.columns:
        return

    new_data = []
    row = 0

    while row < position:
        new_data = new_data + [array.data[row]]
        row = row + 1

    new_data = new_data + [values.data[:values.size]]

    while row < array.rows:
        new_data = new_data + [array.data[row]]
        row = row + 1

    array.data = new_data
    array.rows = array.rows + 1


def delete_row(array, position):
    if position < 0 or position >= array.rows:
        return

    new_data = []
    row = 0

    while row < array.rows:
        if row != position:
            new_data = new_data + [array.data[row]]
        row = row + 1

    array.data = new_data
    array.rows = array.rows - 1


matrix = TwoDArray(2, 3)
matrix.data[0][0] = 1
matrix.data[0][1] = 2
matrix.data[0][2] = 3
matrix.data[1][0] = 4
matrix.data[1][1] = 5
matrix.data[1][2] = 6

print("2D array:")
traverse_2d(matrix)

new_row = OneDArray([7, 8, 9], 3)
insert_row(matrix, 1, new_row)
print("After inserting a row:")
traverse_2d(matrix)

delete_row(matrix, 0)
print("After deleting a row:")
traverse_2d(matrix)

