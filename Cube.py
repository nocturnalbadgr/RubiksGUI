class Cube(object):
    # Speffz notation; edges are lower case, corners are capital.
    # https://www.speedsolving.com/wiki/index.php/Speffz

    '''
    Every turn of a face affects 20 'stickers' (centers don't count). Each is part of a group that cycles among itself.
    If the same move is repeated, stickers will only ever move within their group. They can never cross over to another group.
    If the same move is repeated 4 times, all groups will be back in their starting position.
    '''

    # Some interesting patterns:
    UCycle = [['a', 'b', 'c', 'd'],  # These are the edges ON the face being turned
              ['q', 'm', 'i', 'e'],  # These are the four other edges affected by the face
              ['A', 'B', 'C', 'D'],  # These are the corners ON the face being turned
              ['Q', 'M', 'I', 'E'],
              # These are 4 of the eight corners affected but not on the face. Note that their addresses are the same as their related edges
              ['R', 'N', 'J', 'F']]  # The remaining affected corners

    LCycle = [['e', 'f', 'g', 'h'],
              ['d', 'l', 'x', 'r'],
              ['E', 'F', 'G', 'H'],
              ['D', 'L', 'X', 'R'],
              ['A', 'I', 'U', 'S']]

    FCycle = [['i', 'j', 'k', 'l'],
              ['c', 'p', 'u', 'f'],
              ['I', 'J', 'K', 'L'],
              ['C', 'P', 'U', 'F'],
              ['D', 'M', 'V', 'G']]

    RCycle = [['m', 'n', 'o', 'p'],
              ['b', 't', 'v', 'j'],
              ['M', 'N', 'O', 'P'],
              ['B', 'T', 'V', 'J'],
              ['C', 'Q', 'W', 'K']]

    BCycle = [['q', 'r', 's', 't'],
              ['a', 'h', 'w', 'n'],
              ['Q', 'R', 'S', 'T'],
              ['A', 'H', 'W', 'N'],
              ['B', 'E', 'X', 'O']]

    DCycle = [['u', 'v', 'w', 'x'],
              ['k', 'o', 's', 'g'],
              ['U', 'V', 'W', 'X'],
              ['K', 'O', 'S', 'G'],
              ['L', 'P', 'T', 'H']]

    faceMap = [['A', 'a', 'B', 'd', 'b', 'D', 'c', 'C'],
               ['I', 'i', 'J', 'l', 'j', 'L', 'k', 'K'],
               ['M', 'm', 'N', 'p', 'n', 'P', 'o', 'O'],
               ['E', 'e', 'F', 'h', 'f', 'H', 'g', 'G'],
               ['Q', 'q', 'R', 't', 'r', 'T', 's', 'S'],
               ['U', 'u', 'V', 'x', 'v', 'X', 'w', 'W']]
    faces = [[], [], [], [], [], []]

    centers = ['y', 'r', 'g', 'b', 'o', 'w']

    def __init__(self):
        self.state = {'a': 'y', 'b': 'y', 'c': 'y', 'd': 'y',
                      'e': 'b', 'f': 'b', 'g': 'b', 'h': 'b',
                      'i': 'r', 'j': 'r', 'k': 'r', 'l': 'r',
                      'm': 'g', 'n': 'g', 'o': 'g', 'p': 'g',
                      'q': 'o', 'r': 'o', 's': 'o', 't': 'o',
                      'u': 'w', 'v': 'w', 'w': 'w', 'x': 'w',
                      'A': 'y', 'B': 'y', 'C': 'y', 'D': 'y',
                      'E': 'b', 'F': 'b', 'G': 'b', 'H': 'b',
                      'I': 'r', 'J': 'r', 'K': 'r', 'L': 'r',
                      'M': 'g', 'N': 'g', 'O': 'g', 'P': 'g',
                      'Q': 'o', 'R': 'o', 'S': 'o', 'T': 'o',
                      'U': 'w', 'V': 'w', 'W': 'w', 'X': 'w'}
        self.getFaces()

    def rotateMove(self, cycleList, inverse=False):
        for cycle in cycleList:
            if inverse:
                newOrder = cycle[1:] + [cycle[0]]
            else:
                newOrder = [cycle[-1]] + cycle[0:-1]
            newValues = []
            for loc in newOrder:
                newValues.append(self.state[loc])
            for i in range(4):
                self.state[cycle[i]] = newValues[i]
        self.getFaces()

    def getFaces(self):
        '''Here we are bridging between two systems: The speffz mapping in this class and the face-wise matrix in the display class.'''
        for face in range(6):
            self.faces[face] = []
            for sticker in self.faceMap[face]:
                self.faces[face].append(self.state[sticker])
                if len(self.faces[face]) == 4:
                    self.faces[face].append(Cube.centers[face])  # Add the centers which are static (and always index 4)
        return self.faces
