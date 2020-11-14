# 문제) 부품 찾기
import sys

n = int(sys.stdin.readline().rstrip())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
requests = list(map(int, sys.stdin.readline().rstrip().split()))


parts = sorted(parts)


def bin_search(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] > target :
            end = mid - 1
        else:
            start = mid + 1
    
    return False


for request in requests:
    # 이진 탐색
    result = bin_search(parts, request, 0, n - 1)

    if result:
        print("yes", end=" ")
    else:
        print("no", end=" ")
   

