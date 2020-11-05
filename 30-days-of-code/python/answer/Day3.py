#!/bin/python3

import math
import os
import random
import re
import sys

def ifcond(N):
    if N%2 == 0 and 1<N<6:
        print("Not Weird")
    elif N%2==0 and 5<N<21:
        print("Weird")
    elif N%2==0 and N>21:
        print("Not Weird")
    else:
        print("Weird")

if __name__ == '__main__':
    N = int(input())
    ifcond(N)
