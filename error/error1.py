try:
    f = open('haha.txt', 'w')
    print(f.write('我存在sdfs了'))
    sum = 1 + 4
# except OSError as reason:
#     print('文件出错了T_T' + str(reason))
except TypeError as reason:
    print('类型出错了\n错误原因是：' + str(reason))
finally:
    f.close()

# except(OSError,TypeError):
#     print('出错了！')
