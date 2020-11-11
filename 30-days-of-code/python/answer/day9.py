#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n <= 2 or n >= 12:
        print('Value error')
    else:
        n = n*factorial(n-1)
    return n
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

    ####### Recursion Function########
    
    """
    Factorial functions are essentially
    #n! = n x (n-1)!
    like 3! = 3x2x1, which is also 3x(3-1)!
    so to achieve that in a function,
    we have to multiply it by the previous 'n'value of the function
    so
    n = int(input())
    def factorial_function(n):
        n = n*factorial(n-1)
    This makes it multiply by the previous n function
    """
