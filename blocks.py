from block import Block
from position import Position

#we have 7 type of blocks : L-Block, J-Block, I-Block, O-Block, S-Block, T-Block, Z-Block
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            #rotation state from 0 to 3
            0: [Position(0,2), Position(1, 0), Position(1, 1), Position(1,2)],
            1: [Position(0,1), Position(1, 1), Position(2, 1), Position(2,2)],
            2: [Position(1,0), Position(1, 1), Position(1, 2), Position(2,0)],
            3: [Position(0,0), Position(0, 1), Position(1, 1), Position(2,1)]
        }
        self.move(0,3)

class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            #rotation state from 0 to 3
            0: [Position(0,0), Position(1, 0), Position(1, 1), Position(1,2)],
            1: [Position(0,1), Position(0, 2), Position(1, 1), Position(2,1)],
            2: [Position(1,0), Position(1, 1), Position(1, 2), Position(2,2)],
            3: [Position(0,1), Position(1, 1), Position(2, 0), Position(2,1)]
        }
        self.move(0,3)
class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            #rotation state from 0 to 3
            0: [Position(1,0), Position(1, 1), Position(1, 2), Position(1,3)],
            1: [Position(0,3), Position(1,3), Position(2,3), Position(3,3)],
            2: [Position(2,0), Position(2, 1), Position(2, 2), Position(2,3)],
            3: [Position(0,1), Position(1, 1), Position(2, 1), Position(3,1)]
        }
        self.move(-1,3)
class TBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            #rotation state from 0 to 3
            0: [Position(0,1), Position(1, 0), Position(1, 1), Position(1,2)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1, 1), Position(1, 2), Position(2,1)],
            3: [Position(0,1), Position(1, 0), Position(1, 1), Position(2,1)]
        }
        self.move(0,3)
class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            #rotation state from 0 to 3
            0: [Position(0,0), Position(0, 1), Position(1, 1), Position(1,2)],
            1: [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1, 1), Position(2, 1), Position(2,2)],
            3: [Position(0,1), Position(1, 0), Position(1, 1), Position(2,0)]
        }
        self.move(0,3)
class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            #rotation state from 0 to 3
            0: [Position(0,1), Position(0, 2), Position(1, 0), Position(1,1)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],
            2: [Position(1,1), Position(1, 2), Position(2, 0), Position(2,1)],
            3: [Position(0,0), Position(1, 0), Position(1, 1), Position(2,1)]
        }
        self.move(0,3)
class OBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            #rotation state from 0 to 3
            0: [Position(0,0), Position(0, 1), Position(1, 0), Position(1,1)],
        }
        self.move(-1,4)
