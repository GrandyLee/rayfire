class Potato:
    def __init__(self, name):
        self.name = name

    def kick(self):
        print("我叫%s,噢，~ 谁踢我？！" % self.name)


p = Potato("土豆")
p.kick()
