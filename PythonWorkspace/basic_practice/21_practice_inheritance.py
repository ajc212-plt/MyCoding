# 1. 상속
# 2. 다중상속

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name #멤버변수 클래스내에서 정의된 변수고, 그 변수를 가지고 초기화를 할수 있고 쓸수 있다.
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
            .format(self.name, location, self.speed))

class AttackUnit(Unit): #() 상속 받을려고 하는 클래스 입력
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) #Unit.__init__() 상속받은 클래스내의 인스턴스 사용
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

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 기능 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): #() 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0
        Flyable.__init__(self, flying_speed)

# #발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name,"3")

# 메소드 오버라이딩
# 자식 클래스에서 정의한 메소드를 쓰고 싶을 때 메소드를 새롭게 정의해서 쓸수 있다.