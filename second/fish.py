import random as r


class Fish:
    def __init__(self, name):
        self.name = name
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("%s 的位置是：" % self.name, self.x, self.y)


class GoldFish(Fish):
    pass


class Carp(Fish):
    pass


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self, name):
        super().__init__(name)
        # Fish.__init__(self, name)
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想是天天有吃的^_^")
            self.hungry = False
        else:
            print("太撑了，吃不下！")


fish = GoldFish("金鱼")
shark = Shark("鲨鱼")
for i in range(0, 6):
    fish.move()
    shark.eat()
    shark.move()
