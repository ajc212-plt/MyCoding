#일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name #멤버변수 클래스내에서 정의된 변수고, 그 변수를 가지고 초기화를 할수 있고 쓸수 있다.
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name #멤버변수 클래스내에서 정의된 변수고, 그 변수를 가지고 초기화를 할수 있고 쓸수 있다.
        self.hp = hp
        self.damage = damage

    def attack(self, location): #Class 내에서 Method 앞에서는 항상 self를 써줌
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
            #self. 은 클래스 내에서 전달받은 값을 쓰고
            #non self는 외부에서 전달받은 값을 씀
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병

# 파이어뱃 : 공격 유닛, 화염방사기 .
firebat1 = AttackUnit("파이어뱃",50, 16)
firebat1.attack("5")

#공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
