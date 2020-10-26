# 문제) 문자 재배열
# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

data  = input()
alpha = []
num = 0
# print(datas)

for x in data:
    if x.isalpha():
        alpha.append(x)
    else:
        num += int(x)

alpha.sort()


# 리스트를 문자열로 변환하여 출력 + 더한 숫자는 문자열로 변환하여 출력
print(''.join(alpha) + str(num))
