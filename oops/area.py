
from geometry import Area

obj= Area()

circle_area = obj.area_circle(5)
rectangle_area = obj.area_rectangle(4, 6)
square_area = obj.area_square(4)
triangle_area = obj.area_triangle(3, 6)

print(f"Circle Area:{circle_area}")
print(f"Rectangle Area:{rectangle_area}")
print(f"Square area:{square_area}")
print(f"Triangle Area:{triangle_area}")
