# 문제) 미로 탈출 (최단 거리)
# N * M 크기의 직사각형 형태의 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 시작 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 칸씩 이동할 수 있다.
# 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
# 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
from collections import deque

n, m = map(int, input().split())
gragh = []
for i in range(n):
    gragh.append(list(map(int, input())))


def bfs(x, y):
    # 방향 벡터(상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 큐를 구현하기 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치를 기준으로 연결되어 있는 상, 하, 좌, 우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx, ny가 미로 찾기 범위를 넘어가면 무시하기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if gragh[nx][ny] == 0:
                continue
            elif gragh[nx][ny] == 1:
                gragh[nx][ny] = gragh[x][y] + 1
                queue.append((nx, ny))
    
    return gragh[n-1][m-1]

print(bfs(0, 0))

        
