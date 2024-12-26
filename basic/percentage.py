eng = int(input("Enter marks for English: "))
urdu = int(input("Enter marks for Urdu: "))
maths = int(input("Enter marks for Maths: "))

obtainMarks = eng+urdu+maths
print(f"Your obtain Marks are {obtainMarks}")
percent = (obtainMarks/300)*100
print(f"Your percentage is {percent}")

if percent <=100 and percent>80:
    print("Your are Pass: Your Grade is A1")
elif percent <80 and percent>=70:
    print("Your are Pass: Your Grade is A")
elif percent >70 and percent<=60:
    print("Your are Pass: Your grade is B")
elif percent <60 and percent>=50:
    print("Your are Pass: Your Grade is C")
elif percent >=40 and percent<50:
    print("Your are Pass: Your grade is D")
else:   
    print("You are Fail") 