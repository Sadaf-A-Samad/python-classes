class Animals:
    def __init__(self):
        print('I am an Animal..')

    def sound(self):
        print('Animals have some sounds..')

    def eat(self):
        print('Animals Eat...')
# ------------------------------
class Dog(Animals):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
        print(f"I am Dog. and My Kind is {self.breed}")

    def sound(self):
        # super().sound()
        print("My sound is Woof Woof..")
     
    def eat(self):
        # super().eat()
        print('I eats Meat and Bones')

# =========================
d = Dog("Bulldog")
d.eat()
d.sound()

d1 = Dog('Pomerian')
d1.eat()
d1.sound()