# 시간초과 주의!!! >> 되도록이면 인접 행렬 사용할 것
import sys
from collections import deque

# 정점의 개수 N과 간선의 개수 M
n, m = map(int, sys.stdin.readline().rstrip().split())

gragh = [[] for _ in range(n + 1)]


# 인접 리스트(인접 행렬보다 느리고 메모리는 적게든다)
for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    gragh[x].append(y)
    gragh[y].append(x)

visited = [0] * (n + 1)


def bfs(start):
    queue = deque()
    queue.append(start)

    visited[start] = 1

    while queue:
        v = queue.popleft()
        # 인접한 노드들 중 방문하지 않은 노드를 큐에 넣고 방문처리
        for i in gragh[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


cnt = 0
for i in range(1, n + 1):
    # 모든 노드 차례대로 bfs
    if visited[i] == 0:
        bfs(i)
        # 인접한 노드라면 cnt가 올라가지 않음
        cnt += 1

print(cnt)
