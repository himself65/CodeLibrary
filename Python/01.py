# -*- coding: utf-8 -*-
# 迭代器 yield 装饰器与lambda 以及 上下文管理器

c = iter('abcdefghigklmnopqrstuvwxyz')

# 分别输出a b c
print(next(c))
print(next(c))
print(next(c))
print(next(c))


# 上台阶，每次只能上一个和上两个，层数递增1
def floor():
    a, b = 1, 2
    while True:
        yield b
        a, b = b, a + b


fl = floor()
print(next(fl))
print(next(fl))
print(next(fl))
print(next(fl))


# yield可以用来完成生成有序的ID，或者执行异步
def getID():
    _id = 1
    while True:
        yield _id


# 装饰器，字面意思
@staticmethod
def shit():
    pass


class Shit:
    def __enter__(self):
        print('loadding')

    def __exit__(self, exc_type, exc_value, traceback):
        print('leaving')


with Shit() as s:
    print(s)