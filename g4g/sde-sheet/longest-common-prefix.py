# Given an array of N strings, find the longest common prefix among all strings present in the array.


# Example 1:

# Input:
# N = 4
# arr[] = {geeksforgeeks, geeks, geek,
#          geezer}
# Output: gee
# Explanation: "gee" is the longest common
# prefix in all the given strings.
# Example 2:

# Input:
# N = 2
# arr[] = {hello, world}
# Output: -1
# Explanation: There's no common prefix
# in the given strings.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function longestCommonPrefix() which takes the string array arr[] and its size N as inputs and returns the longest common prefix common in all the strings in the array. If there's no prefix common in all the strings, return "-1".


# Expected Time Complexity: O(N*min(|arri|)).
# Expected Auxiliary Space: O(min(|arri|)) for result.

# Solved from the 2nd atttempt. The mistake was to use 'in' instead of slicing

n = 5
arr = ['geeksforgeeks', 'geeks', 'geek', 'geezer', 'goose']

class Solution:
    def longestCommonPrefix(self, arr, n):
        m = min(arr)
        for i in range(len(m), 0, -1):
            arr2 = [x for x in arr if m[:i] == x[:i]]
            if len(arr2) == n:
                return m[:i]
        return -1

def main():
    obj = Solution()
    print(obj.longestCommonPrefix(arr, n))

if __name__ == '__main__':
    main()
