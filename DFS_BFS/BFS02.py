# 문제) 특정 거리의 도시 찾기 (https://www.acmicpc.net/problem/18352)
# 입력 : 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
# 출력 : X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
#       이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
from collections import deque
import sys

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in gragh[v]:
            print(i)
            if not visited[i]:
                queue.append(i)
                visited[i] == True
                distance[i] = distance[v] + 1


n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
gragh = []
for _ in range(m):
    gragh.append(list(map(int, input().split())))


visited = [False] * (n + 1)
distance = [0] * (n + 1) 


                
bfs(x)

for i in range(n):
    if distance[i] == k:
        print(i)
if k not in distance:
    print(-1)