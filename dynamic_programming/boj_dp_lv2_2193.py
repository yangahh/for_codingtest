# 이친수 개수 구하기

# 런타임 에러나서 dp 테이블 초기화 부분에서 [0] * (n + 1)부분을 100으로 수정함

n = int(input())

dp = [0] * 100

dp[1] = 1
dp[2] = 1


for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])
