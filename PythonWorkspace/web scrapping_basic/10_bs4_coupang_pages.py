#
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"} # 접속하는 유저의 환경정보를 입력해서 사이트가 접속을 막지 않는다.

n = int(input())

for i in range(1,n+1): #1~입력한 숫자 페이지까지
    print("페이지 :",i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) #자동으로 li 클래스 중에서 search-product라고  나오는 모든 정보를 가져옴

    for item in items:

        #광고 제품은 제외
        ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print(" <광고 상품 제외합니다.>")
            continue

        name = item.find("div",attrs={"class":"name"}).get_text()

        #애플 제품 제외
        if "Apple" in name:
            # print(" <Apple 상품 제외합니다.>")
            continue

        price = item.find("strong",attrs={"class":"price-value"}).get_text()
        
        #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em",attrs={"class":"rating"})
        if rate: #평점이 있으면 text로 출력
            rate = rate.get_text()
        else:
            # print(" <평점 없는 상품 제외합니다.>")
            continue
        
        rate_cnt = item.find("span",attrs={"class":"rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1] # 예: (26)
             # 0 1번째 인덱스부터 -1(맨뒤)인덱스까지 ()없애기
        else:
            # print(" <평점 수 없는 상품 제외합니다.>")
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            #print(name, price, rate,rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개")
            print("바로가기 : {}".format("https://www.coupang.com"+link))
            print("-"*100) #줄긋기


print("github Saving")