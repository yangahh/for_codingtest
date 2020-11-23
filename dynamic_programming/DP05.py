# 문제) 금광
# n * m 크기의 금광이 있다. 금광은 1*1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어있다.
# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발 가능
# 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동
# 채굴자가 얻을 수 있는 금의 최대 크기를 출력하시오
# ** 테스트 케이스 횟수가 첫 번째 줄에 입력됨

"""
<점화식>
arrry[i][j] : i행 j열에 존재하는 금의 양
d[i][j] : i행 j열까지의 최적의 해(얻을 수 있는 금의 최댓값)
d[i][j] = array[i][j] + max(d[i-1][j-1], d[i][j-1], d[i+1][j-1])

** d[i-1][j-1] : d[i][j] 기준 왼쪽 위
** d[i][j-1] : d[i][j] 기준 왼쪽
** d[i+1][j-1] : d[i][j] 기준 왼쪽 아래
** 초기 데이터를 담는 변수 array를 사용하지 않고 바로 DP테이블에 초기 데이터를 담아서 DP를 적용할 수도 있다.
"""


tc = int(input())
for tc in range(tc):

    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    # 금광(array) 초기화
    array = []
    index = 0
    for i in range(n):
        array.append(input_list[index : index + m])
        index += m

    # for i in range(n):
    #     for j in range(m):
    #         print(array[i][j], end=" ")
    #     print()

    # DP 테이블 초기화 (초기화 값은 array배열)
    d = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            d[i][j] = array[i][j]

    # 보텀업 방식 DP
    for j in range(1, m):
        for i in range(n):
            # print(i, j, end=" : ")
            # 맨 위 행에서 올 경우
            if i == 0:
                d[i][j] = array[i][j] + max(d[i][j - 1], d[i + 1][j - 1])
            # 맨 아래 행에서 올 경우
            elif i == (n - 1):
                d[i][j] = array[i][j] + max(d[i - 1][j - 1], d[i][j - 1])
            # 중간
            else:
                d[i][j] = array[i][j] + max(d[i - 1][j - 1], d[i][j - 1], d[i + 1][j - 1])
            # print(f"{i}, {j} : {d[i][j]}")

    # 마지막 열 중에서 가장 큰 것을 출력
    result = 0
    for i in range(n):
        result = max(result, d[i][m - 1])

    print(result)
