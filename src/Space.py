
class Entity:
    __init__(self, name, location)



class Space:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupant = None

    def __str__(self):
        if self.occupant == None:
            return " ~ "

        
    def display(self):
        if self.occupant == None:
            return " ~ "
        if self.occupant == "enemy":
            return " ! "
        if self.occupant == "asteroid":
            return " * "



spacey = [
    Space(0,0), Space(1,1), Space(3,3)
]

spacey[1].occupant = "enemy"
spacey[2].occupant = "asteroid"

print( spacey[0].display(), spacey[1].display(), spacey[2].display() )

# for s in spacey:
#     print(s.display())