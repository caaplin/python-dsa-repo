# Lists

def insert_at(items, index, value):
    result = []
    position = 0

    for item in items:
        if position == index:
            result = result + [value]
        result = result + [item]
        position = position + 1

    if position == index:
        result = result + [value]

    return result


def delete_at(items, index):
    result = []
    position = 0

    for item in items:
        if position != index:
            result = result + [item]
        position = position + 1

    return result


def slice_items(items, start, stop):
    result = []
    position = 0

    for item in items:
        if start <= position and position < stop:
            result = result + [item]
        position = position + 1

    return result


# Tuple insertion and deletion return new tuples because tuples are immutable.

def tuple_insert_at(items, index, value):
    result = ()
    position = 0

    for item in items:
        if position == index:
            result = result + (value,)
        result = result + (item,)
        position = position + 1

    if position == index:
        result = result + (value,)

    return result


def tuple_delete_at(items, index):
    result = ()
    position = 0

    for item in items:
        if position != index:
            result = result + (item,)
        position = position + 1

    return result


def tuple_slice_items(items, start, stop):
    result = ()
    position = 0

    for item in items:
        if start <= position and position < stop:
            result = result + (item,)
        position = position + 1

    return result


# Set-like operations.
# A set comprehension creates a native set; native sets do not support indexing.

def set_without(values, target):
    return {item for item in values if item != target}


def set_with(values, value):
    return {item for item in values} | {value}


# Dictionary comprehension and copy.
# Dictionaries do not have positional slicing; select entries by key instead.

def dict_without_key(mapping, target):
    return {key: value for key, value in mapping.items() if key != target}


def dict_with_entry(mapping, new_key, new_value):
    return {
        key: value for key, value in mapping.items() if key != new_key
    } | {new_key: new_value}


# Comprehensions

squares = [number * number for number in (1, 2, 3, 4)]
even_numbers = {number for number in (1, 2, 3, 4) if number % 2 == 0}
word_lengths = {word: count for word, count in (("cat", 3), ("tiger", 5))}
print("Program exited with 0")


