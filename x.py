class Zach:
    def __init__(self):
        self.x = []

    def add_to_x(self):
        self.x.append(4)


z = Zach()
z.add_to_x()
print(z.x)  # [4]

a = Zach()
print(a.x)  # []
print(z.x)  # [4]
