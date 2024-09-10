

class Area():
    pi = 3.141592653589793

    def area_circle(self, radius):
        return self.pi * radius * radius

    def area_rectangle(self, length, width):
        return length * width

    def area_square(self, side):
        return side * side

    def area_triangle(self, base, height):
        return 0.5 * base * height
