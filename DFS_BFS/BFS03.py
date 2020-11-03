# 문제) 경쟁적 전염 (https://www.acmicpc.net/problem/18405) 다시풀기


from collections import deque
import sys

n , k = map(int, sys.stdin.readline().rstrip().split())
gragh = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
target_s, target_x, target_y = map(int, sys.stdin.readline().rstrip().split())

# 각 바이러스 별 위치 정보를 저장(2차원 리스트로 [바이러스 번호, 초, 행 번호, 열 번호]). (초는 0으로 초기화)
virus = []

for i in range(n):
    for j in range(n):
        if gragh[i][j] != 0:
            virus.append([gragh[i][j], 0, i, j])

# 바이러스 번호 순으로 정렬 (첫번째 원소를 기준으로 정렬)
virus.sort()
# virus.sort(key = lambda x: x[0]) 같은 표현

# 바이러스 정보를 큐에 넣어 탐색
queue = deque(virus)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


while queue:
    v_num, s, x, y = queue.popleft()

    if s == target_s:
        break

    # 상, 하, 좌, 우 BFS 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 좌표 범위를 벗어나면 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if gragh[nx][ny] == 0:
            gragh[nx][ny] = v_num
            queue.append([v_num, s+1, nx, ny])
            


print(gragh[target_x - 1][target_y - 1])
    