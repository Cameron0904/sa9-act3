'''
(1)Ex4 – With single parent, using super( ) in the child class to initialize the attribute(s):
	Create two classes based on the following UML diagram:
	In the Rectangle class (base):
-	Define the area(self) = length * width
-	Define the Perimeter(self) = 2 * (length + width)
In the Square Class (child)
	Use super().__init__(length, length) to initialize the lengh
-	Create rectangle object with (4, 5)
-	Create a square object with (6)
-	Display the areas of rec and square.
(2)
Results:
The cube results: length is 3, surface_area is 54, volume = 27
The square results:length: 3, area: 9, perimeter: 12


(3) Author(s): Cameron Cox
(4) Date: 4-27-23
(5) filename: Ex.4.1(Area Inheritance).py
(6) course/section: Comp 2150-002
'''
# Creating the parent class Rectangle in order to determine the area and perimeter of a shape.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    # Computing area of a rectangle
    def area(self):
        return self.length * self.width
    # Computing the perimeter of a rectangle, since perimeter is l+w+l+w, we can say 2 * l+w
    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating a child class to determine the area and perimeter of a square(due to inheritance)
class Square(Rectangle):
    # We use super() to call the parent class in order to access all the methods within Rectangle
    def __init__(self, length):
        # Since squares have perfect symmetry, we can say length,length instead of length,width
        super().__init__(length, length)

# Creating a second child class to deal with a Cube
class Cube(Rectangle):
    # We can use the same logic as before for a square, since cubes are symmetric.
    def __init__(self, length):
        super().__init__(length, length)
        # Since a cube is 6 squares, all the side lengths are identical, including the height
        self.height = length

    # Since a cube is 6 sided, we compute the surface area by multiplying one sides area times six
    def surface_area(self):
        return 6 * super().area()
    # Since the volume of a cube is L*W*H, we obtain the area and multiply it by the height of the cube.
    def volume(self):
        return super().area() * self.height


# Test Cases
sqr = Square(6)
print(f"Square results: length: {sqr.length}, area: {sqr.area()}, perimeter: {sqr.perimeter()}")

rec = Rectangle(4, 5)
print(f"Rectangle results: length: {rec.length}, width: {rec.width}, area: {rec.area()}, perimeter: {rec.perimeter()}")

cub1 = Cube(3)
print(f"Cube results: length is {cub1.length}, surface_area is {cub1.surface_area()}, volume = {cub1.volume()}")

'''
Results:
Square results: length: 6, area: 36, perimeter: 24
Rectangle results: length: 4, width: 5, area: 20, perimeter: 18
Cube results: length is 3, surface_area is 54, volume = 27

'''
