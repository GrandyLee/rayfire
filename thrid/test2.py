# coding:utf-8
def save_file(boy, girl, count):
    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open('G://rayfire/files/' + file_name_boy, 'w')
    girl_file = open('G://rayfire/files/' + file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    f = open(file_name, encoding='utf-8')
    boy = []
    girl = []
    count = 1
    for each in f:
        if each[:5] != '=====':
            (role, line_spoken) = each.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            else:
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1

    save_file(boy, girl, count)

    f.close()


split_file('G://rayfire/files/record.txt')
