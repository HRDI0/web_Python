#rpg게임 구동 패키지
version = 1.0

import random
class player:       

    def __init__(self,name,job):
        self.name = name
        self.job = job

        if self.job == '1':
            self.hp = 1000
            self.mp = 500
            self.atk = 120
            self.dex = 50
            self.int = 50
            self.skill = ['Power sword', 'Shield up', 'Sword sting']
        elif self.job == '2':
            self.hp = 800
            self.mp = 700
            self.atk = 50
            self.dex = 100
            self.int = 50
            self.skill = ['Triple shot', 'dodge shot', 'Head shot']
        elif self.job == '3':
            self.hp = 500
            self.mp = 1000
            self.atk = 50
            self.dex = 50
            self.int = 100
            self.skill = ['Fire ball', 'Frozen', 'Wind Cutter']

    def using_skill(self):
        print(f"{self.name}'s {self.skill[random.randint(0,2)]}")

    def get_status(self):
        print (f'hp {self.hp}\nmp {self.mp}\natk {self.atk}\ndex {self.dex}\nint {self.int}')