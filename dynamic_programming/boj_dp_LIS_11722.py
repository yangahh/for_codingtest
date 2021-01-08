# 가장 긴 감소하는 부분 수열 (개수)
import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * n

arr.reverse()
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# dp.reverse()  # 어차피 max값 찾는거라 안해줘도 됨.(빼는게 시간상 좋음)
print(max(dp))

'''
# 다른 방법 (더 빠르진 않음)
for i in range(n, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
'''
