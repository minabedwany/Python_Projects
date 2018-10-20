# A Black_Hole is derived from only a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y,width,height):
        Simulton.__init__(self, x, y, width, height)
        self._width = Black_Hole.radius
        self._height = Black_Hole.radius
        self._color = "Black"
        
    def update(self):
        removed = set()
        myset = list(model.simultons)
        myset = set(myset)
        for simul in myset:
                if isinstance(simul,Prey):
                    if self.contains((simul._x,simul._y)):
                        removed.add(simul)
        for i in removed:
            try:
                model.simultons.remove(i)
            except KeyError:
                pass
        return removed

    
    def display(self,canvas):
        canvas.create_oval(self._x-self._width      , self._y-self._height,
                                self._x+self._width, self._y+self._height,
                                fill=self._color)

    def contains(self,xy):
        global radius
        return self.distance(xy) < Black_Hole.radius


