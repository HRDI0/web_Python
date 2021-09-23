import random
class monster:
    def __init__ (self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def get_status(self):
        print(f'hp : {self.get_hp()}, attack : {self.get_attack()}, speed : {self.get_speed()}')

    def decrease_hp(self,num):
        self.health -= num
    def get_hp(self):
        return self.health
    def get_attack(self):
        return self.attack
    def get_speed(self):
        return self.speed


class ground(monster):
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
        self.skill = ('drago_breath','fly_high','iron_tail')
    def using_skill1(self):
        print(f'Dragon의 {self.skill[random.randint(0,2)]}')


ork = ground(800,100,40)
ork.decrease_hp(80)
print('You attack ork')
print(ork.get_hp())
ork.digg()
print('ork dig under ground')
print(ork.get_hp())
print('ork run')
print()

print('You find Dragon')
dragon = Dragon(2500,320,250)
dragon.get_status()
print('Dragon attack You')
dragon.using_skill1()
print('Drangon fly')
dragon.fly()
print(f'Drangon now speed {dragon.get_speed()}')

