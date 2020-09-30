import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    totalCost = meal_cost + (tip_percent*meal_cost/100) + (tax_percent*meal_cost/100)
    floorvalue = math.floor(totalCost)
    if totalCost - floorvalue > 0.5:
        print(floorvalue+1)
    else:
        print(floorvalue)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
