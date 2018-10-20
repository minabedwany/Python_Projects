# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
import model


class Pulsator(Black_Hole):
    constant = 30
    
    def __init__(self,x,y,width,height):
        Black_Hole.__init__(self, x, y, width, height)
        self.counter = 0
        
    def update(self):
        x = len(Black_Hole.update(self))
        self.counter +=1
        if x>=1:
            self.counter = 0
            self._width +=1
            self._height +=1
        if self.counter == Pulsator.constant:
            self.counter = 0
            self._width -=1
            self._height -=1
            if self._width == 0 or self._height == 0:
                model.remove(self)


            