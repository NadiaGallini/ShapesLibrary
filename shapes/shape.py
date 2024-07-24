class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses")

def calculate_area(shape):
    if isinstance(shape, Shape):
        return shape.area()
    else:
        raise TypeError("The object is not an instance of Shape")
