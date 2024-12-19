class Animals:
    def __init__(self):
        print('I am an Animal..')

    def features(self, surface):
        print(f'I can live {surface}')
# ------------------------------

class Birds(Animals):
    def __init__(self):
        super().__init__()
        print('I am a Bird.')

    def canFly(self, can):
        print(f'I {can} fly ')
    
# ------------------------------------

class Sparrow(Birds):
    def __init__(self, surface):
        print('my name is Sparrow')
        super().__init__()
        super().features(surface)
        super().canFly('Can')

# ----------------------------
class Chicken(Birds):
    def __init__(self, surface):
        print('My name is Chicken')
        super().__init__()
        super().features(surface)
        super().canFly('Cannot')


# =========================
s = Sparrow('in Air')
c = Chicken('in Coop')