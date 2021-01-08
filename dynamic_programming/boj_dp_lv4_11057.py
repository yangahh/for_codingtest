# 오르막수 (숫자가 0으로 시작할 수 있음)

n = int(input())

# dp[n][m]의 의미 : n자리수일 때 첫째자리수가 m일때 나머지 뒤 자리수에 올 수 있는 숫자들의 경우의 수
# 편의상 dp[0]은 무시

dp = [[0] * 10 for i in range(n + 1)]
dp[1] = [1 for i in range(10)]

for i in range(2, n + 1):  # i는 행(가로 줄)
    for j in range(10):  # j는 열 (0~9)
        for k in range(j, 10):  # k는 윗 줄의 열 번호 (0~9, 1~9, 2~9....이런식으로 반복)
            dp[i][j] += dp[i-1][k]

# 결과는 dp[n] 행의 모든 값을 더한 것
result = sum(dp[n]) % 10007
print(result)


# https://sh4869.tistory.com/6
