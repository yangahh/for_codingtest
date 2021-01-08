# 계단오르기
import sys

n = int(sys.stdin.readline().rstrip())
arr = [0]

for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

# dp[i]의 의미 : i번째 계단에 올라오기 까지 얻은 점수의 최대값
dp = [0] * (n + 1)

for i in range(1, n+1):
    if i == 1:
        dp[1] = arr[1]
    elif i == 2:
        dp[2] = arr[1] + arr[2]
    else:
        # dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
print(dp)
print(dp[n])


# N = int(input())
# arr = [0]
# dp = [0] * (N+1)
# for _ in range(N):
#     arr.append(int(input()))
# print(arr)

# for i in range(1, N+1):
#     if i == 1:
#         dp[i] = arr[1]
#     elif i == 2:
#         dp[i] = arr[1]+arr[2]
#     else:
#         dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

# print(dp[N])
