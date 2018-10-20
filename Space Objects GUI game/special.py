# This purple Special object acts as a 'worm-hole' which sucks in and removes every Mobile Simulton in the simulation! 
# If an object is not mobile, it remains unaffected by this special object.

from simulton import Simulton
import model
import math
from mobilesimulton import Mobile_Simulton


class Special(Simulton):
    radius = 15
    
    def __init__(self,x,y,width,height):
        Simulton.__init__(self, x, y, width, height)
        self._width = width
        self._height = height
        self._color = "Purple"
        
    def update(self):
        removedd = set()
        myset = list(model.simultons)
        myset = set(myset)
        for simul in myset:
                if isinstance(simul,Mobile_Simulton):
                    y_diff = -simul._y + self._y
                    x_diff = -simul._x + self._x
                    simul._angle = math.atan2(y_diff,x_diff)
                    if self.contains((simul._x,simul._y)):
                        removedd.add(simul)
        for i in removedd:
            try:
                model.simultons.remove(i)
            except KeyError:
                pass
        
    def display(self,canvas):
        canvas.create_oval(self._x-(Special.radius*2)     , self._y-Special.radius,
                                self._x+(Special.radius*2), self._y+Special.radius,
                                fill=self._color)
    
    def contains(self,xy):
        global radius
        return self.distance(xy) < Special.radius
