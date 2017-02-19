#!/usr/bin/env python

import unittest
from context import tictactoe


class TicTacToeTest(unittest.TestCase):
    won_states = """XXX......
...XXX...
......XXX
X..X..X..
.X..X..X.
..X..X..X"""
    not_won_states = """XOX......
.........
...OXX...
.O..X..X.
..O..X..X"""
    invalid_length = """XX.....XX.
XOXO...
."""
    invalid_state = """
123456789
abjsoeo39
xoxoxx..."""

    def test_won(self):
        for state in self.won_states.split('\n'):
            self.assertTrue(tictactoe.TicTacToe(state).won)

    def test_not_won(self):
        for state in self.not_won_states.split('\n'):
            self.assertFalse(tictactoe.TicTacToe(state).won)

    def test_input_length(self):
        for state_input in self.invalid_length.split('\n'):
            self.assertRaises(ValueError, tictactoe.TicTacToe, state_input)

    def test_input_state(self):
        for state_input in self.invalid_state.split('\n'):
            self.assertRaises(ValueError, tictactoe.TicTacToe, state_input)


if __name__ == "__main__":
    unittest.main()
