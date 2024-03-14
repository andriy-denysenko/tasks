# Given an array a of n positive integers.
# The task is to find maximum of j-i
# subjected to the constraint of a[i] <= a[j] and i <= j.

class Solution:
    # Works for over allowed 2.4s
    # It's not logical to start from the lowest indexDiff
    # and create loops for both i and j
    # def maxIndexDiff(self,a, n):
    #     indexDiff = 0
    #     for i in range(0, n-1):
    #         for j in range(i+1, n):
    #             if a[i] <= a[j] and j-i > indexDiff:
    #                 indexDiff = j-i
    #     return indexDiff

    # Works for over allowed 2.4s
    # We start from the max indexDiff and check for the condition
    def maxIndexDiff(self,a, n):
        for indexDiff in range(n - 1, 0, -1):
            print(f'For indexDiff = {indexDiff}')
            for i in range(0, n - indexDiff):
                print(f'\tFrom {i} to {n - indexDiff}')
                print(f'\t\t{a[i]} and {a[n - indexDiff]}')
                if a[i] <= a[i + indexDiff]:
                    print(f'Returning {indexDiff}')
                    return indexDiff
        return 0

a = [10, 9, 8, 7, 6, 5, 4, 3, 1, 2]
s = Solution()
s.maxIndexDiff(a, len(a))
