# 합분해

n, k = map(int, input().split())

# DP 테이블 초기화 (2차원 리스트)
dp = [[0] * 201 for _ in range(201)]

for i in range(1, n + 1):
    for j in range(1, k + 1):

        if i == 1:
            dp[i][j] = j
        elif j == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

DIV = 1000000000
print(dp[n][k] % DIV)
