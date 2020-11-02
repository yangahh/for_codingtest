# 문제) 특정 거리의 도시 찾기 (https://www.acmicpc.net/problem/18352)
# 입력 : 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
# 출력 : X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
#       이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
from collections import deque

n, m, k, x = map(int, input().split())
# 도로 정보를 저장할 2차원 배열. (각 행 번호 == 도시 번호, 값 == 연결된 도시 번호)
gragh = [[] for _ in range(n+1)] 

for _ in range(m):
    a, b = map(int, input().split())
    gragh[a].append(b) 

# 방문처리
visited = [False] * (n + 1)
# 도시간의 거리 (0으로 초기화)
distance = [0] * (n + 1)


queue = deque()
queue.append(x)
# 선언과 동시에 원소 추가하는 방법
# queue = deque([x])
visited[x] = True

while queue:
    now = queue.popleft()
    for adj_city in gragh[now]:
        if not visited[adj_city]:
            queue.append(adj_city)
            visited[adj_city] = True
            distance[adj_city] = distance[now] + 1


for i in range(1, n+1):
    if distance[i] == k:
        print(i)
if k not in distance:
    print(-1)

