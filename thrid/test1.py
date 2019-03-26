# coding:utf-8


f = open('G://rayfire/files/record.txt', encoding='utf-8')

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
        file_name_boy = 'boy' + str(count) + '.txt'
        file_name_girl = 'girl' + str(count) + '.txt'

        boy_file = open('G://rayfire/files/' + file_name_boy, 'w')
        girl_file = open('G://rayfire/files/' + file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

file_name_boy = 'boy' + str(count) + '.txt'
file_name_girl = 'girl' + str(count) + '.txt'

boy_file = open('G://rayfire/files/' + file_name_boy, 'w')
girl_file = open('G://rayfire/files/' + file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()

f.close()

