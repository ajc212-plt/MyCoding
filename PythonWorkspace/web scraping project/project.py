# Project) 웹 스크래핑을 이용하여 나만의 비서를 만드시오

# [조건]
# 1. 네이버에서 오늘 서울의 날씨 정보를 가져온다.
# 2. 헤드라인 뉴스 3건을 가져온다
# 3. IT뉴스 3건을 가져온다.
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다.

# [출력 예시]

# [오늘의 날씨]
# 흐림, 어제보다 OOº 높아요
# 현재 OOºC (최저 OOº/ 최고 OOº)
# 오전 강수확률 OO% / 오후 강수확률 OO%

# 미세먼지 OO
# .......

import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def print_news(index, title, link):
    print("{}.{}".format(index+1, title))
    print(" (링크 : {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    url ="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    #맑음, 어제보다 3도 낮아요
    cast = soup.find("p",attrs={"class":"cast_txt"}).get_text()

    #현재 OOºC (최저 OOº/ 최고 OOº)
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp = soup.find("span",attrs={"class":"min"}).get_text()
    max_temp = soup.find("span",attrs={"class":"max"}).get_text()

    # 오전 강수확률 OO% / 오후 강수확률 OO%
    morning_rain_rate = soup.find("span",attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span",attrs={"class":"point_time afternoon"}).get_text().strip()

    # 미세먼지 38㎍/㎥보통
    # 초미세먼지# 11㎍/㎥좋음
    # 오존지수# 0.024ppm좋음
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text() #미세먼지
    pm25 = dust.find_all("dd")[1].get_text() #초미세먼지

    # 출력
    print(cast)
    print("현재 {} (최고 {} / 최저 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()


# print("[헤드라인 뉴스]")
    # url ="https://news.naver.com"
    # soup = create_soup(url)
    # news_list = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li")
    # for index, news in enumerate(news_list):
    #     title = news.find("a").get_text().strip()
    #     link = url + news.find("a")["href"]
    #     print("{}. {}".format(index+1,title))
    #     print("(링크 : {})".format(link))
    # print()

def scrape_headline():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li",limit=3) #limit = 3 -> 3개까지만 찾아라
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=3) #3개까지
    for index, news in enumerate(news_list):
        a_idx=0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a태그의 정보를 사용

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div",attrs={"id":re.compile("^conv_kor_t")}) #re.compile("^conv_kor_t") conv_kor_t로 시작하는 어떤 값을 가지는 ID의 DIV태그를 모두 가져올수 있다
    print("[영어 지문]")
    for sentence in sentences[len(sentences)//2:]: #8문장이 있다고 가정할 때, index 기준 4~7까지 잘라서 가져옴
        print(sentence.get_text().strip())
    
    print()
    print("[한글 지문]")
    for sentence in sentences[:len(sentences)//2]: #8문장이 있다고 가정할 때, index 기준 0~3까지 잘라서 가져옴
        print(sentence.get_text().strip())
    print()

    
    
    
if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline() # 헤드라인 뉴스 정보 가져오기
    scrape_it_news() # IT 뉴스 정보 가져오기
    scrape_english() # 오늘의 영어회화 가져오기