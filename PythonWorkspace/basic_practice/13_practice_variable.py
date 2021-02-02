gun = 10

def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))


#----------------------------------------------Quiz--------------------------------------------
# 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#  남자 : 키(m) x 키(m) x 22
#  여자 : 키(m) x 키(m) x 21

#  조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
#  조건2 : 표준 체중은 소수점 둘째자리까지 표시

#  (출력 예제)
#  키 175cm 남자의 표준 체중은 67.38kg 입니다.



# def std_weight(height, gender):
#     miter = height * 0.01
#     if gender == "남자":
#         gram = miter * miter * 22
#         return height, gram
#     elif gender == "여자":
#         gram = miter * miter * 21
#         return height, gram
#     else:
#         print("정체가 뭐야?")

# weight = std_weight(height, "남자")
# print("키 %dcm의 표준 체중은 %.2fkg 입니다.",height, weight)

def std_weight(height, gender): #키 m 단위 (실수), 성별 "남자" / 여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 #cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender),2) 
#round 반올림 std의 return 값을 weight라는 새로운 변수를 지정해서 받아준다.
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))