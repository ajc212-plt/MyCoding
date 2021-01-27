# requests 해당 웹사이트의 정보를 받아오는지 확인

import requests
res = requests.get("http://google.com")
#res = requests.get("https://nadocoding.tistory.com")
res.raise_for_status()
#print("응답코드 : ",res.status_code) #200점이면 정상, 403이면 접근권한 없음.

# if res.status_code == requests.codes.ok: # ok = 200 
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ",res.status_code,"]")

# res.raise_for_status() #문제가 생겼을 경우 프로그램을 바로 종료함.
# print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)