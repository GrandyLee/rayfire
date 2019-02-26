import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置是:", self.x, self.y)


class GoldFish(Fish):
    pass


goldfish = GoldFish()

for i in range(10):
    goldfish.move()


