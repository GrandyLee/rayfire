from thrid.area import *


num1 = float(input("请输入三角形的第一边："))
num2 = float(input("请输入三角形的第二边："))
num3 = float(input("请输入三角形的第三边："))

triang = Triangle(num1, num2, num3)
triang.is_triangle()
print("三角形的面积是：" + str('%.2f' % triang.area()))
print("三角形的周长是：" + str(triang.girth()))


a = float(input("请输入长方形的长："))
b = float(input("请输入长方形的宽："))
pic = '正方形'
pic1 = '长方形'
rec = Rectangle(a, b)
if a == b:
    print("这是个" + pic)
    print(pic + "的面积是：" + str(rec.area()))
    print(pic + "的周长是：" + str(rec.girth()))
else:
    print("这是个" + pic1)
    print(pic1 + "的面积是：" + str(rec.area()))
    print(pic1 + "的周长是：" + str(rec.girth()))


r = float(input("请输入圆形的半径："))
cicurlar = Circular(r)
print("圆的面积是：" + str(cicurlar.area()))
print("圆的周长是：" + str(cicurlar.girth()))

