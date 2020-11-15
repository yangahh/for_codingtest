# 문제) N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성 (https://www.acmicpc.net/problem/1920)
'''
import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()

def bin_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        
    return False


for i in x:
    result = bin_search(a, i, 0, n - 1)
    
    if result:
        print(1)
    else:
        print(0)
'''



## set을 이용해서 풀기

import sys
n = int(sys.stdin.readline().rstrip())
a = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))

for i in x:
    if i in a:
        print(1)
    else:
        print(0)