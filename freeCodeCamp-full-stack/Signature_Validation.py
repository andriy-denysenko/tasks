import string

letter_key_dic = {}
for index, char in enumerate(string.ascii_lowercase):
    letter_key_dic[char] = index + 1
for index, char in enumerate(string.ascii_uppercase):
    letter_key_dic[char] = index + 27

def verify(message, key, signature):
    sum = 0
    for c in message:
        if c in letter_key_dic.keys():
            sum += letter_key_dic[c]
    for c in key:
        if c in letter_key_dic.keys():
            sum += letter_key_dic[c]

    return sum == signature