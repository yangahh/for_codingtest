# 카드 구매하기 (금액의 최대값)
import sys
# import copy

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr = [0] + arr  # 편의상 인덱스 1부터 사용하기 위해 인덱스 0 자리에 버퍼 추가

# dp[i]는 i개의 카드를 사는데 드는 금액의 최대값
dp = [0] * 1001
dp[1] = arr[1]
# dp = copy.deepcopy(arr)


for i in range(2, n + 1):
    for j in range(1, i):
        # 여러 조합으로 카드를 사는 경우, i개가 들어있는 카드팩 1개만 사는 경우, 지금까지의 최대값 중 가장 큰 값으로 갱신
        dp[i] = max(dp[i - j] + dp[j], arr[i], dp[i])
        # dp[i] = max(dp[i - j] + dp[j], dp[i])


print(dp[n])

'''다른방법
import sys
import copy

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr = [0] + arr  

dp = copy.deepcopy(arr)

for i in range(2, n + 1):
    for j in range(1, i):
        dp[i] = max(dp[i - j] + dp[j], dp[i])

print(dp[n])
'''
