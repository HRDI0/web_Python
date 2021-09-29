import random
class monster:                  #monster 객체

    version = 1.0               #모든 객체들이 공유하는 속성
    def __init__ (self, health, attack, speed):     #생성자. 객체가 생성되면 자동으로 실행되는 함수
        self.health = health
        self.attack = attack
        self.speed = speed
    def __str__(self):                              #객체를 print에 넣으면 실행됨.
       return f'hp : {self.get_hp()}, attack : {self.get_attack()}, speed : {self.get_speed()}'

    #instancemethod 인스턴스 속성에 접근할수 있는 메소드
    def decrease_hp(self,num):
        self.health -= num
    def get_hp(self):
        return self.health
    def get_attack(self):
        return self.attack
    def get_speed(self):
        return self.speed


    @classmethod        #데코레이티드
    def _v(cls):        #클래스를 뜻하는 cls 변수
        print('version : ' + str(cls.version))  #클래스 변수인 version 출력


class ground(monster):          #monster 객체를 상속.
    def digg(self):
        self.health += 50
class water(monster):
    def swim(self):
        self.attack += 50
class air(monster):
    def fly(self):
        self.speed +=50

class Dragon(air):
    def __init__ (self, health, attack, speed):
        super().__init__(health, attack, speed)
        self.__skill = ('drago_breath','fly_high','iron_tail')
    def using_skill1(self):
        print(f'Dragon의 {self.__skill[random.randint(0,2)]}')

class roll:
    @staticmethod
    def dice():
        return random.randint(0,6)


monster._v()

print(roll.dice())
ork = ground(800,100,40)
print(ork)
ork.decrease_hp(80)
print('You attack ork')
print(ork.get_hp())
ork.digg()
print('ork dig under ground')
print(ork.get_hp())
print('ork run')
print()

print(roll.dice())
print('You find Dragon')
dragon = Dragon(2500,320,250)
print(dragon)
print('Dragon attack You')
dragon.using_skill1()
print('Drangon fly')
dragon.fly()
print(f'Drangon now speed {dragon.get_speed()}')

