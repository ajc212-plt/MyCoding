#
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1~200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") #newline="" 을 주면 자동으로 줄바꿈이 생기지 않는다.
                        #exel에서는 euc-kr or utf-8-sig로 저장해야 글이 깨지지않는다.
                        #utf-8-sig는 엑셀이나 vs에서 열어도 깨지지 않는다.
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", "현재가", ...]
print(type(title))
writer.writerow(title)

for page in range(1, 2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: #의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns] #.strip() -> 공백 제거
        # print(data)
        writer.writerow(data)


print("github Saving")