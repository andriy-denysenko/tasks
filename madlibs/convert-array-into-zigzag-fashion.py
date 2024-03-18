# Given an array arr of distinct elements of size N, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

# arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 

# NOTE: If your transformation is correct, the output will be 1 else the output will be 0. 

# Example 1:

# Input:
# N = 7
# Arr[] = {4, 3, 7, 8, 6, 2, 1}
# Output: 3 7 4 8 2 6 1
# Explanation: 3 < 7 > 4 < 8 > 2 < 6 > 1
# Example 2:

# Input:
# N = 4
# Arr[] = {1, 4, 3, 2}
# Output: 1 4 2 3
# Explanation: 1 < 4 > 2 < 3
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function zigZag() which takes the array of integers arr and n as parameters and returns void. You need to modify the array itself.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= N <= 106
# 0 <= Arri <= 109

# Passed on the 2nd attempt because of server lag. I did not change anything before the 2nd try.

arr = [4, 3, 7, 8, 6, 2, 1]
n = 7

class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
        for i in range(n-1):
            print(arr)
            print(f'Element arr[{i}] == {arr[i]}.')
            if i % 2 == 0:
                print(f'Is {arr[i]} < {arr[i+1]}?')
                if arr[i] > arr[i+1]:
                    print(f'No. Swapping.')
                    foo = arr[i+1]
                    arr[i+1] = arr[i]
                    arr[i] = foo
            else:
                print(f'Is {arr[i]} > {arr[i+1]}?')
                if arr[i] < arr[i+1]:
                    print(f'No. Swapping.')
                    foo = arr[i+1]
                    arr[i+1] = arr[i]
                    arr[i] = foo


        return arr

def main():
    obj = Solution()
    print(obj.zigZag(arr, n))

if __name__ == '__main__':
    main()
