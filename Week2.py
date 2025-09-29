class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rec= rectangle (10, 15)

print("area: ", rec.area())
print("perimeter: ", rec.perimeter())


