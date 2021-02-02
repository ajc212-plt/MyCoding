#표준 입출력

print("Python","Java",sep=",",end="?") #sep=" " 안에 내용이 , 대신 들어간다 end는 다음 문장을 내리지 않고 
                                       #해당 문장을 "" 안의 문자를 출력한다.
print("무엇이 더 재밋을까요?")

import sys
# print("Python","Java",file=sys.stdout) #stdout 표준출력
# print("Python","Java",file=sys.stderr) #stderr 표준에러

#시험성적
# scores = {"수학":0, "영어":50,"코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4),sep=":") 
    #ljust() -> 왼쪽 정렬을 하는데 ()안에 들어간 숫자만큼 칸을 확보 <-> rjust

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호:" +str(num).zfill(4))
#  #zfill() 안에 숫자만큼 칸을 확보하고 빈공간은 0으로 채워준다

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
