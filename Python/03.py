"""
十进制转二进制代码
"""


def convert(number):
    if not isinstance(number, int):
        raise ValueError
    while(number):
        t = number & 1
        print(t, end='')
        number = number >> 1
    print('\n')


if __name__:
    num = int(input())
    convert(num)
