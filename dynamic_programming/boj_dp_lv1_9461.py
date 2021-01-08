# 파도반 수열
# 런타임에러 나는 이유 >> n = 1인 경우를 생각하자!! >> p 테이블 초기화 할때 [0] * (n+1) 보다 [0] * 101로 하는게 좋다

T = int(input())

for _ in range(T):

    n = int(input())
    p = [0] * 101

    p[1] = 1
    p[2] = 1
    p[3] = 1

    for i in range(4, n + 1):
        p[i] = p[i - 2] + p[i - 3]

    print(p[n])
