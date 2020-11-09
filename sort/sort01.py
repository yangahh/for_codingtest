# 문제) 두 배열의 원소를 최대 k번 교체. a 배열 원소의 합이 최대로 나오게
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

# a는 오름차순으로 정렬, b를 내림차순으로 정렬 후 k번 차례대로 원소 바꾸기

a.sort()
b.sort(reverse=True)


for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: 
        break

    
print(sum(a))