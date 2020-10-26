# 문제) 시각 (완전 탐색 유형)
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오
import time, datetime
n = int(input())
cnt = 0
'''
# str_to_time = datetime.datetime.strptime("000000", "%H%M%S")  # strptime(string, format) : 문자열을 지정된 포맷의 시간으로
# 시간.strftime(format) : 시간을 지정된 포맷의 문자열로
# start_time = time.strftime('%H%M%S', time.strptime('121212', '%H%M%S'))


# print(type(str(str_to_time.hour)))
# print(str_to_time.minute)
# print(str_to_time.second)

# # x = start_time + datetime.timedelta(seconds=1)
# # print(str(x))
# end_time = n + "5959"

# 문자열 > (여기서 부터 반복) 시간 > 1초더하기 > 문자열로 다시 변환 > 3들어있는지 체크 > count + 1 > (반복. N시 59분 59초 까지)


start_str_to_time = datetime.datetime.strptime("000000", "%H%M%S")
end = n + "5959"
end_str_to_time = datetime.datetime.strptime(end, "%H%M%S")

while True:
    start_str_to_time += datetime.timedelta(seconds=1)
    time_to_str = str(start_str_to_time.hour) + str(start_str_to_time.minute) + str(start_str_to_time.second)
    for x in time_to_str:
        if x == '3':
            cnt += 1
    
    if start_str_to_time > end_str_to_time:
        break
'''
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1


print(cnt)