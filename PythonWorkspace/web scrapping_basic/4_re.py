#정규식 (정해진 규칙)
#주민등록번호
#900110-123548 ok, 900110-fdfd123 no

#이메일 주소
#ajc212@naver.com ok
#ajc212@naver@gmail.com no

import re



p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 > care, came, case | caffe(x)
# ^ (^de)  : 문자열의 시작 > desk, destination | fade(x)
# $ (se$)  : 문자열의 끝 > case, base | face (x)

def print_match(m):
#print(m.group()) # 매칭되면 출력, 매치되지 않으면 에러가 발생함.
    if m:
        print("m.group():",m.group()) # 일치하는 문자열 반환
        print("m.string: ", m.string) # 입력받은 문자열 그대로 반환
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():",m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음.")

# m = p.match("careless") #match 주어진 문자열의 처음부터 일하는지 확인
# print_match(m)

#m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
#print_match(m)

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 1. p = re.complie("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열 ") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식 (w3schools.com) 정규식 Python RegEx, docs.python.org -> Regular expression operations
# . (ca.e) : 하나의 문자를 의미 > care, came, case | caffe(x)
# ^ (^de)  : 문자열의 시작 > desk, destination | fade(x)
# $ (se$)  : 문자열의 끝 > case, base | face (x)