# 使用了迭代器的斐波那契数列的例子
# for 循环的对象并不是个内容，而是生成内容的方法，这样做可以节省资源
class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a

            self.a, self.b = self.b, self.a+self.b
            self.current_num += 1

            return ret
        else:
            raise StopIteration


fibo = Fibonacci(10)

for num in fibo:
    print(num)