# From Comp 2150, original question converted from .PY to .RB

# (1)Ex4 – With single parent, using super( ) in the child class to initialize the attribute(s):
# Create two classes based on the following UML diagram:
# In the Rectangle class (base):
# -	Define the area(self) = length * width
# -	Define the Perimeter(self) = 2 * (length + width)
# In the Square Class (child)
# Use super().__init__(length, length) to initialize the lengh
# -	Create rectangle object with (4, 5)
# -	Create a square object with (6)
# -	Display the areas of rec and square.

class Rectangle
    def initialize(length, width)
      @length = length
      @width = width
    end
  
    def area
      @length * @width
    end
  
    def perimeter
      2 * (@length + @width)
    end
end
  
class Square < Rectangle
    def initialize(length)
      super(length, length)
    end
end
  
class Cube < Rectangle
    def initialize(length)
      super(length, length)
      @height = length
    end
  
    def surface_area
      6 * @length**2
    end
  
    def volume
      @length**3
    end
end
  
  
  