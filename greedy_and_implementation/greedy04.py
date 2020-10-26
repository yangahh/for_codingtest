# 문제) 큰 수의 법칙
# 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙. 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
# 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주.
# 예를 들어 순서대로 3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고, K가 2라고 가정하자.
# 이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다.
# 결과적으로 4 + 4 + 4 + 4 + 4 + 4 + 4인 28이 도출된다.
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하세요.

n, m, k = map(int, input().split())
data = list(map(int, input().split()))


# 가장 큰 수 2개 고르기
data.sort()
first = data[n-1]
second = data[n-2]

result = 0
'''
# 이 방법은 입력되는 수가 커지면 시간 초과가 됨
while True:

    for i in range(k): #1 2 3번째
        if m == 0:
            break
        result += first   # 6 + 6 + 6
        m -= 1  # 7 6 5
        

    if m == 0 : 
        break

    result += second # + 5
    m -= 1 # 4

print(result)  
'''

### 다른풀이(더 빠른 풀이) ###
# 수열 이용

roof_cnt = m // (k + 1)  # 반복되는 횟수
rest = m % (k + 1) # 수열이 반복되고 남은 횟수

# 가장 큰 수(first)가 더해지는 횟수
cnt = (roof_cnt * k) + rest

# (가장 큰 수*가장 큰 수가 더해지는 횟수) + (두번째 큰수 * 두 번째 큰 수 가 반복되는 횟수(=m에서 가장 큰 수가 더해지는 횟수 빼기))
result = (first * cnt) + (second * (m - cnt))


print(result)
