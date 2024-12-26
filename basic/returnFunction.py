# a^3 + 2a^2b +2ab^2 +b^3
def sqr(a):
    c = a**2
    print(f"the Square of {a} = {c}")
    return c

def multiply(a, b, c):
    e = a*b*c
    print(f"the Product of {a} x {b} x {c} = {e}")
    return e

def sum(a, b, c):
    e = a+b+c
    print(f"the sum of {a} + {b} + {c} = {e}")
    return e



aSqr = sqr(8)
bSqr = sqr(3)
ab2 = multiply(2, 8, 3)
formula = sum(aSqr, ab2, bSqr)






# x = input("hello")

# print(x)