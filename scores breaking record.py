#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minimum = 0
    maximum = 0
    min1 = 0
    max1 = 0
    for i in range (0,len(scores)):
        if i > 0 :
            if scores[i] > maximum:
                maximum = scores[i]
                max1+=1
            elif scores[i] < minimum:
                minimum = scores[i]
                min1+=1
            else:
                min1 = min1
                max1 = max1
                      
        else :
            minimum = maximum = scores[i]
            min1 = max1 = 0
            
        
    return (max1, min1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
