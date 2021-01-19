# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)

# import glob
# print(glob.glob("*.py")) #확장자가 py 인 모든 파일

# os : 운영체재에서 제공하는 기본 기능
import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td)

# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
import byme
byme.sign()

# (출력 예제)
# 이 프로그램은 안종찬이 만들었습니다.
# 유튜브 : http://youtube.com
# 이메일 : ajc212@naver.com