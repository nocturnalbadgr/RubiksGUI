from Cube import *
from tkinter import *

class RubiksShell(Frame):
    """This is a class meant to display a GUI for the Rubiks class"""

    animationDelay = 200

    def __init__(self, parent):
        Frame.__init__(self, parent)
        # Create Canvas, store canvas items
        self.canvas = Canvas(parent, width=800, height=650)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas_items = [[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],
                             [3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5]]

        #first row of buttons: U F R L B D
        row_one = Frame()
        top_face = Button(row_one, text='U ', command = self.top_turn)
        top_face.pack(side=LEFT)
        front_face = Button(row_one, text='F ', command = self.front_turn)
        front_face.pack(side=LEFT)
        right_face = Button(row_one, text='R ', command = self.right_turn)
        right_face.pack(side=LEFT)
        left_face = Button(row_one, text='L ', command = self.left_turn)
        left_face.pack(side=LEFT)
        back_face = Button(row_one, text='B ', command = self.back_turn)
        back_face.pack(side=LEFT)
        bottom_face = Button(row_one, text='D ', command = self.bottom_turn)
        bottom_face.pack(side=LEFT)
        row_one.pack(side=TOP)
        #second row of buttons: U' F' R' L' B' D'
        row_two = Frame()
        top_face_ccw = Button(row_two, text="U'", command = self.top_turn_ccw)
        top_face_ccw.pack(side=LEFT)
        front_face_ccw = Button(row_two, text="F'", command = self.front_turn_ccw)
        front_face_ccw.pack(side=LEFT)
        right_face_ccw = Button(row_two, text="R'", command = self.right_turn_ccw)
        right_face_ccw.pack(side=LEFT)
        left_face_ccw = Button(row_two, text=" L'", command = self.left_turn_ccw)
        left_face_ccw.pack(side=LEFT)
        back_face_ccw = Button(row_two, text="B'", command = self.back_turn_ccw)
        back_face_ccw.pack(side=LEFT)
        bottom_face_ccw = Button(row_two, text="D'", command = self.bottom_turn_ccw)
        bottom_face_ccw.pack(side=LEFT)
        row_two.pack(side=TOP)

        self.moveStack = []

        # Draw the cube
        self.draw_cube(400, 75, 60, 8)
        # creates a model to store its cube data
        self.cube = Cube()
        # correctly colors the faces on the drawn cube according to cube data
        self.recolor_faces()
        # handles key presses for manual button input
        parent.bind('<KeyPress>', self.onKeyPress)

    def draw_cube(self, x_origin, y_origin, side_width, space_width):
        """Draws a visual representation of a rubik's cube.
Currently only the top face is calibrated to make the entire face from variables"""
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

    def top_turn(self):
         self.cube.rotate_move(Cube.UCycle)
         self.recolor_faces()

    def front_turn(self):
        self.cube.rotate_move(Cube.FCycle)
        self.recolor_faces()

    def right_turn(self):
        self.cube.rotate_move(Cube.RCycle)
        self.recolor_faces()

    def left_turn(self):
        self.cube.rotate_move(Cube.LCycle)
        self.recolor_faces()

    def back_turn(self):
        self.cube.rotate_move(Cube.BCycle)
        self.recolor_faces()

    def bottom_turn(self):
        self.cube.rotate_move(Cube.DCycle)
        self.recolor_faces()

    def top_turn_ccw(self):
        self.cube.rotate_move(Cube.UCycle, inverse=True)
        self.recolor_faces()

    def front_turn_ccw(self):
        self.cube.rotate_move(Cube.FCycle, inverse=True)
        self.recolor_faces()

    def right_turn_ccw(self):
        self.cube.rotate_move(Cube.RCycle, inverse=True)
        self.recolor_faces()

    def left_turn_ccw(self):
        self.cube.rotate_move(Cube.LCycle, inverse=True)
        self.recolor_faces()

    def back_turn_ccw(self):
        self.cube.rotate_move(Cube.BCycle, inverse=True)
        self.recolor_faces()

    def bottom_turn_ccw(self):
        self.cube.rotate_move(Cube.DCycle, inverse=True)
        self.recolor_faces()

    def show_alg_execution(self, alg):
        moves = alg.split(' ')
        self.moveStack = moves
        self.animate_movestack()


    def animate_movestack(self):
        if not self.moveStack:
            return
        self.cube.execute_move(self.moveStack[0])
        self.moveStack = self.moveStack[1:]
        self.recolor_faces()

        self.master.after(RubiksShell.animationDelay, self.animate_movestack)


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

    def recolor_faces(self):
        """Recolor the faces of the rubik's cube. Color the visual representation"""
        faces = self.cube.faces
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
        if event.char == 't':
            self.show_alg_execution("R U R' U' R' F R2 U' R' U' R U R' F'")
        # if event.char == 'u':
        #     if self.my_cube.is_solved() == True:
        #         print("THE CUBE IS SOLVED")
        #         self.stop_timer()
        #     else:
        #         print("THE CUBE IS NOT YET SOLVED")

if __name__ == '__main__':
    window = Tk()
    shell = RubiksShell(window)
    #shell.cube.execute_algorithm("R U R' U' R' F R2 U' R' U' R U R' F'")
    shell.recolor_faces()
    window.mainloop()
