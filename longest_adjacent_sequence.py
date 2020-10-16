import sys
import numpy
import queue


# Traverses the matrix looking for an element that hasn't been checked yet
def find_next_unchecked_element(elements, last_checked_el):
    (x, y) = last_checked_el
    for i in range(y, len(elements[0])):
        if not elements[x][i]:
            return (x, i)
    for i in range(x + 1, len(elements)):
        for j in range(0, len(elements[0])):
            if not elements[i][j]:
                return (i, j)
    return (-1, -1)


# Adds the element's coordinates to the queue, sets the boolean check to True
def add_element_to_sequence(coords, curr_sequence, is_checked_el):
    curr_sequence.put(coords)
    is_checked_el[coords[0]][coords[1]] = True


# Reads the file, sets the matrix, and returns the dimensions
def get_matrix_from_file(file_name, matrix):
    with open(file_name, "r") as f:
        firstLine = f.readline()
        for line in f:
            matrix.append([str(x) for x in line.split()])
    matrix_dimensions = firstLine.split()
    matrix_dimensions = [int(i) for i in matrix_dimensions]
    return matrix_dimensions


# Traverses the given matrix, looking for sequential equivalent colors
def longest_adjacent_color_sequence(file_name):
    matrix = []
    [rows, cols] = get_matrix_from_file(file_name, matrix)
    rowsxcols = rows * cols
    # Matrix that will store if an element has been checked already
    is_checked_el = numpy.full((rows, cols), False)
    is_checked_el[0][0] = True
    last_checked_el = (0, 0)
    # Queue that will store the elements of the current sequence
    curr_sequence = queue.Queue()
    curr_sequence.put(last_checked_el)  # Starts with the first element
    counter = curr_counter = 1

    # If only the last element is left unchecked, there is no need to look for a sequence
    while last_checked_el[0] != rows - 1 or last_checked_el[1] != cols - 1:
        (x, y) = curr_sequence.get()

        # Check right element
        if y != cols - 1 and not is_checked_el[x][y + 1]:
            if matrix[x][y] == matrix[x][y + 1]:
                add_element_to_sequence((x, y + 1), curr_sequence, is_checked_el)
                curr_counter += 1
        # Check down element
        if x != rows - 1 and not is_checked_el[x + 1][y]:
            if matrix[x][y] == matrix[x + 1][y]:
                add_element_to_sequence((x + 1, y), curr_sequence, is_checked_el)
                curr_counter += 1
        # Check left element
        if y != 0 and not is_checked_el[x][y - 1]:
            if matrix[x][y] == matrix[x][y - 1]:
                add_element_to_sequence((x, y - 1), curr_sequence, is_checked_el)
                curr_counter += 1
        # Check up element
        if x != 0 and not is_checked_el[x - 1][y]:
            if matrix[x][y] == matrix[x - 1][y]:
                add_element_to_sequence((x - 1, y), curr_sequence, is_checked_el)
                curr_counter += 1

        if curr_counter > counter:
            counter = curr_counter
            # If it has already counted all the elements as a part of the same sequence,
            # there is no need to check if all elements are checked
            if counter == rowsxcols:
                break
        if curr_sequence.empty():
            # If the counter is already bigger or equal to half of the elements,
            # there can not be any bigger sequence
            if counter >= rowsxcols / 2 + (rowsxcols % 2 != 0):
                break
            next_unchecked_el = find_next_unchecked_element(is_checked_el, last_checked_el)
            # If all the elements have been checked
            if next_unchecked_el == (-1, -1):
                break
            curr_sequence.put(next_unchecked_el)
            is_checked_el[next_unchecked_el[0]][next_unchecked_el[1]] = True
            last_checked_el = next_unchecked_el
            curr_counter = 1
    return counter


def main():
    tests = sys.argv[1:]
    length = len(tests)
    if length >= 1 and length <= 4:
        for item in tests:
            print("Result of", item + ":", longest_adjacent_color_sequence(item))


if __name__ == "__main__":
    main()
