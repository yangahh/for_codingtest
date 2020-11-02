# 문제) 경쟁적 전염 (https://www.acmicpc.net/problem/18405) 다시풀기


from collections import deque

def bfs(gragh, a, b, k):
    # 큐를 구현하기 위해 deque라이브러리 사용
    queue = deque()
    queue.append((a, b))
    
    # 방향 벡터(상, 하, 좌, 우) 설정
    da = [-1, 1, 0, 0]
    db = [0, 0, -1, 1]

    second = 0
    
    while queue:
        a, b = queue.popleft()
        second += 1
        # 상, 하, 좌, 우 탐색
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            
            # 다음 좌표가 범위를 벗어나면 무시
            if na < 0 or na >= n or nb < 0 or nb >= n:
                continue
            # 다음 좌표에 바이러스가 퍼지지 않은 경우
            if gragh[na][nb] == 0:
                gragh[na][nb] = k
                queue.append((na, nb))
         
        # 주어진 시간이 지나면 탐색 종료
        if second == s:
            break
    return gragh

n , k = map(int, input().split())
gragh = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

# 각 바이러스 별 위치 정보를 저장(2차원 리스트로 [바이러스 번호, 행 번호, 열 번호]). (0행은 무시하는 행)
virus = [[0, 0, 0]]

for i in range(n):
    for j in range(n):
        if gragh[i][j] != 0:
            virus.append([gragh[i][j], i, j])

# 바이러스 번호 순으로 정렬
virus.sort(key = lambda x: x[0])

# 바이러스 번호가 작은 순서대로 탐색
for i in range(1, k+1):
    bfs(gragh, virus[i][1], virus[i][2], virus[i][0])
    for xx in range(n):
        for yy in range(n):
            print(gragh[xx][yy], end=" ")
        print()
    print()

print(gragh[x-1][y-1])
    