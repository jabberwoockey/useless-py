#!/usr/bin/env python3

from sys import argv, exit
import os
import re

pattern = re.compile("^(?:[-_\\\(\[\'\"«]+)?([\w]([\w]*)?([-\'][\w]+)?)",
          re.IGNORECASE)

# Try to open a file
try:
    script, filename = argv
    with open(filename) as file:
        content = file.read()
except ValueError:
    print('Usage: word_frequency.py file.txt')
    exit(1)
except FileNotFoundError:
    print(f'No such file or directory: {filename}')
    exit(1)

# Initial variables
base = os.path.basename(filename).split(".")[0]
words = content.split()
words_capt = []
words_noncapt = []
words_capt_dict = {}
count = 0

# Create a words list
for word in words:
    re_word = pattern.search(word)
    if re_word != None and not re_word.group(1).isdigit():
        words_capt.append((re_word.group(1).lower()))
    else:
        words_noncapt.append(word.lower())

# Remove 's endings
for i in range(len(words_capt)):
    if words_capt[i][-2:] == "'s":
        words_capt[i] = words_capt[i][:-2]

# Create a ditionary with words
for word in words_capt:
    if word not in words_capt_dict:
        words_capt_dict[word] = 1
    else:
        words_capt_dict[word] += 1

# Sort the dictionary
result = {k: v for k, v in sorted(words_capt_dict.items(),
          key=lambda item: item[1], reverse=True)}

# Write output files
try:
    with open(f'{base}_words.csv', 'w') as res_words:
        for k, v in result.items():
            print(f'{k:>30}:' + f' {v:>7}')
            res_words.write(f'{k};{v}\n')
            count += v
    with open(f'{base}_nonwords.csv', 'w') as res_nonwords:
        for word in set(words_noncapt):
            res_nonwords.write(word + '\n')
except PermissionError:
    print("Close related .csv files!")
    exit(1)

# Print footer
print(f'{count:>39}\n' + '-'*39)
print(f'Total words                   : {len(words):>7}')
print(f'Captured words                : {len(words_capt):>7}')
print(f'Non-captured words            : {len(words_noncapt):>7}')
print(f'Distinct words                : {len(set(words)):>7}')
print(f'Distinct captured words       : {len(set(words_capt)):>7}')
