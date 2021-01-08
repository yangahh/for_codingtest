# 스티커 떼어내기
import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    n = int(sys.stdin.readline().rstrip())

    # 스티커 입력받기(2차원 리스트)
    arr = [list(map(int, sys.stdin.readline().rstrip().split()))
           for _ in range(2)]

    # 인덱싱 편의성을 위해 arr리스트에 인덱스 0자리에 버퍼 추가
    arr[0] = [0] + arr[0]
    arr[1] = [0] + arr[1]

    # dp테이블 초기화
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][1] = arr[0][1]
    dp[1][1] = arr[1][1]

    # 보텀업 방식
    for i in range(2, n + 1):
        dp[0][i] = max(dp[1][i - 1] + arr[0][i], dp[1][i - 2] + arr[0][i])
        dp[1][i] = max(dp[0][i - 1] + arr[1][i], dp[0][i - 2] + arr[1][i])

    print(max(dp[0][n], dp[1][n]))
