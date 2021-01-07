cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

#print(cabinet.get(3))
#print(cabinet[5]) #캐비넷에서 오류가 뜨면 다음 문구는 실행되지 않는다.
#print("hi") # 실행되지 않음.
# print(cabinet.get(5)) #-> 5의 value를 찾아보고 없으면 NONE
# print(cabinet.get(5,"사용 가능")) #-> 5의 value를 찾아보고 없으면 뒤에 값을 띄워준다.
# print("hi") #-> 위 내용의 값이 없어도 프로그램 실행이 종료되지 않기 때문에 출력 가능

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"} #String도 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())
print(cabinet)

#목욕탕 폐점
cabinet.clear()
print(cabinet)