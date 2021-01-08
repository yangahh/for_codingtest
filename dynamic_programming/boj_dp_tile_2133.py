# 3 x N 타일링

n = int(input())

dp = [0] * 31
dp[2] = 3

# 규칙
# dp[4] = dp[4 - 2] * 3 + 2
# dp[6] = dp[6 - 2] * 3 + dp[6 - 4] * 2 + 2
# dp[8] = dp[8 - 2] * 3 + dp[8 - 4] * 2 + 2


# n이 홀수일 경우 결과는 무조건 0
if n % 2 != 0:
    dp[n] = 0

# n이 짝수일 경우
else:
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + 2  # 첫 항과 마지막 항
        for j in range(4, i, 2):
            dp[i] += dp[i - j] * 2


print(dp[n])
