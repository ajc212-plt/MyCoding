class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): #두개 이상의 부모 클래스를 다중 상속을 받을때는 맨 처음 받는 클래스만
                                  #상속이 된다.
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

#드랍쉽
dropship = FlyableUnit()