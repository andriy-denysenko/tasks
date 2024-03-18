# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
 
 
def heapify(arr, N, i):
    print(f'in heapify({arr}, {N}, {i})')
    largest = i  # Initialize largest as root
    print(f'largest = {largest}')
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
    print(f'l = {l}')
    print(f'r = {r}')
 
    # See if left child of root exists and is
    # greater than root
    print(f'See if left child (#{l}) of root exists and is greater than root')
    if l < N and arr[largest] < arr[l]:
        print('Yes. Set largest to left.')
        largest = l
    else:
        print('No. Do nothing.')
 
    # See if right child of root exists and is
    # greater than root
    print(f'See if right child (#{r}) of root exists and is greater than root')
    if r < N and arr[largest] < arr[r]:
        print('Yes. Set largest to right.')
        largest = r
    else:
        print('No. Do nothing.')
 
    # Change root, if needed
    if largest != i:
        print(f'Largest has changed.')
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        print(f'swap ith {arr[i]} with largest {arr[largest]}')
        print('And heapify the root.')
 
        # Heapify the root.
        heapify(arr, N, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr):
    N = len(arr)
    print(f'N = {N}')
 
    # Build a maxheap.
    print(f'Build a maxheap.')
    for i in range(N//2 - 1, -1, -1):
        print(f'Maxheap i = {i}')
        heapify(arr, N, i)
 
    # One by one extract elements
    print('One by one extract elements')
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
 
 
# Driver's code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
 
    # Function call
    heapSort(arr)
    N = len(arr)
 
    print("Sorted array is")
    for i in range(N):
        print("%d" % arr[i], end=" ")
# This code is contributed by Mohit Kumra
