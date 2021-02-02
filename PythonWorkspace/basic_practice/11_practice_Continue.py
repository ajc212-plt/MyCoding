#Continue

from random import *


# absent = [2,5] # 결석
# no_book = [7] # 책을 분실함.
# for student in range(1, 11): #1 ~ 10
#     if student in absent:
#         continue # 밑에 있는 문장을 실행하지 않고 다음 반복으로 넘어감.
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은(는) 교무실로 따라와".format(student))
#         break #반복문을 탈출함.

#     print("{0}, 책을 읽어봐".format(student))

#     #출석번호가 1,2,3,4 앞에 100을 붙이기로 함. -> 101, 102, 103, 104
#     students = [1,2,3,4,5]
#     print(student)
#     students = [i+100 for i in students]#students 안에 값을 가져오면서 100을 더하라
#     print(students) # -> 101,102,103,104,105

#     #학생 이름을 길이로 변환
#     students = ["Iron man","Thor","I am groot"]
#     students = [len(i) for  i in students] #추출한 값의 길이를 출력
#     print(students)

#     #학생 이름을 대문자로 변환
#     students = ["Iron man","Thor","I am groot"]
#     students = [i.upper() for i in students]
#     print(students)


    #----------------------------------------------Quiz--------------------------------------------
    #  당신은 Cocoa 서비스를 이용하는 택시기사님입니다. 
    # 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

    # 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
    # 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

    # (출력문 예제)
    # [0] 1번째 손님 (소요시간 : 15분)
    # [ ] 2번째 손님 (소요시간 : 50분)
    # [0] 3번째 손님 (소요시간 : 5분)
    # ...
    # [ ] 50번째 손님(소요시간 16분)

    # 총 탑승객 2분
    # """




# total = 0
# for Customer in range(1,51) :
#     CustomerDt = randint(5,51)
#     print("[{0}]번째 손님(소요시간 : {1}분)".format(Customer, CustomerDt))
#     if 4< CustomerDt < 16 :
#         total += 1

# print("총 탑승객 : {0}명".format(total)) 


cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): #1~50이라는 수
    time = randrange(5,51) # 5분~50분 소요시간
    if 5 <= time <= 15 : # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요 시간 : {1}분)".format(i, time))
        cnt += 1
    else :
        print("[ ] {0}번째 손님 (소요 시간 : {1}분)".format(i, time))

print("총 탑승객 : {0}명".format(cnt)) 