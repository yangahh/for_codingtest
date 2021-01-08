# 증가 부분 수열 중에서 합이 가장 큰 것
import sys
import copy

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# dp를 arr리스트 값으로 초기화(모든 수열의 가장 작은 합은 자기 자신만 더한 것이므로)
dp = copy.deepcopy(arr)


for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])


print(max(dp))


'''
n = int(input())
num = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    dp[i] = num[i]
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + num[i])

print(max(dp))
'''
