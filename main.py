from CubeViewer import *
import threading, queue, time
from os import system
from platform import system as platform

cube = Cube()
view = CubeViewer(cube=cube)


class InputListener(threading.Thread):
    def run(self):
        while True:
            alg = str(input("> "))
            if alg == "reset":
                cube.reset()
            else:
                cube.execute_algorithm(alg)
            view.animate_movestack()

listener = InputListener()
listener.daemon = True
listener.start()

# Bring app into focus (on osx)
if platform() == 'Darwin':  # How Mac OS X is identified by Python
    system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

view.mainloop()
