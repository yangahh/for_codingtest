# 문제) 가장 긴 증가하는 부분 수열 (https://www.acmicpc.net/problem/11053)

import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))

# DP테이블 초기화
d = [1] * (n + 1)

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            d[i] = max(d[j] + 1, d[i])


print(max(d))