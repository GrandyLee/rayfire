#coding=utf-8
# from selenium import webdriver
import os
import time
import tkinter

# def is_odd(n):
#     return n % 3 == 0
#
# #
# def flower_numb(number):  # 水仙花数
#     first = number // 100  # 取百位数
#     second = number // 10 % 10  # 取十位数
#     third = number % 10  # 取个位数
#     if first**3+second**3+third**3 == number:
#         print(number)
#
#


def flower_numb(number):  # 水仙花数
    first = number // 100  # 取百位数
    second = number // 10 % 10  # 取十位数
    third = number % 10  # 取个位数
    return number == first**3+second**3+third**3


list_flower_number = list(filter(flower_numb, list(range(100, 1000))))
print(list_flower_number)
# for i in range(100, 1000):
#     flower_numb(i)

# print(list(range(100, 1000)))
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# list2 = list(filter(is_odd, list1))
# print(list2)
# number = 159

for number in range(100, 999):
    first = number // 100  # 取百位数
    # print(first)
    second = number // 10 % 10  # 取十位数
    # print(second)
    third = number % 10  # 取个位数
    # print(third)
    if first**3+second**3+third**3 == number:
        print(number)

