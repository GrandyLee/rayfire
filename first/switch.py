# p = (4, 5)
# x, y = p
# print(x)
# print(y)

# user_name = input('请输入你的姓名：')
# name = user_name
# if name == 'grandy' or name =='Grandy':
#     print('hello,' + name)
# else:
#     print('你不是电脑的主人！！！')

import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


r = random.randint(1, 9)
print(r)
fortune = getAnswer(r)
print(fortune)
