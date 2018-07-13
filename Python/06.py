p = 19260817
a = int(input()) % p
b = int(input()) % p
if b == 0:
    print('Angry!')
else:
    print(a * pow(b, p - 2, p) % p)
