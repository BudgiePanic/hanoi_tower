class Action:
    def __init__(self, fromPeg, toPeg):
        self.fromPeg = fromPeg
        self.toPeg = toPeg

    def apply(self, board):
        return board.move(self.fromPeg, self.toPeg)

    def __eq__(self, other):
        return self.fromPeg == other.fromPeg and self.toPeg == other.toPeg

    # define to string method
    def __str__(self):
        return "Move from peg " + str(self.fromPeg) + " to peg " + str(self.toPeg)
    
    # define representation method
    def __repr__(self):
        return str(self)
