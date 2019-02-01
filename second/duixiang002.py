from second.duixiang001 import *


class Frog(Turtle):
    def run(self):
        print("哈哈，我不是跑，我是跳")

    shell = False
    weight = 0.5

    def climb(self):
        print("我的体重是" + str(Frog.weight) + 'kg')


aa = Turtle()
print("888888888888888888888")
bb = Frog()

bb.climb()
