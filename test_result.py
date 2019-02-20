#!/usr/bin/env python
import os

pwd = os.getcwd()
print(pwd)

f = open("放管服.postman_test_run20190220.json", 'r')
test_json = f.read(-1)
print(test_json)
