# 키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

def profile1(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
    #end=" " -> 줄바꿈을 하지 않고 밑에 있는 문장을 이어서 출력
    print(lang1, lang2, lang3, lang4, lang5)

profile1("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile1("김태호", 25, "kotlin", "Swift", "","","")

#가변 인자

def profile2(name, age, *language): #다른 갯수의 변수가 들어와도 출력 가능
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
    for lang in language :
        print(lang, end=" ")
    print()

profile2("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile2("김태호", 25, "kotlin", "Swift")