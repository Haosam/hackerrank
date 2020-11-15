#!/bin/python3

import math
import os
import random
import re
import sys

def func(num):
    return num[2:]

if __name__ == '__main__':
    n = int(input())
    print(max(func(bin(n)).split('0')).count('1'))
    
    
    
    
    
"""
I must say, this solution is quite ingenius. Also an added advantage for python
taking input n
bin(n) converts n to its corresponding binary value, so 5 = 0b101
func(bun(n)) puts it into the func(num) function and splices the first 2 values, so 101
.split('0') breaks the 0, so the output becomes ['1','1']
max(...) takes the max value of the array, in this case is 1, but for another case like
13 = 1101
['11','1']
max will return '11'
.count('1') just returns the number of '1's, so 1 for 5, 2 for 13
"""
