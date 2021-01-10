# with

import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file)) #close해줄 필요가 없다.

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt","r", encoding="utf8") as study_file:
#     print(study_file.read())


# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

# 조건 : 파일명 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# work = {"부서":"백엔드", "이름":"안종찬","업무 요약" : "공부중"}
# for weakly in range(1,51):
#     with open("{0}주차.txt".format(weakly), "w", encoding="utf8") as workform:
#         for title, memo in work:
#             workform.write(title.ljust(10), sep="") 
#             workform.write(memo.rjust)
        
for i in range(1,51):
    with open(str(i) + "주차.txt","w", encoding="utf") as report_file:
        report_file.write(" -- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 :")
