# Vowels and Consonants
# Given a string, return an array with the number of vowels and number of consonants in the string.
#
# Vowels consist of a, e, i, o, u in any case.
# Consonants consist of all other letters in any case.
# Ignore any non-letter characters.
# For example, given "Hello World", return [3, 7].

# Counts vowels and consonants in a given string
def count(s: str) -> list:
    vowels: str = 'aeiou'
    s = s.lower()
    vowel_count = 0
    consonant_count = 0
    for c in s:
        if c.isalpha():
            if c in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return [vowel_count, consonant_count]


assert (count("Hello World") == [3, 7])
assert (count("JavaScript") == [3, 7])
assert (count("Python") == [1, 5])
assert (count("freeCodeCamp") == [5, 7])
assert (count("Hello, World!") == [3, 7])
assert (count("The quick brown fox jumps over the lazy dog.") == [11, 24])