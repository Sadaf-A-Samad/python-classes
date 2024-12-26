# -------------Simple Function
def func_1():
    a = 5
    b = 2
    c = a+b
    print(f"the sum of {a} + {b} = {c}")
    print('THis is my Function')    


# -----------Argument Type
def sum(a, b):
    c = a+b
    print(f"the sum of {a} + {b} = {c}")
    return c

def sqr(a):
    c = a**2
    print(f"the Square of {a} = {c}")

# x = sum(5,2)
# sqr(x)

# a2 + 2*a*b +b2


# -----------Argument Type
# def sum(*a):
#     print(a[2])


# for value in list:
    
# ----------- variable Argument Type
def sum(*a):
    print(a)
    c = 0
    for val in a:
        print(f'{c} + {val} ')
        c = c + int(val)
    print(f"sum = {c}")

# sum1(9,7, 5)
# sum(9,17)
# sum(19,7)


