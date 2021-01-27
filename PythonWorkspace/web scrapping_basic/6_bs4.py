#beautifulsoup4

import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
#print(soup.a) #첫번째로 발견된 a태그를 출력
# print(soup.a.attrs) #a element의 속성 정보를 출력
# print(soup.a["href"]) #a element의 href "값" 정보를 출력 할 수 있다.

#print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 a element 를 찾아줘
# #soup 객체 내에 있는 모든 내용 중에서 해당하는 첫 번째 element
# 뒤에 나오는 전부 해당하는 값중에 처음으로 발견되는 a가져올 수 있다.
#print(soup.find(attrs={"class":"Nbtn_upload"})) #class="Nbtn_upload" 인 어떤 element를 찾아줘

#print(soup.find("li",attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a) #rank에서 찾아온 값에서 a element만 출력
# print(rank1.a.get_text())
# print(rank1.next_sibling) #next_sibling 다음 형제 태그로 넘어감 rank01 -> rank02
#next_sibling을 했는데 아무 내용이 나오지 않는다면 해당 태그들 사이에 개행이 있어서 안나올수 있다.
rank2 = rank1.next_sibling.next_sibling #그럴땐 2번 써주면 된다.
#rank3 = rank2.next_sibling.next_sibling
print(rank2.a.get_text())

