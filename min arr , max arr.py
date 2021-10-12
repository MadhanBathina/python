

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_total = 0
    max_total = 0
    arr.sort()
    for num in range (0,len(arr)-1):
        min_total=min_total+arr[num]
    for num in range (1,len(arr)):
        max_total=max_total+ arr[num]
    print(min_total, max_total)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
