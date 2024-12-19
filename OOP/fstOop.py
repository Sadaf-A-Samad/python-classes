class Student:
    rollno = 0
    stName = ''
    dob = ''

    def __init__(self, rollno, stName, dob):
        self.rollno = rollno
        self.stName = stName
        self.dob = dob

        
    def printInfo(self):
        print("this is my class function")
        print(f'Rollno = {self.rollno} - Student Name = {self.stName} - Date of Birth = {self.dob}')


obj = Student(1, 'Ali', '10-10-2014')   #Constructor or init - intialization function

# obj1 = Student()

# obj.stName = 'Fahad'
# print(f"Variable from class {obj.stName}")
obj.printInfo()

