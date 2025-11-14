# Word Search
#
# Given a matrix (an array of arrays) of single letters and a word to find,
# return the start and end indices of the word in the matrix.
#
#     The given matrix will be filled with all lowercase letters (a-z).
#     The word to find will always be in the matrix exactly once.
#     The word to find will always be in a straight line in one of these directions:
#         left to right
#         right to left
#         top to bottom
#         bottom to top
#
# For example, given the matrix:
#
# [
#   ["a", "c", "t"],
#   ["t", "a", "t"],
#   ["c", "t", "c"]
# ]
#
# And the word "cat", return:
#
# [[0, 1], [2, 1]]
#
# Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t"
# (end of the word).

def find_word(matrix: list, word: str) -> list:
    word_coords: list = None
    row_index: int = 0
    candidate: list = []
    word_length: int = len(word)
    # Check rows for a match
    while row_index < word_length and word_coords is None:
        candidate = matrix[row_index]
        found_pos: int = get_word_pos(candidate, word)
        if found_pos > -1:
            word_coords = [[row_index, found_pos], [row_index, word_length - 1]]
        else:
            found_pos = get_reverse_word_pos(candidate, word)
            if found_pos > -1:
                word_coords = [[row_index, found_pos], [row_index, found_pos - word_length + 1]]
            else:
                row_index += 1

    # Check columns for a match if rows do not match
    if word_coords is None:
        col_index: int = 0
        first_letter: str = word[0]
        # Check the first row, then the last
        row: list = matrix[0]
        if first_letter not in row:
            # Check the last row
            row = matrix[len(matrix) - 1]

        # Check for no match to search safely
        if first_letter in row:
            # Check for certain occurrences
            start_pos: int = 0
            while start_pos < word_length and word_coords is None:
                col_index = row.index(first_letter, start_pos)
                candidate = get_column(matrix, col_index)
                found_pos: int = get_word_pos(candidate, word)
                if found_pos > -1:
                    word_coords = [[found_pos, col_index], [word_length - 1, col_index]]
                else:
                    found_pos = get_reverse_word_pos(candidate, word)
                    if found_pos > -1:
                        word_coords = [[found_pos, col_index], [found_pos + 1 - word_length, col_index]]
                    else:
                        start_pos = col_index + 1
    return word_coords


# Determines if the list contains the word
def get_word_pos(row, word):
    return ''.join(row).find(word)


# Determines if the list contains the reversed word
def get_reverse_word_pos(row, word):
    found_pos: int = ''.join(row[::-1]).find(word)
    if found_pos > -1:
        found_pos = len(row) - found_pos - 1
    return found_pos


# Gets a column with the specified index from a matrix
def get_column(matrix: list, col_index: int) -> list:
    column = []
    for row_index in range(len(matrix)):
        column.append(matrix[row_index][col_index])
    return column


assert (find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat") == [[0, 1], [2, 1]])
assert (find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog") == [[0, 0], [0, 2]])
assert (find_word([
    ["h", "i", "s", "h"],
    ["i", "s", "f", "s"],
    ["f", "s", "i", "i"],
    ["s", "h", "i", "f"]],
    "fish") == [[3, 3], [0, 3]])
assert (find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox") == [
    [1, 3], [1, 1]])
