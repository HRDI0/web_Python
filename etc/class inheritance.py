#클래스 상속 연습
from abc import *           #추상 클래스

class item(metaclass = ABCMeta):
    """
    속성 : name

    메소드
    pick : 아이템 줍기
    drop : 아이템 버리기
    """
    def __init__(self,name):
        self.name = name

    def pick(self):
        print(f"Pick the [{self.name}]")

    def drop(self):
        print(f"Drop the [{self.name}]")

    @abstractmethod         #추상 메소드
    def use(self):          #상속받는 메소드에서 강제적으로 작성해야함
        pass

class wepon(item):
    """
    속성 : 공격력

    메소드
    attack : 무기 사용 공격
    """

    def __init__(self,name,damage):
        super().__init__(name)
        self.__damage = damage

    def use(self):
        print(f"Using {self.name}, Attack {self.__damage} damage")

class healing_item(item):
    """
    속성 : 회복량

    메소드
    healing : 회복 아이템 사용 체력 회복
    """

    def __init__(self,name, heal):
        super().__init__(name)
        self.__heal = heal

    def use(self):
        print(f"Using {self.name}, Healing {self.__heal} HP")


k2 = wepon('k2',100)
k1 = wepon('k1',100)
healPack = healing_item('healPack',80)
bandage = healing_item('bandage',50)

k2.pick()
k2.use()
k2.drop()

k1.pick()

healPack.pick()
bandage.pick()
bandage.use()
bandage.drop()

k1.use()
healPack.use()
healPack.drop()
