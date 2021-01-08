# 가장 긴 증가하는 부분 수열
import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 모든 i에 대해 dp[i]는 최소 1이므로 1로 초기화
dp = [1] * 1001


for i in range(n):
    # j < i 일때 arr[j] < arr[i] 이면 dp[i] = max(dp[i], dp[j] + 1)
    # arr[j] > arr[i]면 무시 (아무 것도 하지 않음)
    for j in range(i):
        # print(i, j)
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp[:n])
print(max(dp))
