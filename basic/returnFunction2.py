# a^3 + 3a^2b +3ab^2 +b^3
def pow(a, p):
    c = a**p
    print(f"{a} power {p} = {c}")
    return c

def multiply(a, b, c):
    e = a*b*c
    print(f"the Product of {a} x {b} x {c} = {e}")
    return e

def sum1(*a):
    c = 0
    for val in a:
        c = c + int(val)
    print(f"sum = {c}")
    return c

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))

aCube = pow(a, 3)
bCube = pow(b, 3)

aSqr = pow(a, 2)
bSqr = pow(b, 2)

ab1 = multiply(3, aSqr, b)
ab2 = multiply(3, a, bSqr)

formula = sum1(aCube, ab1, ab2, bCube)
