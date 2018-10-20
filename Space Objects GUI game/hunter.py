# A Hunter is derived from both a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from blackhole import Black_Hole
import math
import model


class Hunter(Pulsator,Mobile_Simulton):
    distancee = 200
    
    def __init__(self,x,y,width,height,angle,speed):
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)
        Pulsator.__init__(self, x, y, width, height)
        self.counter = 0
        

    def update(self):
        temp = set()
        self.move()
        self.wall_bounce()
        x = len(Black_Hole.update(self))
        self.counter +=1
        myset = list(model.simultons)
        myset = set(myset)        
        for simul in myset:
                if isinstance(simul,Prey) and self.distance((simul._x,simul._y))<Hunter.distancee:
                    temp.add(simul)
                    lst = sorted(temp, key = lambda simul: self.distance((simul._x, simul._y)))
                    y_diff = lst[0]._y - self._y
                    x_diff = lst[0]._x - self._x
                    self._angle = math.atan2(y_diff,x_diff)
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
    

        
