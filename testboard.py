from icecream import ic
from collections import Counter
import math
import sys
INF = sys.maxsize

input = sys.stdin.readline


while True:
    A = list(map(int, input().split()))
    if A[0] == 0 and A[1] == 0 and A[2] == 0:
        break
    A = sorted(A)
    if A[-1] >= A[0] + A[1]:
        print("Invalid")
    elif A[0] == A[1] == A[2]:
        print("Equilateral")
    elif A[0] == A[1] or A[1] == A[2]:
        print("Isosceles")
    else:
        print("Scalene")
 