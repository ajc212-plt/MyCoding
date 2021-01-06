sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "991011-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전까지 (0,1)값만 가져옴
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지(0,1,2,3,4)
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지

print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) #0번째 문자가 대문자가 맞으면 True, 아니면 False
print(len(python)) #문자열 길이
print(python.replace("Python","Java"))

index = python.index("n") 
# python = "Python is Amazing" 에서 n이 몇번째 위치에 나오는지 찾기
print(index)
index = python.index("n",index +1) 
#python = "Python is Amazing" 에서 두번째 n이 몇번쨰 위치에 나오는지 찾기
print(index)

print(python.find("g")) 
#find는 원하는 글자 찾아주고, 없는 글자를 찾으면 -1을 리턴해주고 프로그램은 계속 실행
#print(python.index("JAVA")) #index는 원하는 글자가 없을 경우 오류가 나고 실행 종료

print(python.count("n")) #n이 총 몇번 나오는지 확인 = 2



print("a" + "b")
print("a","b")

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % "A")

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {color}살이며, {age}색을 좋아해요.".format(age = 20, color="빨간"))

#방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

                                    
                                    #탈출 문자

#\n: 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

#\" \' : 문장 내에서 따옴표
#저는 안종찬입니다.
print('저는 "안종찬" 입니다')
print("저는 '안종찬' 입니다")
print("저는 \"안종찬\" 입니다.") 
print("저는 \'안종찬\' 입니다.") 

#\\ : 문장 내에서 \
print("D:\\Data\\Study\\Connect_Github\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") 
# Pine(0,1,2,3)만큼의 문자열이 맨 앞으로 이동하여 기존 글자와 변경
# Red□(0,1,2,3)을 Pine 으로 변경해서 -> PineApple이라는 결과값이 나옴

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")



# Quiz) 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#             (nav)                   (5)             (1)       (!)

# 예) 생성된 비밀번호 : nav51!


# hint = "http://naver.com"
# first = hint[7:]
# print(first)
# second = first.replace(".com","")
# print(second)
# print("생성된 비밀번호는 : ", second[0:3]+str(len(second))+str(second.count("e"))+"!")

url = "http://naver.com"
my_str = url.replace("http://", "") #규칙1
#print(my_str)
my_str = my_str[:my_str.index(".")] #규칙2
#my_str = naver.com 에서 . 직전까지만 나오게
#print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

