# 문제) 떡볶이 떡 만들기
# 떡의 개수: N, 손님이 요청한 떡의 길이: M
# 떡 절단기 높이인 h의 최대 값을 출력

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
h = 0

# 이진 탐색 수행
while (start <= end):
    total = 0
    mid = (start + end) // 2

    for x in array:
        # 절단기 높이가 떡의 길이보다 짧을 때만 떡을 자른다
        if x > mid:
            total += (x - mid)

    # 떡의 양이 부족한 경우 >> 왼쪽 탐색
    if total < m:
        end = mid - 1
    
    # 떡의 양이 넘치는 경우 >> 값 저장 후(이게 적정 값일 수 있으므로) 오른쪽 탐색
    else:
        h = mid
        start = mid + 1

print(h)