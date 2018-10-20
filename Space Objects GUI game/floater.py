# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import uniform


class Floater(Prey):
    
    def __init__(self,x,y,width,height,angle,speed):
        Prey.__init__(self, x, y, width, height, angle, speed)
        self._image = PhotoImage(file='ufo.gif')
        
    def update(self):
        self._angle += uniform(-0.5, 0.5)
        if self._speed>3 and self._speed <7:
            self._speed += uniform(-0.5, 0.5)
        elif self._speed == 7:
            self._speed += uniform(-0.5, 0)
        elif self._speed == 3:
            self._speed += uniform(0, 0.5)
        self.move()
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_image(*self.get_location(),image=self._image)
        