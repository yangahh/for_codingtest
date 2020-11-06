data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(data, start, end):
    if start >= end: # 원소가 1개인 경우 함수 종료
        return
    pivot = start   # 0, 7
    left = start + 1  # 1, 5
    right = end # 9, 8

    while left <= right:

        # 왼쪽에서부터 피벗보다 큰 데이터를 찾을 때 까지 반복
        while data[pivot] >= data[left] and left <= end:
            left += 1
        
        # 오른쪽에서 부터 피벗보다 작은 데이터를 찾을 때 까지 반복
        while data[pivot] <= data[right] and right > start:
            right -= 1
        
        
        # if left <= right:
        #     data[left], data[right] = data[right], data[left]
        #     print(data)
        # else:
        #     data[right], data[pivot] = data[pivot], data[right]
        #     print("else")
        #     print(data)

        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    quick_sort(data, start, right - 1)
    quick_sort(data, right + 1, end)


quick_sort(data, 0, len(data)-1)
print(data)
