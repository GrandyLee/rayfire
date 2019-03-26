# a = [0, 1, 2, 3, 4, 5, 3, 1]
# print(a)
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


f = open('G://rayfire/files/test001.txt', 'w')

# print(f.read(5))
# print(f.tell())
#
# f.seek(45, 0)
# print(f.tell())
# print(f.readline())
# print(list(f))
f.write('我爱美丽世界')
print(f.read())
f.close()
