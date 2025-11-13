import re

def count_words(sentence):
    word_count = len(re.findall(r'\S+', sentence))
    return word_count
