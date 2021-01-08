# 2 x N 타일링 2
# 2x1, 1x2, 2x2 타일로 채우기

import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3


for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[n] % 10007)
