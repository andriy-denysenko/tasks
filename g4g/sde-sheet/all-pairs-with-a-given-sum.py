# Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.

# Note: All pairs should be printed in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then
# (u1,v1) should be printed first else second.

# Example 1:

# Input:
# A[] = {1, 2, 4, 5, 7}
# B[] = {5, 6, 3, 4, 8}
# X = 9
# Output:
# 1 8
# 4 5
# 5 4
# Explanation:
# (1, 8), (4, 5), (5, 4) are the
# pairs which sum to 9.
# Example 2:
# Input:
# A[] = {-1, -2, 4, -6, 5, 7}
# B[] = {6, 3, 4, 0}
# X = 8
# Output:
# 4 4
# 5 3

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function allPairs() which takes the array A[], B[], its size N and M respectively, and an integer X as inputs and returns the sorted vector pair values of all the pairs u,v where u belongs to array A and v belongs to array B. If no such pair exists return empty vector pair.


# Expected Time Complexity: O(NLog(N))
# Expected Auxiliary Space: O(N)


# Constraints:
# 1 ≤ N, M ≤ 106
# -106 ≤ X, A[i], B[i] ≤ 106

# Made from the second attempt replaced for... with while...

A = [-113, 147, 65, 37, 6, -27, -73, 109, 31, -8, -102, -74, -183, -186, 131, 40, 150, -123, -111, -91, 176, 170, -4, -165, -49, 93, -68, 142, 171, 98, -60, -196, 99, 69, 138, -20, -143, -63, 129, -158, -103, -30, 73, 32, 151, 136, 82, -150, -31, -37, -164, 101, -69, -62, -100, -14, 111, -97, 119, -137, 68, -130, -127, -161, 124]
B = [-122, 102, -67, 152, -169, 48, -52, -134, 33, -91, 188, 6, -148, -109, -35, 64, 32, 75, 198, 22, 65, -168, 185, -66, -127, -147, 145, -29, 104, 51, 93, 71, 129, 39, 76, 10, 70]

N = 65
M = 37
X = 2

class Solution:
    def allPairs(self, A, B, N, M, X):
        result = []
        for u in A:
            for v in B:
                if u + v == X:
                    if len(result) == 0:
                        result.append((u, v))
                    else:
                        i = len(result) - 1
                        while u < result[i][0]:
                            i -= 1
                            if i < 0:
                                break
                        result.insert(i+1, (u, v))
        return result


def main():
    obj = Solution()
    print(obj.allPairs(A, B, N, M, X))

if __name__ == '__main__':
    main()
