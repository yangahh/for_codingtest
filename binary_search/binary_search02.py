# 문제) 부품 찾기
import sys

n = int(sys.stdin.readline().rstrip())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
requests = list(map(int, sys.stdin.readline().rstrip().split()))


parts = sorted(parts)
print(parts)
start = 0
end = n - 1

results = ["empty"] * m


for i in range(m):
    # 이진 탐색
    while start <= end:
        mid = (start + end) // 2
        
        if parts[mid] == requests[i]:
            print("yes", end=" ")
            break
        elif parts[mid] >= requests[i]:
            end = mid - 1
        else:
            start = mid + 1
    print("no", end=" ")

