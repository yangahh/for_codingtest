# DFS, BFS 탐색 결과 출력하기
from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().rstrip().split())

# gragh = [[]]
# for _ in range(m):
#     gragh.append(list(map(int, sys.stdin.readline().rstrip().split())))

gragh = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    gragh[x][y] = 1
    gragh[y][x] = 1


dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)


def dfs(gragh, v):
    # 현재 노드 방문 처리
    dfs_visited[v] = 1
    print(v, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for node, yn in enumerate(gragh[v]):
        if yn == 1:
            if dfs_visited[node] == 0:
                dfs(gragh, node)


def bfs(gragh, v):
    # 큐 구현
    queue = deque()
    queue.append(v)

    # 현재 노드 방문 처리
    bfs_visited[v] = 1

    # 큐가 빌 때 까지 반복
    while queue:

        # 큐에서 원소 하나를 뺀다
        v = queue.popleft()
        print(v, end=" ")

        # 인접한 노드들 중 방문하지 않은 노드들은 큐에 넣는다
        for node, yn in enumerate(gragh[v]):
            if yn == 1:
                if bfs_visited[node] == 0:
                    queue.append(node)
                    bfs_visited[node] = 1


dfs(gragh, v)
print()
bfs(gragh, v)
