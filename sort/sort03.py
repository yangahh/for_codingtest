n = int(input())
info = []

for i in range(n):
    info.append(input().split())
    info[i][1] = int(info[i][1])

# info.sort(key = lambda x : x[1])
info = sorted(info, key = lambda info: info[1])

for i in range(n):
    print(info[i][0], end=" ")