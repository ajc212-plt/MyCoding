# user_agent , site -> google 검색: user agent string -> What is my User Agent
# 접속한 유저 정보 확인. Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
# 웹사이트에서는 접속하는 사용자의 정보를 알 수 있음. 접속하는 사용자 정보에 따라 웹사이트에서 제공하는 정보가 달라짐
# 하지만 웹크롤링으로 접속하는 경우 사이트 내에서 접속을 차단할 수 있다.


import requests
url = "https://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

print(len(res.text))
print(res.text)

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)