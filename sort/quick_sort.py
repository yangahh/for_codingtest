data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(data, start, end):
    if start >= end: # 원소가 1개인 경우 함수 종료
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:

        # 왼쪽에서부터 피벗보다 큰 데이터를 찾을 때 까지 반복
        while data[left] <= data[pivot] and left <= end:
            left += 1
        
        # 오른쪽에서 부터 피벗보다 작은 데이터를 찾을 때 까지 반복
        while data[right] >= data[pivot] and right > start:
            right -= 1
        
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    quick_sort(data, start, right - 1)
    quick_sort(data, right + 1, end)


quick_sort(data, 0, len(data)-1)
print(data)
