# import random
#
# a = 'eqwsdqweqwaqaq'
# b = ''
# x = len(a)
# print(x)
#
# for i in range(x-1):
#     if a[i] == 'w' or a[i] == 'q':
#         pass
#     else:
#         b = b+a[i]
# print(a)
# print(b)


#!/usr/bin/env python


f = open('放管服.postman_test_run20190220.json', 'rb')
test_json = f.read(-1)
print(test_json)
