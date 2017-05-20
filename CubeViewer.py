from Cube import *
from tkinter import *
from os import system
from platform import system as platform

class RubiksShell(Frame):
    """This is a class meant to display a GUI for the Rubiks class"""

    ANIMATION_DELAY = 200

    def __init__(self, parent, cube=Cube()):
        Frame.__init__(self, parent)
        # Create Canvas, store canvas items
        self.canvas = Canvas(parent, width=800, height=650)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas_items = [[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],
                             [3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5]]

        # Draw the cube
        self.draw_cube(400, 75, 60, 8)
        # references the cube we will be displaying
        self.cube = cube
        # correctly colors the faces on the drawn cube according to cube data
        self.recolor_faces(cube.moveStack[0])
        # handles key presses for manual button input
        parent.bind('<KeyPress>', self.onKeyPress)

    def draw_cube(self, x_origin, y_origin, side_width, space_width):
        """Draws a visual representation of a rubik's cube. Currently only the top face is calibrated to make the entire face from variables"""
        # Top Face
        self.draw_top_square(x_origin, y_origin, side_width, 0, 0)
        self.draw_top_square(x_origin, y_origin+space_width+side_width, side_width, 0, 4)
        self.draw_top_square(x_origin, y_origin+space_width*2+side_width*2, side_width, 0, 8)
        self.draw_top_square(x_origin+1.73*side_width+space_width, y_origin+space_width+side_width, side_width, 0, 2)
        self.draw_top_square(x_origin-1.73*side_width-space_width, y_origin+space_width+side_width, side_width, 0, 6)
        self.draw_top_square(x_origin+(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)/2, side_width, 0, 1)
        self.draw_top_square(x_origin-(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)/2, side_width, 0, 3)
        self.draw_top_square(x_origin+(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)*3/2, side_width, 0, 5)
        self.draw_top_square(x_origin-(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)*3/2, side_width, 0, 7)
        y_origin = y_origin+space_width*2+side_width*2
        # Right Face
        self.draw_side_square(x_origin+0.5*side_width, y_origin+side_width-space_width, side_width, 1, 2, 0)
        self.draw_side_square(x_origin+0.5*side_width, y_origin+2*side_width, side_width, 1, 2, 3)
        self.draw_side_square(x_origin+0.5*side_width, y_origin+3*side_width+space_width, side_width, 1, 2, 6)
        self.draw_side_square(x_origin+0.5*side_width+side_width, y_origin+0.5*side_width-1.5*space_width, side_width, 1, 2, 1)
        self.draw_side_square(x_origin+0.5*side_width+side_width, y_origin+1.5*side_width-0.5*space_width, side_width, 1, 2, 4)
        self.draw_side_square(x_origin+0.5*side_width+side_width, y_origin+2.5*side_width+0.5*space_width, side_width, 1, 2, 7)
        self.draw_side_square(x_origin+0.5*side_width+2*side_width, y_origin-2*space_width, side_width, 1, 2, 2)
        self.draw_side_square(x_origin+0.5*side_width+2*side_width, y_origin+side_width-space_width, side_width, 1, 2, 5)
        self.draw_side_square(x_origin+0.5*side_width+2*side_width, y_origin+2*side_width, side_width, 1, 2, 8)
        # Front Face
        self.draw_side_square(x_origin-0.5*side_width, y_origin+side_width-space_width, side_width, -1, 1, 2)
        self.draw_side_square(x_origin-0.5*side_width, y_origin+2*side_width, side_width, -1, 1, 5)
        self.draw_side_square(x_origin-0.5*side_width, y_origin+3*side_width+space_width, side_width, -1, 1, 8)
        self.draw_side_square(x_origin-0.5*side_width-side_width, y_origin+0.5*side_width-1.5*space_width, side_width, -1, 1, 1)
        self.draw_side_square(x_origin-0.5*side_width-side_width, y_origin+1.5*side_width-0.5*space_width, side_width, -1, 1, 4)
        self.draw_side_square(x_origin-0.5*side_width-side_width, y_origin+2.5*side_width+0.5*space_width, side_width, -1, 1, 7)
        self.draw_side_square(x_origin-0.5*side_width-2*side_width, y_origin-2*space_width, side_width, -1, 1, 0)
        self.draw_side_square(x_origin-0.5*side_width-2*side_width, y_origin+side_width-space_width, side_width, -1, 1, 3)
        self.draw_side_square(x_origin-0.5*side_width-2*side_width, y_origin+2*side_width, side_width, -1, 1, 6)
        # Back Face
        y_origin = y_origin-space_width*2-side_width*2
        side_width = 0.75*side_width
        space_width = 0.75*space_width
        self.draw_side_square(x_origin+5*side_width, y_origin-0.5*side_width, side_width, -1, 4, 2)
        self.draw_side_square(x_origin+5*side_width, y_origin+0.5*side_width+space_width, side_width, -1, 4, 5)
        self.draw_side_square(x_origin+5*side_width, y_origin+1.5*side_width+2*space_width, side_width, -1, 4, 8)
        self.draw_side_square(x_origin+6*side_width, y_origin+0.5*space_width, side_width, -1, 4, 1)
        self.draw_side_square(x_origin+6*side_width, y_origin+side_width+1.5*space_width, side_width, -1, 4, 4)
        self.draw_side_square(x_origin+6*side_width, y_origin+2*side_width+2.5*space_width, side_width, -1, 4, 7)
        self.draw_side_square(x_origin+7*side_width, y_origin+1.0*side_width-2.5*space_width, side_width, -1, 4, 0)
        self.draw_side_square(x_origin+7*side_width, y_origin+2.0*side_width-1.5*space_width, side_width, -1, 4, 3)
        self.draw_side_square(x_origin+7*side_width, y_origin+3.0*side_width-0.5*space_width, side_width, -1, 4, 6)
        # Left face
        self.draw_side_square(x_origin-5*side_width, y_origin-0.5*side_width, side_width, 1, 3, 0)
        self.draw_side_square(x_origin-5*side_width, y_origin+0.5*side_width+space_width, side_width, 1, 3, 3)
        self.draw_side_square(x_origin-5*side_width, y_origin+1.5*side_width+2*space_width, side_width, 1, 3, 6)
        self.draw_side_square(x_origin-6*side_width, y_origin+0.5*space_width, side_width, 1, 3, 1)
        self.draw_side_square(x_origin-6*side_width, y_origin+side_width+1.5*space_width, side_width, 1, 3, 4)
        self.draw_side_square(x_origin-6*side_width, y_origin+2*side_width+2.5*space_width, side_width, 1, 3, 7)
        self.draw_side_square(x_origin-7*side_width, y_origin+1.0*side_width-2.5*space_width, side_width, 1, 3, 2)
        self.draw_side_square(x_origin-7*side_width, y_origin+2.0*side_width-1.5*space_width, side_width, 1, 3, 5)
        self.draw_side_square(x_origin-7*side_width, y_origin+3.0*side_width-0.5*space_width, side_width, 1, 3, 8)
        # Bottom face
        space_width = 4/3*space_width
        y_origin = y_origin+9*side_width
        self.draw_top_square(x_origin, y_origin, side_width, 5, 6)
        self.draw_top_square(x_origin, y_origin+space_width+side_width, side_width, 5, 4)
        self.draw_top_square(x_origin, y_origin+space_width*2+side_width*2, side_width, 5, 2)
        self.draw_top_square(x_origin+1.73*side_width+space_width, y_origin+space_width+side_width, side_width, 5, 8)
        self.draw_top_square(x_origin-1.73*side_width-space_width, y_origin+space_width+side_width, side_width, 5, 0)
        self.draw_top_square(x_origin+(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)/2, side_width, 5,7)
        self.draw_top_square(x_origin-(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)/2, side_width, 5, 3)
        self.draw_top_square(x_origin+(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)*3/2, side_width, 5, 5)
        self.draw_top_square(x_origin-(side_width*1.73+space_width)/2, y_origin+(space_width+side_width)*3/2, side_width, 5, 1)

    def draw_top_square(self, x_origin, y_origin, side_length, face, slot, outline='black', fill='white', width=1):
        """Draws the squares of the top face on canvas"""
        points = []
        points.append((x_origin + 1.73/2*side_length, y_origin))
        points.append((x_origin, y_origin + 0.5*side_length))
        points.append((x_origin - 1.73/2*side_length, y_origin))
        points.append((x_origin, y_origin - 0.5*side_length))
        self.canvas_items[face][slot] = self.canvas.create_polygon(points, outline=outline, fill=fill, width=width)

    def draw_side_square(self, x_origin, y_origin, side_length, orientation, face=0, slot=0, outline='black', fill='white', width=1):
        """Draws the squares of the side faces on canvas"""
        points = []
        # Orientation 1 for right, -1 for front
        points.append((x_origin+1.73/4*side_length, y_origin-orientation*0.75*side_length))
        points.append((x_origin+1.73/4*side_length, y_origin+orientation*0.25*side_length))
        points.append((x_origin-1.73/4*side_length, y_origin+orientation*0.75*side_length))
        points.append((x_origin-1.73/4*side_length, y_origin-orientation*0.25*side_length))
        self.canvas_items[face][slot] = self.canvas.create_polygon(points, outline=outline, fill=fill, width=width)

    def draw_side(self, x_origin, y_origin, side_length, width, shape_type, slot):
        """Draws the miscellaneous objects, which help make visualization easier."""

    def animate_movestack(self):
        if not self.cube.moveStack:
            return
        self.recolor_faces(self.cube.moveStack[0])
        self.cube.moveStack = self.cube.moveStack[1:]

        self.master.after(RubiksShell.ANIMATION_DELAY, self.animate_movestack)

    def recolor_faces(self, faces):
        """Recolor the faces of the rubik's cube. Color the visual representation"""
        for face in range(6):
            for slot in range(9):
                color = 'green'
                if faces[face][slot] == 'b':
                    color = 'blue'
                elif faces[face][slot] == 'w':
                    color = 'white'
                elif faces[face][slot] == 'r':
                    color = 'red'
                elif faces[face][slot] == 'o':
                    color = 'orange'
                elif faces[face][slot] == 'y':
                    color = 'yellow'
                self.canvas.itemconfig(self.canvas_items[face][slot], fill=color)

    def onKeyPress(self, event):
        pass
        if event.char == 't':
            self.cube.execute_algorithm("R U R' U' R' F R2 U' R' U' R U R' F'")
            self.animate_movestack()


if __name__ == '__main__':
    window = Tk()
    shell = RubiksShell(window, Cube())

    # Bring app into focus (on osx)
    if platform() == 'Darwin':  # How Mac OS X is identified by Python
        system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    window.mainloop()
