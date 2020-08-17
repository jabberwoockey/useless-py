#!/usr/bin/env python3

from sys import argv

script, textfile = argv

with open(textfile, 'r') as text:
    content = text.read()

words = content.split()
letters = dict()

for word in words:
    for letter in word.lower():
        if ord(letter) in range(1072, 1106):
            letters[letter] = letters.get(letter, 0) + 1

res = sorted([(v, k) for k,v in letters.items()], reverse=True)
for i in range(len(res)):
    print(f'{i+1:>2}. {res[i][1]}: {res[i][0]:>5}')
