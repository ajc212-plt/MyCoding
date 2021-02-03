#

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"} # 접속하는 유저의 환경정보를 입력해서 사이트가 접속을 막지 않는다.
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) #자동으로 li 클래스 중에서 search-product라고  나오는 모든 정보를 가져옴

#print(items[0].find("div",attrs={"class":"name"}).get_text())
for item in items:

    #광고 제품은 제외
    ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품 제외합니다.>")
        continue

    name = item.find("div",attrs={"class":"name"}).get_text()

    #애플 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다.>")
        continue

    price = item.find("strong",attrs={"class":"price-value"}).get_text()
    
    #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em",attrs={"class":"rating"})
    if rate: #평점이 있으면 text로 출력
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품 제외합니다.>")
        continue
    
    rate_cnt = item.find("span",attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() # 예: (26)
        rate_cnt = rate_cnt[1:-1] # 0 1번째 인덱스부터 -1(맨뒤)인덱스까지 ()없애기
        #print("리뷰 수", rate_cnt)
    else:
        print(" <평점 수 없는 상품 제외합니다.>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate,rate_cnt)



print("github Saving")