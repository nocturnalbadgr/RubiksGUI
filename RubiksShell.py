from tkinter import *
import random
import Rubiks
import quitbutton

help_string = '''Rotations:
htns = left, top, right, bottom
wtc = front, top, back
aoe = x, y, and z axes
;qj = x, y, and z axis slices
shift for counter-clockwise
Space = scramble and start timer
u = check if solved
r = reset cube to solved state'''


class RubiksShell(Frame):
    """This is a class meant to display a GUI for the Rubiks class"""
    def __init__(self, parent):
        Frame.__init__(self, parent)
        # Create Canvas, store canvas items
        self.canvas = Canvas(parent, width=800, height=650)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas_items = [[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],
                             [3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5]]
        """
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
        #third row of buttons
        row_three = Frame()
        middle_x = Button(row_three, text='Mx', command = self.middle_x)
        middle_x.pack(side=LEFT)
        middle_x_ccw = Button(row_three, text = "Mx'", command = self.middle_x_ccw)
        middle_x_ccw.pack(side=LEFT)
        middle_y = Button(row_three, text='My', command = self.middle_y)
        middle_y.pack(side=LEFT)
        middle_y_ccw = Button(row_three, text = "My'", command = self.middle_y_ccw)
        middle_y_ccw.pack(side=LEFT)
        middle_z = Button(row_three, text='Mz', command = self.middle_z)
        middle_z.pack(side=LEFT)
        middle_z_ccw = Button(row_three, text = "Mz'", command = self.middle_z_ccw)
        middle_z_ccw.pack(side=LEFT)
        row_three.pack(side=TOP)
        #fourth row of buttons
        row_four = Frame()
        rotate_x = Button(row_four, text='X', command = self.turn_x)
        rotate_x.pack(side=LEFT)
        rotate_x_ccw = Button(row_four, text="X'", command = self.turn_x_ccw)
        rotate_x_ccw.pack(side=LEFT)
        rotate_y = Button(row_four, text='Y', command = self.turn_y)
        rotate_y_ccw = Button(row_four, text="Y'", command = self.turn_y_ccw)
        rotate_y.pack(side=LEFT)
        rotate_y_ccw.pack(side=LEFT)
        rotate_z = Button(row_four, text='Z', command = self.turn_z)
        rotate_z_ccw = Button(row_four, text="Z'", command = self.turn_z_ccw)
        rotate_z.pack(side=LEFT)
        rotate_z_ccw.pack(side=LEFT)
        row_four.pack(side=TOP)
        #fifth row of buttons:
        row_five = Frame()
        cube_print = Button(row_five, text='PRINT THE CUBE', command = self.print_cube)
        cube_print.pack(side=LEFT)
        cube_reset = Button(row_five, text='Reset', command=self.reset)
        cube_reset.pack(side=LEFT)
        cube_scramble = Button(row_five, text='Scramble', command=self.scramble)
        cube_scramble.pack(side=LEFT)
        row_five.pack(side=TOP)
        self.pack()
        """
        # Draw the cube
        self.draw_cube(400, 75, 60, 8)
        # creates a model to store its cube data
        self.my_cube = Rubiks.ThreeCube()
        # correctly colors the faces on the drawn cube according to cube data
        self.recolor_faces()
        # handles key presses for manual button input
        parent.bind('<KeyPress>', self.onKeyPress)
        # displays help text
        self.help_text_display = self.canvas.create_text(10, 640, anchor=SW, font='courier', text=help_string)
        # timer variables
        self.current_time = 0
        self.msecs = 1000
        self.current_time_display = self.canvas.create_text(790, 640, anchor=SE, font='courier', text=self.current_time)
        self._job = None

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
        """Turns the top face of my_cube clockwise"""
        self.my_cube.top_turn()
        self.recolor_faces()

    def front_turn(self):
        """Turns the front face of my_cube clockwise"""
        self.my_cube.front_turn()
        self.recolor_faces()

    def right_turn(self):
        """Turns the right face of my_cube clockwise"""
        self.my_cube.right_turn()
        self.recolor_faces()

    def left_turn(self):
        """Turns the left face of my_cube clockwise"""
        self.my_cube.left_turn()
        self.recolor_faces()

    def back_turn(self):
        """Turns the back face of my_cube clockwise"""
        self.my_cube.back_turn()
        self.recolor_faces()

    def bottom_turn(self):
        """Turns the bottom face of my_cube clockwise"""
        self.my_cube.bottom_turn()
        self.recolor_faces()

    def top_turn_ccw(self):
        """Turns the top face of my_cube counterclockwise"""
        self.my_cube.top_turn_ccw()
        self.recolor_faces()

    def front_turn_ccw(self):
        """Turns the front face of my_cube counterclockwise"""
        self.my_cube.front_turn_ccw()
        self.recolor_faces()

    def right_turn_ccw(self):
        """Turns the right face of my_cube counterclockwise"""
        self.my_cube.right_turn_ccw()
        self.recolor_faces()

    def left_turn_ccw(self):
        """Turns the left face of my_cube counterclockwise"""
        self.my_cube.left_turn_ccw()
        self.recolor_faces()

    def back_turn_ccw(self):
        """Turns the back face of my_cube counterclockwise"""
        self.my_cube.back_turn_ccw()
        self.recolor_faces()

    def bottom_turn_ccw(self):
        """Turns the bottom face of my_cube counterclockwise"""
        self.my_cube.bottom_turn_ccw()
        self.recolor_faces()

    def middle_x(self):
        """Rotates the middle x-axis slice clockwise"""
        self.my_cube.middle_turn_x()
        self.recolor_faces()

    def middle_x_ccw(self):
        """Rotates the middle x-axis slice counterclockwise"""
        self.my_cube.middle_turn_x_ccw()
        self.recolor_faces()

    def middle_y(self):
        """Rotates the middle y-axis slice clockwise"""
        self.my_cube.middle_turn_y()
        self.recolor_faces()

    def middle_y_ccw(self):
        """Rotates the middle y-axis slice counterclockwise"""
        self.my_cube.middle_turn_y_ccw()
        self.recolor_faces()

    def middle_z(self):
        """Rotates the middle z-axis slice clockwise"""
        self.my_cube.middle_turn_z()
        self.recolor_faces()

    def middle_z_ccw(self):
        """Rotates the middle z-axis slice counterclockwise"""
        self.my_cube.middle_turn_z_ccw()
        self.recolor_faces()

    def print_cube(self):
        """prints the layout of my_cube to shell"""
        self.my_cube.print_cube()
        self.recolor_faces()

    def turn_x(self):
        """rotates the cube around the x axis clockwise"""
        self.my_cube.rotate_cube_x()
        self.recolor_faces()

    def turn_x_ccw(self):
        """rotates the cube around the x-axis counterclockwise)"""
        self.my_cube.rotate_cube_x_ccw()
        self.recolor_faces()

    def turn_y(self):
        """rotates the cube around the Y axis clockwise"""
        self.my_cube.rotate_cube_y()
        self.recolor_faces()

    def turn_y_ccw(self):
        """rotates the cube around the y-axis counterclockwise)"""
        self.my_cube.rotate_cube_y_ccw()
        self.recolor_faces()

    def turn_z(self):
        """rotates the cube around the z axis clockwise"""
        self.my_cube.rotate_cube_z()
        self.recolor_faces()

    def turn_z_ccw(self):
        """rotates the cube around the z-axis counterclockwise)"""
        self.my_cube.rotate_cube_z_ccw()
        self.recolor_faces()

    def reset(self):
        """Resets the cube to a solved state"""
        self.my_cube.reset()
        print('DONT CHEAT NEXT TIME')
        self.recolor_faces()

    def scramble(self):
        """Scrambles the cube"""
        for turn in range(100):
            turn_type = random.randrange(12)
            if turn_type == 0:
                self.top_turn()
            elif turn_type == 1:
                self.front_turn()
            elif turn_type == 2:
                self.right_turn()
            elif turn_type == 3:
                self.left_turn()
            elif turn_type == 4:
                self.back_turn()
            elif turn_type == 5:
                self.bottom_turn()
            elif turn_type == 6:
                self.top_turn_ccw()
            elif turn_type == 7:
                self.front_turn_ccw()
            elif turn_type == 8:
                self.right_turn_ccw()
            elif turn_type == 9:
                self.left_turn_ccw()
            elif turn_type == 10:
                self.back_turn_ccw()
            elif turn_type == 11:
                self.bottom_turn_ccw()
            else:
                print("You don't understand random numbers, do you?")

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
        for face in range(6):
            for slot in range(9):
                if int(self.my_cube.faces[face][slot])<10:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='blue')
                elif int(self.my_cube.faces[face][slot])<20:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='white')
                elif int(self.my_cube.faces[face][slot])<30:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='red')
                elif int(self.my_cube.faces[face][slot])<40:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='orange')
                elif int(self.my_cube.faces[face][slot])<50:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='yellow')
                elif int(self.my_cube.faces[face][slot])<60:
                    self.canvas.itemconfig(self.canvas_items[face][slot], fill='green')

    def onKeyPress(self, event):
        """Handles Key Presses so cube can be controlled through keyboard"""
        # Basic face rotations
        if event.char == 'h':
            self.left_turn()
        elif event.char == 't':
            self.top_turn()
        elif event.char == 'n':
            self.right_turn()
        elif event.char == 's':
            self.bottom_turn()
        elif event.char == 'c':
            self.back_turn()
        elif event.char == 'w':
            self.front_turn()
        elif event.char == 'H':
            self.left_turn_ccw()
        elif event.char == 'T':
            self.top_turn_ccw()
        elif event.char == 'N':
            self.right_turn_ccw()
        elif event.char == 'S':
            self.bottom_turn_ccw()
        elif event.char == 'C':
            self.back_turn_ccw()
        elif event.char == 'W':
            self.front_turn_ccw()
        # These are cube rotations
        elif event.char == 'a':
            self.turn_x()
        elif event.char == 'o':
            self.turn_y()
        elif event.char == 'e':
            self.turn_z()
        elif event.char == 'A':
            self.turn_x_ccw()
        elif event.char == 'O':
            self.turn_y_ccw()
        elif event.char == 'E':
            self.turn_z_ccw()
        # These are slice rotations
        elif event.char == ';':
            self.middle_x()
        elif event.char == ':':
            self.middle_x_ccw()
        elif event.char == 'q':
            self.middle_y()
        elif event.char == 'Q':
            self.middle_y_ccw()
        elif event.char == 'j':
            self.middle_z()
        elif event.char == 'J':
            self.middle_z_ccw()
        # Miscellaneous button presses
        elif event.char == 'r':
            self.reset()
        elif event.char == ' ':
            self.scramble()
            self.current_time = 0
            self.start_timer()
        elif event.char == 'u':
            if self.my_cube.is_solved() == True:
                print("THE CUBE IS SOLVED")
                self.stop_timer()
            else:
                print("THE CUBE IS NOT YET SOLVED")

    def start_timer(self):
        """Starts the timer"""
        # variables are current_time, msecs
        self.current_time = self.current_time+self.msecs
        self.canvas.delete(self.current_time_display)
        self.current_time_display = self.canvas.create_text(790, 640, anchor=SE, font='courier', text=self.current_time/1000)
        self._job = self.after(self.msecs, self.start_timer)

    def stop_timer(self):
        """Stops the timer"""
        if self._job is not None:
            self.after_cancel(self._job)
            self._job = None

if __name__ == '__main__':
    window = Tk()
    quitter = quitbutton.quitButton(window)
    shell = RubiksShell(window)
