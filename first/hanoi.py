i = 0


def hanoi(n, x, y, z):
    global i
    if n == 1:
        i += 1
        print("移动第", i, "次", x, '-->', z)
    else:
        hanoi(n-1, x, z, y)  # 将前n-1的盘子从x移动到y上3
        hanoi(1, x, '-->', z)   # 将最底下的一个盘子从x移动到z上
        hanoi(n-1, y, x, z)  # 将y上的n-1个盘子移动到z上


n = int(input('请输入汉诺塔的层数：'))
hanoi(n, 'x', 'y', 'z')
print("总共需要移动至少"+str(i)+"次！")