# 1, 2, 3 합으로 표현

# 점화식
# d[n] = d[n - 1] + d[n - 2] + d[n - 3]

T = int(input())

for _ in range(T):
    n = int(input())

    d = [0] * 12

    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, 12):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]

    print(d[n])
