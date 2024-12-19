class Person:

    def __init__(self, stName, fName, dob):
        self.stName = stName
        self.fName = fName
        self.__dob = dob
        
    def printInfo(self):
        print(f'Name = {self.stName} - Father Name = {self.fName} - Date of Birth = {self.__dob}')

# ----------------------------------------

class Student(Person):
    def __init__(self, stName, fName, dob, rollno, dept):
        super().__init__(stName, fName, dob)
        self.rollno = rollno
        self.dept = dept
        # super().printInfo()

    def printInfo(self):
        super().printInfo()
        print(f'Rollno = {self.rollno} - Department {self.dept}')


# ----------------------------------------

class Employee(Person):
    def __init__(self, stName, fName, dob, salary, dept):
        super().__init__(stName, fName, dob)
        self.salary = salary
        self.dept = dept

    def printInfo(self):
        super().printInfo()
        print(f'Salary = {self.salary} - department - {self.dept}')

# ---------------------------------------

s1 = Student('Ali', 'Raza', '2-2-2010', '1', 'Engineering')
s1.printInfo()
e1 = Employee('Saad', 'Hassan', '3-5-2000', '30000', 'Admin')
e1.printInfo()
e1._dob = '8-10-2000'
print(e1._dob)
