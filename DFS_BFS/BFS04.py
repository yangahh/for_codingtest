# 문제) 감시 피하기 (https://www.acmicpc.net/problem/18428)

# 문제 해결 아이디어
# 장애물 3개를 설치하는 모든 경우를 확인하며, 매 경우마다 모든 학생을 감시로부터 피할 수 있는지 체크
# 복도의 크기는 N * N(N은 최대 6) >> 모든 조합의 수는 최악의 경우 36C3 >> 경우의 수가 10,000 이하이므로 모든 조합을 고려하여 완전 탐색을 수행하여 해결
# 모든 조합을 찾을 때에는 DFS/BFS를 이용하거나 조합 계산 라이브러리를 사용할 수 있다.

from itertools import combinations

n = int(input())
map = []
teachers = [] # 선생님(=T) 위치 저장
spaces = [] # 빈 공간(=X) 위치 저장

for i in range(n):
    map.append(list(input().split()))
    for j in range(n):
        if map[i][j] == 'T':
            teachers.append((i, j))
        elif map[i][j] == 'X':
            spaces.append((i, j))

# 상, 하, 좌, 우 4방향 탐색
def search_4d(x, y, i):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while True:
        # 범위를 벗어나면 반복문 나가기
        if x < 0 or x >= n or y < 0 or y >= n:
            break

        if map[x][y] == 'S': # 학생을 발견한 경우
            return True
        elif map[x][y] == 'O': # 장애물이 있는 경우
            return False
        x += dx[i]
        y += dy[i]

    # 그 줄에 T만 있어서 결국에 학생을 못 발견한 경우
    return False




def check(map): # 발견하면 True, 발견 못하면 False 반환
    for x, y in teachers:
        # 상, 하, 좌, 우 방향으로 하나씩 탐색
        for i in range(4):
            if search_4d(x, y, i): # 학생 발견
                return True

    return False




# 학생이 감지 되었는지(감지 되었으면 False, 감지 되지 않으면 True)
hide = False

# 빈 공간에서 3개를 뽑아서 모든 조합 확인
for obstacle in combinations(spaces, 3):
    for x, y in obstacle:
        # 빈 공간에 장애물 설치
        map[x][y] = 'O'
    
    # 장애물 1세트(3개)씩 학생을 발견했는지 체크
    if not check(map): # 학생을 발견하지 못한 경우
        hide = True
        break
    
    # 감지를 못한 경우 다음 경우를 위해 설치한 장애물 없애기(초기상태로 돌리기)
    for x, y in obstacle:
        map[x][y] = 'X'



if hide:
    print('YES') 
else:
    print('NO')   