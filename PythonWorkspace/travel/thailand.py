class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__": #해당 py 안에서 직접 불러올 때 if 문 아래 코드가 실행
    print("Thailand 모듈을 직접 실행")
    print("이 문장을 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else: #다른 py에서 해당 py를 임포트해서 불러오면 else 문 아래 코드가 실행
    print("Thailand 외부에서 모듈 호출")