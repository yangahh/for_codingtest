# https://www.acmicpc.net/problem/1463
# 1로 만들기

n = int(input())

# dp 테이블 초기화
d = [0] * (n + 1)
# d[i] : 숫자 i를 1로 만드는 최소 연산 횟수

# dp테이블 갱신(보텀업 방식)
for i in range(2, n + 1):

    # 1을 빼는 연산
    d[i] = d[i - 1] + 1

    # 2로 나누는 연산을 할 경우>> 더 작은 값으로 갱신
    if(i % 2 == 0):
        d[i] = min(d[i], d[i // 2] + 1)

    # 3로 나누는 연산을 할 경우>> 더 작은 값으로 갱신
    if(i % 3 == 0):
        d[i] = min(d[i], d[i // 3] + 1)

print(d[i])
