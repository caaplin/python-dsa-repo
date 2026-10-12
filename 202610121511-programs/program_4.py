def size_of(items):
    count = 0
    for item in items:
        count = count + 1
    return count


def linear_search(items, target):
    index = 0
    for item in items:
        if item == target:
            return index
        index = index + 1
    return -1


def binary_search(items, target):
    left = 0
    right = size_of(items) - 1

    while left <= right:
        middle = (left + right) // 2

        if items[middle] == target:
            return middle
        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def bubble_sort(items):
    result = items[:]
    size = size_of(result)
    end = size - 1

    while end > 0:
        index = 0
        while index < end:
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
            index = index + 1
        end = end - 1

    return result


def selection_sort(items):
    result = items[:]
    size = size_of(result)
    start = 0

    while start < size:
        smallest = start
        index = start + 1

        while index < size:
            if result[index] < result[smallest]:
                smallest = index
            index = index + 1

        result[start], result[smallest] = result[smallest], result[start]
        start = start + 1

    return result


def insertion_sort(items):
    result = items[:]
    index = 1
    size = size_of(result)

    while index < size:
        value = result[index]
        position = index - 1

        while position >= 0 and result[position] > value:
            result[position + 1] = result[position]
            position = position - 1

        result[position + 1] = value
        index = index + 1

    return result


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    left_size = size_of(left)
    right_size = size_of(right)

    while left_index < left_size and right_index < right_size:
        if left[left_index] <= right[right_index]:
            result = result + [left[left_index]]
            left_index = left_index + 1
        else:
            result = result + [right[right_index]]
            right_index = right_index + 1

    while left_index < left_size:
        result = result + [left[left_index]]
        left_index = left_index + 1

    while right_index < right_size:
        result = result + [right[right_index]]
        right_index = right_index + 1

    return result


def merge_sort(items):
    size = size_of(items)

    if size <= 1:
        return items[:]

    middle = size // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])

    return merge(left, right)


def quick_sort(items):
    size = size_of(items)

    if size <= 1:
        return items[:]

    pivot = items[size // 2]
    smaller = []
    equal = []
    larger = []

    for item in items:
        if item < pivot:
            smaller = smaller + [item]
        elif item > pivot:
            larger = larger + [item]
        else:
            equal = equal + [item]

    return quick_sort(smaller) + equal + quick_sort(larger)


numbers = [29, 10, 14, 37, 13]
sorted_numbers = [10, 13, 14, 29, 37]

print("Searching")
print("Linear search for 14:", linear_search(numbers, 14))
print("Binary search for 14:", binary_search(sorted_numbers, 14))

print("Sorting")
print("Bubble sort:", bubble_sort(numbers))
print("Selection sort:", selection_sort(numbers))
print("Insertion sort:", insertion_sort(numbers))
print("Merge sort:", merge_sort(numbers))
print("Quick sort:", quick_sort(numbers))

# Performance comparison:
# Linear search: O(n) time, O(1) extra space.
# Binary search: O(log n) time, O(1) extra space; the input must be sorted.
# Bubble sort: O(n^2) average and worst-case time, O(n) extra space here.
# Selection sort: O(n^2) time, O(n) extra space here.
# Insertion sort: O(n^2) average and worst-case time, O(n) extra space here;
# it can run in O(n) time when the input is already sorted.
# Merge sort: O(n log n) time, O(n) extra space.
# Quick sort: O(n log n) average time, O(n^2) worst-case time;
# this implementation uses extra space for its partitions and recursive calls.

