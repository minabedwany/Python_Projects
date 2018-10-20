import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special
from prey      import Prey
import random,math
# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
simultons       = set()
clicked = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simultons
    running     = False
    cycle_count = 0
    simultons       = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global running, cycle_count
    if running:
        cycle_count+=1
        running = False
    if running == False:
        cycle_count+=1
        running = True
        for b in simultons:
            try:
                b.move()
            except:
                pass  
        running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global clicked
    clicked = str(kind)


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global clicked
    
    if clicked == None:
        pass
    if clicked == "Remove":
            myset = list(simultons)
            myset = set(myset)
            for b in myset:
                if not isinstance(b, Black_Hole):
                        if b.contains([x,y]):
                            remove(b)
                if isinstance(b,Black_Hole):
                    if b.contains([x,y]):
                        remove(b)


    if clicked == "Ball" or clicked == "Floater" or clicked == "Hunter":
        string = clicked
        string += "(x,y,5,5,random.random()*math.pi*2,5)"
        s = string
        add(eval(s))

    if clicked == "Black_Hole" or clicked == "Special" or clicked == "Pulsator":
        string = clicked
        string += "(x,y,5,5)"
        s = string
        add(eval(s))


#add simulton s to the simulation
def add(s):
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    sett = set()
    for simul in simultons:
        if isinstance(simul, Prey) and p(simul.get_location()):
            sett.add(simul)
    return sett
            


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        try:
            for b in simultons:
                b.update()
        except RuntimeError:
            pass


#delete from the canvas each simulton in the simulation; then call display for each
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in simultons:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" updates/"+str(cycle_count)+" cycles")
