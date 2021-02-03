#pip install selenium 설치
from selenium import webdriver
import time

browser = webdriver.Chrome() #()안에는 Chromedriver가 설치되어있는데 폴더경로를 써야함.
                             #같은 폴더에 있을 경우 빈칸 or "./chromedriver.exe"으로 해놔도 상관없음

#1. 네이버 이동
browser.get("http://naver.com")

#2. 로그인 버튼
elem = browser.find_element_by_class_name("link_login")
elem.click()


#3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

#5. id를 새로 입력
#browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#6. html 정보 출력
print(browser.page_source)

time.sleep(10)

browser.quit()




