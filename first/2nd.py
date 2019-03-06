def spam(divibeBy):
    try:
        return 42/divibeBy
    except ZeroDivisionError:
        print('Error:Invalid argument')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(6))
print(spam(9))


def strtest(num):
    str = 'first'
    for i in range(num):
        str += 'X'
    return str


print(strtest(5))
