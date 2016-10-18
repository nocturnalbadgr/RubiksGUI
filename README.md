# RubiksGUI
A Rubiks Cube, implemented in tkinter and operational via button input or key
press.

### Usage
- Run `RubiksShell.py` somewhere with tkinter installed, like in IDLE

### Features
- Completely accurate, solvable Rubiks Cuble
- Single-key commands for clockwise rotation on each face
- Shift modifier for counterclockwise rotation on each face
- Scramble/reset/timer features to track improvements in speed

### What it does
- Manipulates the ThreeCube class defined in `Rubiks.py`
- Uses tkinter to draw, color, and recolor polygons on the Tkinter canvas

### What it doesn't do
- N/A

### Included Files
```
README.md.........................This readme file
Rubiks.py.........................Data representation of a Rubiks Cube
RubiksShell.py....................Wrapper to store ThreeCube and render GUI
quitbutton.py.....................A tkinter quit button class
diagrams/.........................Directory to store images
```

### Screenshots

![alt text][outputimage]
[outputimage]: https://github.com/ztaira14/RubiksGUI/blob/master/diagrams/RubiksGUI.png "Example Screenshot"
