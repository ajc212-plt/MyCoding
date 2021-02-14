from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동



#가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# # 이번달 27일,28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

# # 다음달 27일,28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 이번달 27일,다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

#제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    # 페이지 검색시 특정구간에서 로딩시간이 있을경우
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))) 
    # 브라우저를 최대 10초까지 대기하는데 XPATH기준으로 이 "//*[@id='content']/div[2]/div/div[4]/ul/li[1]" 에 
    # 해당하는 엘리먼트(EC.presence_of_element_located)가 나올때까지
    
    #성공했을때 동작 수행
    print(elem.text) #첫번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 클릭
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)

time.sleep(1000)