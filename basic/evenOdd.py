no = int(input("Enter any Year: "))

c = no%4
print(c)

if(c == 0):
    print("Leap Year")
else:
    print("Not a Leap year")