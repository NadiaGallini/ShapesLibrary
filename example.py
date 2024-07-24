from shapes import Circle, Triangle, Square, calculate_area

circle = Circle(5)
triangle = Triangle(3, 4, 5)
square = Square(4)

print(f"Circle area: {circle.area()}")
print(f"Triangle area: {triangle.area()}")
print(f"Square area: {square.area()}")

print(f"Area using calculate_area (Circle): {calculate_area(circle)}")
print(f"Area using calculate_area (Triangle): {calculate_area(triangle)}")
print(f"Area using calculate_area (Square): {calculate_area(square)}")
