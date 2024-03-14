# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

from time import time

# This solution consumes less time with short strings
def capital_indexes(s):
    return [i for i in range(len(s)) if s[i].isupper()]

# Sample solution
# naive solution
# This solution consumes less time with long strings
def capital_indexes1(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i)
    return result

# shorter version for python2
# from string import uppercase
# def capital_indexes2(s):
#     return [i for i in range(len(s)) if s[i] in uppercase]

# you can also use the .isupper() string method.

if __name__ == "__main__":
    s = time()
    r = capital_indexes("HeLlO")
    f = time()

    s1 = time()
    r1 = capital_indexes("HeLlO")
    f1 = time()

    # s2 = time()
    # r2 = capital_indexes("HeLlO")
    # f2 = time()
    print(f'{f-s}\n{f1-s1}')
