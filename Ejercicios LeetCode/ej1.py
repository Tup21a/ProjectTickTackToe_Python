def inv(num):
    n = num
    rev = 0
    while n>0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    return num == rev

n = 121
n = - 121
print(inv(n))

