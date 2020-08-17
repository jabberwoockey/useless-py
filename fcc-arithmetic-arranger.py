#!/usr/bin/env python3

# https://repl.it/@freeCodeCamp/fcc-arithmetic-arranger

from functools import reduce as red

def arithmetic_arranger(problems, result=False):
    arranged_problems = ''
    nums1 = list()
    nums2 = list()
    ops = list()
    lengths = list()
    op_funcs = {
        '+': lambda x,y: x + y,
        '-': lambda x,y: x - y
    }

    for problem in problems:
        num1, op, num2 = problem.split(' ')
        nums1.append(num1)
        nums2.append(num2)
        ops.append(op)
        lengths.append(len(num1) + 2 if len(num1) >= len(num2) else len(num2) + 2)

    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
    elif not (''.join(nums1) + ''.join(nums2)).isnumeric():
        arranged_problems = 'Error: Numbers must only contain digits.'
    elif len(red(lambda x,y: x if len(x) > len(y) else y, nums1 + nums2)) > 4:
        arranged_problems = 'Error: Numbers cannot be more than four digits.'
    elif not set(ops).issubset(set(op_funcs)):
        arranged_problems = "Error: Operator must be '+' or '-'."
    else:
        prob_len = len(problems)
        arranged_problems += '    '.join([f'{nums1[i]:>{lengths[i]}}' \
                                          for i in range(prob_len)]) + '\n'
        arranged_problems += '    '.join([f'{ops[i]} {nums2[i]:>{lengths[i]-2}}' \
                                          for i in range(prob_len)]) + '\n'
        arranged_problems += '    '.join([f'{"-" * lengths[i]}' \
                                          for i in range(prob_len)])
        if result:
            arranged_problems += '\n' + \
                             '    '.join([f'{str(op_funcs[ops[i]](int(nums1[i]),int(nums2[i]))):>{lengths[i]}}' \
                                          for i in range(prob_len)])
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print('\n')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print('\n')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49124"], True))
print('\n')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123456 + 491"], True))
print('\n')
print(arithmetic_arranger(["32 + 698", "3801 / 2", "45 + 43", "123 + 49"]))
print('\n')
print(arithmetic_arranger(["32 + 698", "3801 + 2", "45 + 43", "123 + 49", "56 - 24", "123 + 74"]))
print('\n')
print(arithmetic_arranger(["32 + 698", "3801 + 2", "45a + 43", "123 + 49b"]))
