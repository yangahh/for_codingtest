# 문제) 정렬된 배열에서 특정 수의 개수 구하기
# N(1 <= N <= 1,000,000)개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
# 이때 이 수열에서 x(-10^9 <= x <= 10^9)가 등장하는 횟수를 출력 (하나도 없는 경우 -1 출력)
# 단, 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받는다.
# 즉 일반적인 선형 탐색으로는 시간 초과 판정을 받음
# 문제에서 정렬된 데이터, N의 범위를 통해 이진탐색을 수행해야 함을 알 수 있다.

from bisect import bisect_left, bisect_right
import sys

n, x = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

result = bisect_right(array, x) - bisect_left(array, x)

if result == 0:
    print(-1)
else:
    print(result)