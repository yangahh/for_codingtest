# 문제) 음료수 얼려 먹기
# N * M 크기의 얼음 틀에서 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램이르 작성하시오

n, m = map(int, input().split())
gragh = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    # 재귀 호출 시 오류 처리(얼음판 범위를 벗어나는 경우)
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # DFS로 특정 노드를 방문처리한 뒤, 해당 노드와 연결된(상, 하, 좌, 우) 노드들을 방문
    if gragh[x][y] == 0:
        # 해당 노드 방문 처리
        gragh[x][y] = 1
        # 상, 하, 좌, 우 노드 탐색 (재귀적으로 호출)
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True


    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)



