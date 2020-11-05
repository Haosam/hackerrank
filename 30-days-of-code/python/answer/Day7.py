#!/bin/python3

import math
import os
import random
import re
import sys

def reverseorder(arr):
    newarr = arr[::-1]
    listToStr = ' '.join(map(str, newarr)) 
  
    print(listToStr) 

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reverseorder(arr)
