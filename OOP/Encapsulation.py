class class1:
    __a = 7
    def __show(self):
        print(f'value of a is {self.__a}')

class class2(class1):

    def __init__(self):
        super().__show()
        # print(super().__a)


c = class2()
# c.show()
# print(c.__a)
