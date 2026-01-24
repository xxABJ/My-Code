
class ShapeName:
    def __init__(self):
        self.name = None
    
    def pyy(self):
        print(self.name)


class ShapeType:
    def __init__(self):
        self.type = None
        self.new_type = None
    
    def po(self):
        print(self.type)


class ShapeSize:
    def __init__(self):
        self.size = None
    
    def pl(self):
        print(self.size)


class ShapeColour:
    def __init__(self):
        self.colour = None

    def pg(self):
        print(self.colour)


class FinalShape(ShapeName, ShapeType, ShapeSize, ShapeColour):
    def __init__(self, name, type, size, colour):
        ShapeName.__init__(self)
        ShapeType.__init__(self)
        ShapeSize.__init__(self)
        ShapeColour.__init__(self)
        self.name = name
        self.type = type
        self.size = size
        self.colour = colour

    def pp(self):
        pass
    

s = FinalShape("abj", "circle", 20, "blue")
g = FinalShape("aj", "square", 23, "red")

print(FinalShape.__dict__)
