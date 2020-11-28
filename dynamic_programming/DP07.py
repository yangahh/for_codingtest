# 문제) 병사 배치하기 (https://www.acmicpc.net/problem/18353)
# (https://www.acmicpc.net/problemset?sort=no_asc&author=ndb796&author_type=1)
# 무작위로 N명의 병사가 있음. 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
# 병사에 대한 정보가 주어졌을 때, 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외해야 하는 병사의 수를 출력하는 프로그램을 작성

import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))

# 내림차순 정렬을 위해 입력받은 배열을 뒤집어서 가장 긴 증가하는 부분 수열(LIS) 알고리즘을 적용
array.reverse()

# DP 테이블 초기화
d = [1] * (n + 1)

# DP 탐색
for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))