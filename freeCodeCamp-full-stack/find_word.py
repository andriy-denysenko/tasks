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

def find_word(matrix, word):
    word_coords: list = None
    row_index: int = 0
    candidate: list = []
    word_length: int = len(word)
    # Check rows for a match
    while row_index < word_length and word_coords is None:
        candidate = matrix[row_index]
        if is_word(candidate, word):
            word_coords = [[row_index, 0], [row_index, word_length - 1]]
        elif is_reverse_word(candidate, word):
            word_coords = [[row_index, word_length - 1], [row_index, 0]]
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
                if is_word(candidate, word):
                    word_coords = [[0, col_index], [word_length - 1, col_index]]
                elif is_reverse_word(candidate, word):
                    word_coords = [[word_length - 1, col_index], [0, col_index]]
                else:
                    start_pos = col_index + 1
    return word_coords


# Determines if the list represents the word
def is_word(row, word):
    return ''.join(row) == word


# Determines if the list represents the reversed word
def is_reverse_word(row, word):
    return ''.join(row[::-1]) == word


# Gets a column with the specified index from a matrix
def get_column(matrix: list, col_index: int) -> list:
    column = []
    for row_index in range(len(matrix)):
        column.append(matrix[row_index] [col_index])
    return column


matrix: list = [
    ["a", "c", "t"],
    ["t", "a", "t"],
    ["c", "t", "c"]
]

word: str = 'cat'

print(find_word(matrix, word))
