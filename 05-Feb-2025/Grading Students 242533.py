# Problem: Grading Students - https://www.hackerrank.com/challenges/grading/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        rounded_grade_1 = grade + 1
        rounded_grade_2 = grade + 2
        if grade < 38:
            result.append(grade)
        elif rounded_grade_1 % 5 == 0:
            result.append(rounded_grade_1)
        elif rounded_grade_2 % 5 == 0:
            result.append(rounded_grade_2)
        else:
            result.append(grade)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
