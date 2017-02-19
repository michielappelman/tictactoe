#!/usr/bin/env python

""" Tic-tac-toe Game. """


class InvalidMove(Exception):
    """ Raised when a move is made on an invalid position. """
    pass


class TicTacToe:
    def __init__(self, state=None):
        self.winner = None
        if state is None:
            self.state = "." * 9
        elif not isinstance(state, str) or len(state) != 9:
            raise ValueError
        else:
            self.state = state

    def __str__(self):
        return "\n-----\n".join("|".join(self.state[start:start + 3]) for start in range(0, 9, 3))

    def __repr__(self):
        return f"{type(self).__name__}('{self.state}')"

    def _split_state(self):
        return ["".join(self.state[start:start + 3]) for start in range(0, 9, 3)]

    @classmethod
    def _full_line(cls, line):
        if line[0] != "." and line == line[0] * 3:
            return line[0]
        else:
            return False

    @property
    def won(self):
        # Horizontal line win
        for row in self._split_state():
            full_line = self._full_line(row)
            if full_line:
                self.winner = full_line
                return True
        # Verical line win
        for column in zip(*self._split_state()):
            full_line = self._full_line("".join(column))
            if full_line:
                self.winner = full_line
                return True
        # Diagonal line win
        diagonals = [self.state[0:9:4], self.state[2:7:2]]
        for diagonal in diagonals:
            full_line = self._full_line(diagonal)
            if full_line:
                self.winner = full_line
                return True
        return False

    def move(self, position):
        if self.won:
            return self
        if self.state[position] != ".":
            raise InvalidMove(position)
        if self.state.count(".") % 2 == 0:
            turn = "O"
        else:
            turn = "X"
        new_state = list(self.state)
        new_state[position] = turn
        return TicTacToe("".join(new_state))


def main():
    ttt = TicTacToe()
    while not ttt.won:
        print(ttt)
        play = input("Play: ")
        ttt = ttt.move(int(play))
    print("Winner:", ttt.winner)


if __name__ == "__main__":
    main()
