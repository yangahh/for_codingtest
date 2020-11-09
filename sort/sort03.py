n = int(input())
info = []

for i in range(n):
    input_data = input().split()
    info.append((input_data[0], int(input_data[1])))

# info.sort(key = lambda x : x[1])
info = sorted(info, key = lambda info: info[1])

for student in info:
    print(student[0], end=" ")