"""
十进制转二进制代码
"""


def convert(number):
    if not isinstance(number, int):
        raise ValueError
    while(number):
<<<<<<< HEAD
        print(number & 1, end='')
=======
        t = number & 1
        print(t, end='')
>>>>>>> 436b66374f15ab074b0fe9385a61ff39a6a2e0da
        number = number >> 1
    print('\n')


if __name__:
    num = int(input())
    convert(num)
