# 쉬운 계단수(숫자가 0으로 시작하지 않음)

n = int(input())

dp = [[0] * 10 for _ in range(101)]
# 0행과 모든 행의 0열은 무시

# dp[1]은 dp[1][0] 빼고 다 '1'로 만든다
for i in range(1, 10):
    dp[1][i] = 1

# dp[2]는 dp[2][0]와 dp[2][9] 빼고 모두 2로 만든다
dp[2] = [2 for _ in range(10)]
dp[2][0] = 0
dp[2][9] = 1

print(dp)

for i in range(3, n + 1):
    for j in range(1, 10):
        if j == 1:
            dp[i][j] = dp[i-2][j] + dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


DIV = 1000000000
print(sum(dp[n]) % DIV)
