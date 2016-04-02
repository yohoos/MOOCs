import re

words = []

with open('regex_sum_255931.txt') as f:
    for line in f:
        matching = re.findall('[0-9]+', line)
        words.extend(matching)

words = map(int, words)
print sum(words)
