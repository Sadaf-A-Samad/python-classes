a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
op = input('Enter OPerator between (+ - * / ): ')
c = 0

if op == "+":
    c = a+b
    print(f"Sum of {a} + {b} = {c}")
elif op == "-":
    c = a-b
    print(f"Sum of {a} - {b} = {c}")
else:
    print("please enter operator b/w (+ - * /)")