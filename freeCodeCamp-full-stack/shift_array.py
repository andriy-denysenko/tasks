def shift_array(arr, n):
    head = []
    tail = []
    if n > 0:
        tail = arr[:len(arr) - n]
        head = arr[-n:]
    elif n < 0:
        n = -n
        head = arr[n:]
        tail = arr[:n]
        n = -n
    if n != 0:
        head.extend(tail)
    return head


arr = [1, 2, 3, 4, 5]
print(shift_array(arr, 1))
print(shift_array(arr, -1))
