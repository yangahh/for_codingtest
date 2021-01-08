# 제곱수의 합으로 표현

import math

n = int(input())

dp = [0] * (n + 1)


for i in range(1, n + 1):
    dp[i] = i  # 먼저 가장 최악의 경우인 1^2로 구성되는 방법
    for j in range(1, int(math.sqrt(i)) + 1):
        if dp[i] > dp[i - j*j] + 1:  # min쓰면 시간 초과되서 if문으로 수정
            dp[i] = dp[i - j*j] + 1

print(dp[n])
