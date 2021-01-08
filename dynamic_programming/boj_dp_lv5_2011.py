# 암호코드 경우의 수
import sys

arr = list(map(int, sys.stdin.readline().rstrip()))
arr_len = len(arr)

# dp테이블 초기화
# dp[i]의 의미 : i번째 문자열까지 해석했을 때 나올 수 있는 해석의 경우의 수
dp = [0] * (arr_len + 1)


# 암호가 잘못된 경우(맨 첫자리 수가 0일 때)
if arr[0] == 0:
    print(0)
else:
    arr = [0] + arr  # 인덱싱을 편리하게 하기위해 인덱스 0자리에 버퍼 추가

    dp[0] = 1  # 아래 코드 중 두 자리 수의 암호일 때를 위해 0이아니라 1이되어야 함
    dp[1] = 1  # arr[1]로 이루어진 암호코드의 경우의 수는 1개
    for i in range(2, arr_len + 1):

        # 한 자리 수의 암호일 때
        if 1 <= arr[i] <= 9:
            dp[i] = dp[i] + dp[i - 1]

        # 두 자리 수의 암호일 때
        if 10 <= (arr[i-1] * 10 + arr[i]) <= 26:
            dp[i] = dp[i] + dp[i - 2]

    print(dp[arr_len] % 1000000)


'''
if a[0] == 0: # 암호 만들 수 없는 경우
    print(0)
else :
    a = [0] + a # 인덱싱을 위해 추가한 0
    dp[0] = 1
    dp[1] = 1 # 첫번째 수로 이뤄진 암호코드는 1개이다.

    for i in range(2, l+1):
        cur = a[i] # 한 자리
        cur2 = a[i-1] * 10 + a[i] # 두 자리
        if cur >= 1 and cur <= 9:
            dp[i] += dp[i-1]
        if cur2 >= 10 and cur2 <= 26:
            dp[i] += dp[i-2]
        dp[i] %= 1000000


    print(dp[l])
'''
