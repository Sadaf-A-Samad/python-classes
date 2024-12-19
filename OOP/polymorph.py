class poly:
    def sum(self,a, b):
        c = (a+b)
        return c
    
    def sum(self, a, b, c):
        d = (a+b+c)
        return d
    
p = poly()
# x = p.sum(2,5)
y = p.sum(6,8,9)

# print(f"Sum of a+b = {x}")
print(f"Sum of a+b+c = {y}")