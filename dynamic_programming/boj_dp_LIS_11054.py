# 가장 긴 바이토닉 부분 수열

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp_left = [1] * n
dp_right = [1] * n

# 정방향으로 가장 긴 부분수열 찾기
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)

print(dp_left)

# 역방향으로 가장 긴 부분수열 찾기
arr.reverse()
print(f'arr_reverse : {arr}')
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)
dp_right.reverse()
print(dp_right)

# dp = [dp_right[i] + dp_right[i] for i in range(n)]
# dp = []
# for i in range(n):
#     print(dp_left[i], dp_right[i])
#     dp.append(dp_left[i] + dp_right[i])

dp = [dp_left[i] + dp_right[i] for i in range(n)]

print(f'dp : {dp}')
print(max(dp))


################################################
'''
n = int(input())
lst = list(map(int, input().split()))
dp_left = [1] * n
dp_right = [1] * n
print(lst)

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            if dp_left[i] < dp_left[j] + 1:
                dp_left[i] = dp_left[j] + 1

print(dp_left)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if lst[j] < lst[i]:
            if dp_right[i] < dp_right[j] + 1:
                dp_right[i] = dp_right[j] + 1

dp = [dp_left[i] + dp_right[i] for i in range(n)]

print(dp_right)

print(dp)
print(max(dp) - 1)
'''
