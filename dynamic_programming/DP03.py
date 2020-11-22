# 문제) 효율적인 화폐 구성
# n가지 종류의 화폐. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 m원이 되도록
# 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분.

# 금액 i를 만들 수 있는 최소한의 화폐 개수를 a(i), 화폐의 단위를 k라고 했을 때
# a(i) = min(a(i), a(i-k) + 1)
# ** 주어진 각 화폐 단위별로 갱신해야함

n, m = map(int, input().split())  # 2, 15
array = []  # 2, 3

for i in range(n):
    array.append(int(input()))

# DP테이블 초기화. 최소값을 구해야 하기 때문에 초기값을 10000보다 크게 잡아줌(더 큰 수여도 상관 없음)
# 즉, 10001이라면 금액 i를 만들 수 없다는 뜻
d = [10001] * (m + 1)
d[0] = 0

# 화폐 단위 하나씩
for coin in array:
    for i in range(coin, m + 1):
        d[i] = min(d[i], d[i - coin] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
