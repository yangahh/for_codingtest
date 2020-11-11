# 1. 재귀 함수로 구현한 이진 탐색 코드

def binary_search_recursive(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, end)

def binary_search_loop(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# n : 원소의 개수, target : 찾고자 하는 문자열
n, target = map(int, input().split())
# array : 전체 원소
array = list(map(int, input().split()))

result = binary_search_recursive(array, target, 0, n - 1)
result2 = binary_search_loop(array, target, 0, n -1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

if result2 == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

