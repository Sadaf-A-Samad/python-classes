class TypesOfComputer:
    def types(self, type):
        print(f"Computer has 7 types. I am {type}")

class KindsOfComputer:
    def kind(self, kind):
        print(f'Computers are Digital or Analoge but I am {kind}')

class Computer(TypesOfComputer, KindsOfComputer):
    def comp(self):
        print("Computer is an electronic device")


laptop = Computer()
laptop.comp()
laptop.types("Laptop")
laptop.kind('Hybrid')