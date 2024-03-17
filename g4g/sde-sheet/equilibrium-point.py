# Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.

# Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.

# Example 1:

# Input:
# n = 5
# A[] = {1,3,5,2,2}
# Output:
# 3
# Explanation:
# equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2).
# Example 2:

# Input:
# n = 1
# A[] = {1}
# Output:
# 1
# Explanation:
# Since there's only element hence its only the equilibrium point.
# Your Task:
# The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= n <= 105
# 0 <= A[i] <= 109

# Again, we cannot use sum() like
# for i in range(N):
#     lsum = sum(A[:i])
#     rsum = sum(A[i+1:])
#     if lsum == rsum:
#         return i + 1
# return -1

# Solved using Hint2

A = [1,3,5,2,2]
N = 5

class Solution:
    def equilibriumPoint(self, A, N):
        total = sum(A)

        if len(A) == 1:
            return 1

        l_sum = 0
        r_sum = 0

        for i in range(1, N):
            l_sum += A[i -1]
            r_sum = total - l_sum - A[i]
            if l_sum == r_sum:
                return i + 1

        return -1



def main():
    obj = Solution()
    print(obj.equilibriumPoint(A, N))


if __name__ == '__main__':
    main()
