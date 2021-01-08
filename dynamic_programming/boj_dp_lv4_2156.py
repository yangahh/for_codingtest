# 최대 양의 포도주 시식

# 런타임에러 발생 이유 : dp[2] = arr[1] + arr[2]를 dp[1] = arr[1] 아래 선언했었는데, n=1인 경우 arr[2]원소는 없기때문에 런타임 에러 발생

'''
 ** 런타임 에러 원인 및 해결
백준에 제출하면 런타임 에러가 나서 원인을 찾아보니
대부분의 경우가 n = 1인 경우(혹은 n=0, n=2 등 n이 극 초반일때의 경우)일때의 dp테이블의 인덱스 접근 오류일 가능성이 높다고 했다.
'''

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

# dp[i]의 의미 : i번째 잔까지 마셨을 때 최대로 마실 수 있는 포도주의 양
dp = [0] * 10001
dp[1] = arr[1]

if n > 1:
    dp[2] = arr[1] + arr[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])

print(dp[n])
