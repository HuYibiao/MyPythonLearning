
#python learning
#编写python函数解决汉诺塔问题

#这一类问题可以分为三步来理解：
#1.将x上的前n-1个盘子移动到y上
#2.将x上的最后一个盘子移动到z上
#3.将y上的前n-1个盘子移动到z上
#再通过迭代函数很轻松解决


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    elif n > 1:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, a, b, c)

#expecting output:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C