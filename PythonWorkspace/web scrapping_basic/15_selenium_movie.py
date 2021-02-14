import requests
from bs4 import BeautifulSoup



url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Accept-Language":"ko-KR,ko" #대소문자 맞춰줘야함.
    }
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html","w",encoding="utf-8") as f:
#     #f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 작성
#     #User Agent로 접속해야 해당 사용자 설정에 맞게 뜨나, 그렇지 않다면 홈페이지 기본설정으로 뜸.(ex 구글같은 미국에서 접속한게 기본설정으로 맞춰서 나옴)

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)