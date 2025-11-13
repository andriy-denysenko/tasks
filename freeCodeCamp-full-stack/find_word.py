# Word Search
#
# Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.
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
    # Set found flag to false
    word_coords = None
    # Is the first row the word?
    row_index = 0
    # Check if the first row represents the word or reversed word
    row: list = matrix[row_index]
    if ''.join(row) == word:
        word_coords = [[0, 0], [0, len(row)]]
    elif ''.join(row[::-1]) == word:
        word_coords = [[0, len(row)], [0, 0]]

 #   if word_coords is None:
 #       if word[0] in row:
 #           col_index = row.index(word[0])

    # Try to find the first letter position in the first row.

    # It can occur 0 or more times.
    # If it occurs:
    #   for each occurrence:
    #       set the first return value to row, col of the occurrence
    #       start counting from the next row
    #       set exit flag to false
    #       while exit flag is false:
    #           if the current row is before the last or is the last itself:
    #               check if the correspondent letter in the same column
    #               is the letter from the word with the same index as the row
    #               if it is:
    #                   increment row
    #               else:
    #                   set exit flag to true
    #           else:
    #               (if we get here, the word is found)
    #               set found flag to true
    #               set the second return value to last row, col of the occurrence
    #               set exit flag to true
    #   if not found:
    #       Repeat FIND VERTICAL WORD searching from the last letter to the first one downward.
    #   if not found:
    #       join each row to find the word
    #   if not found:
    #       join each reversed row to find the word
    #
    #
    return matrix


# Determines if the list represents the word
def is_hz_word(row, word):
    return ''.join(row) == word

# Determines if the list represents the reversed word
def is_hz_reverse_word(row, word):
    return ''.join(row[::-1]) == word

# Gets a column with the specified index from a matrix
def get_column(matrix, col_index):
    column = []
    for row_index in range(len(matrix)):
        column.append(matrix[row_index, col_index])
    return column