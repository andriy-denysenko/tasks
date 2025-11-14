# Array Shift
# Given an array and an integer representing how many positions to shift the array, return the shifted array.
#
# A positive integer shifts the array to the left.
# A negative integer shifts the array to the right.
# The shift wraps around the array.
# For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].

# Shifts an array to the left/right by the given number of positions.
def shift_array(arr: list, n: int) -> list:
    head: list = []
    tail: list = []
    # Reduce n while it is greater than array length
    # (The reminder is always positive, and the left shift is applied instead of the right shift.
    # It provides correct results.)
    n = n if abs(n) < len(arr) else n % len(arr)
    # Split the array
    if n > 0:
        head = arr[n:]
        tail = arr[:n]
    elif n < 0:
        head = arr[n:]
        tail = arr[:len(arr) + n]
    if n != 0:
        head.extend(tail)
    return head


assert (shift_array([1, 2, 3], 1) == [2, 3, 1])
assert (shift_array([1, 2, 3], -1) == [3, 1, 2])
assert (shift_array(["alpha", "bravo", "charlie"], 5) == ["charlie", "alpha", "bravo"])
assert (shift_array(["alpha", "bravo", "charlie"], -11) == ["bravo", "charlie", "alpha"])
assert (shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15) == [5, 6, 7, 8, 9, 0, 1, 2, 3, 4])
