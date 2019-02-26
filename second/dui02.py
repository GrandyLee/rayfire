class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池中总共有乌龟 %d只，小鱼 %d 条" % (self.turtle.num, self.fish.num))
        print("水池中总共有乌龟"+str(self.turtle.num)+"只，小鱼"+str(self.fish.num) + "条")


pool = Pool(2, 5)
pool.print_num()
