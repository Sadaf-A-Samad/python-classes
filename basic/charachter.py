ch = input("Enter any character: ")

if(ch >= 'a' and ch <= 'z'):
    print(f"{ch} is a Small Alphabet")
elif(ch >= 'A' and ch <= 'Z'):
    print(f"{ch} is a Capital Alphabet")
elif(ch >= '0' and ch <= '9'):
    print(f"{ch} is a Number")
else:
    print(f"{ch} is a Special Charachter")