n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)
for i in a:
    print(i, end=" ")
