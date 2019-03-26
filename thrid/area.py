#!/usr/bin/env python
# encoding: utf-8
# Author: GrandyLee <45406700@qq.com>
# Create Date: 2019-03-26 14:03:57
# Last Modified: 2019-03-26 16:11:13
# Description:
"""
1、长方形的面积=长×宽 ，正方形的面积=边长×边长
2、三角形的面积=海伦公式
3、圆的面积=圆周率×半径×半径
"""
# from math import pi
class Rectangle:
    def __init__(self, length, width):  # 初始化长方形
        self.length = length
        self.width = width

    def area(self):  # 计算面积
        return self.length * self.width

    def girth(self): # 计算周长
        return (self.length + self.width) * 2


class Triangle:
    def __init__(self, x, y, z):  # 初始化三角形
        self.x = x
        self.y = y
        self.z = z

    def is_pythagoras(self):  # 判断是否为直角三角形
        if self.x ** 2 + self.y ** 2 == self.z ** 2 or self.x ** 2 + self.z ** 2 == self.y ** 2 or self.y ** 2 + self.z ** 2 == self.x ** 2:
            return True
        else:
            return False

    def is_triangle(self):
        if (self.x + self.y) > self.z and (self.x + self.z) > self.y and (self.y + self.z) > self.x:  # 判断是否能构成三角形
            if self.x == self.y == self.z:  # 判断是否能构成等边三角形
                print("这是个等边三角形")
            elif self.x == self.y or self.x == self.z or self.z == self.y:  # 判断是是否能构成等腰直角三角形
                if Triangle.is_pythagoras(self):  # 调用直角三角形判断
                    print("这是个等腰直角三角形")
                else:
                    print("这是个等腰三角形")
            elif Triangle.is_pythagoras(self):  # 调用直角三角形判断
                print("这是个普通直角三角形")
            else:
                print("这是个普通三角形")
        else:
            print("不能构成三角形")

    def area(self):  # 计算面积
        p = (self.x + self.y + self.z)*0.5
        return (p * (p-self.x) * (p-self.y) * (p-self.z))**0.5

    def girth(self):  # 计算周长
        return self.x + self.y + self.z


class Circular:  # 计算圆的面积和周长
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def girth(self):
        return self.radius * 2 * 3.14


if __name__ == "__main__":
    pass
