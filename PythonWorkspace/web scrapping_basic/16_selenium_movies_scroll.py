#할인된 영화 목록만 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)


# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 2560 x 1080
# browser.execute_script("window.scrollTo(0, 2080)") # 2560 x 1080

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    #페이지 로딩 대기
    time.sleep(interval)

    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight") 
    if curr_height == prev_height:
        break
    
    prev_height = curr_height #현재 문서 높이를 prev_height 에 저장 후 while문으로 다시 실행하면서 계속해서 스크롤을 내려감.

print("스크롤 완료")


soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    #할인전 가격
    original_price = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title," <할인되지 않은 영화 제외> ")
        continue

    #할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크 정보
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 : https://play.google.com + link

    print(f"제목 :{title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할이 후 금액 : {price}")
    print("링크 : ","https://play.google.com" + link)
    print("-"*100)

browser.quit()
# time.sleep(1000)

