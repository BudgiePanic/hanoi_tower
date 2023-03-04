from action import Action


class Board:
    def __init__(self, state, parent=None):
        # state should be a 2D list of integers
        self.state = state
        self.parent = parent
    
    def clone(self):
        stateCopy = []
        for peg in self.state:
            pegCopy = []
            for disc in peg:
                pegCopy.append(disc)
            stateCopy.append(pegCopy)
        return Board(stateCopy, parent=self)

    def move(self, fromPeg, toPeg):
        # assert fromPeg does not equal toPeg
        if fromPeg == toPeg:
            raise Exception("fromPeg cannot equal toPeg")
        # move the top disk from fromPeg to toPeg
        copy = self.clone()
        copy.state[toPeg].append(copy.state[fromPeg].pop())
        return copy

    def isValid(self):
        # state is a two dimensional list of integers
        # check if the pegs are sorted in descending order
        for peg in range(len(self.state)):
            for disc in range(len(self.state[peg]) - 1):
                if self.state[peg][disc] < self.state[peg][disc + 1]:
                    return False
        return True

    def generatePossibleMoves(self):
        moves = []
        for index in range(len(self.state)):
            peg = self.state[index]
            if len(peg) > 0:
                for other in range(len(self.state)):
                    if other != index:
                        move = Action(index, other)
                        if move.apply(self).isValid():
                            moves.append(move)
        return moves

    def __eq__(self, other):
        return self.state == other.state
    
    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    