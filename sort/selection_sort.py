data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(data)):
    # 맨 앞에 있는 원소의 인덱스
    min_index = i

    # i 번째 원소 이후의 원소들 중 가장 작은 원소의 인덱스를 찾아서 min_index 값을 바꿔준다
    for j in range(i + 1, len(data)):
        if data[min_index] > data[j]:
            min_index = j
    
    # 갱신된 min_index의 원소와 맨 앞에 있는 원소(i)를 스와프
    data[min_index], data[i] = data[i], data[min_index]
        

print(data)