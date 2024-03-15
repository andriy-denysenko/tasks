# Largest subsquare surrounded by X

# Given a square matrix a of size n x n, where each cell can be either 'X' or 'O', you need to find the size of the largest square subgrid that is completely surrounded by 'X'. More formally you need to find the largest square within the grid where all its border cells are 'X'.

# Example 1:

# Input:
# n = 2
# a = [[X,X],
#      [X,X]]
# Output:
# 2
# Explanation:
# The largest square submatrix
# surrounded by X is the whole
# input matrix.
# Example 2:

# Input:
# n = 4
# a = [[X,X,X,O],
#      [X,O,X,X],
#      [X,X,X,O],
#      [X,O,X,X]]
# Output:
# 3
# Explanation:
# Here,the input represents following
# matrix of size 4 x 4
# X X X O
# X O X X
# X X X O
# X O X X
# The square submatrix starting at
# (0,0) and ending at (2,2) is the
# largest submatrix surrounded by X.
# Therefore, size of that matrix would be 3.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function largestSubsquare() which takes the integer n and the matrix a as input parameters and returns the size of the largest subsquare surrounded by 'X'.

# Expected Time Complexity: O(n2)
# Expected Auxillary Space: O(n2)

# Constraints:
# 1 <= n <= 1000
# a[i][j] belongs to {'X','O'}

# My thoughts

# Result := 0
# We must scan all the rows
# We store max lengths of X's in a separate dic:
#    key is length, vals are row index lists.
#    Then we throw away items, which have a single element only.
# v1. We do the same with columns.
#    ???????
# v2. We store start and end positions
#    We loop from longest to the shortest pair
#         If they start and end in equal positions
#              Loop from start x, start y+1 to start x, end y+1
#                   If start x, cur y or end x, cur y contains 0:
#                        continue to the lesser length
# return result

# Or we can loopfrom max length and slice lists

def largestSubsquare(n, a):
     result = 0
     lengths = []
     for row in range(n):
          max_len = 0
          for col in range(n):
               # To be solved
               pass
          pass



