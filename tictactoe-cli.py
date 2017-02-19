#!/usr/bin/env python

""" Curses interface for the Tic-tac-toe Game. """

import curses
from curses import wrapper
import tictactoe

LOCATIONS = {(0, 0): 0,
             (0, 2): 1,
             (0, 4): 2,
             (2, 0): 3,
             (2, 2): 4,
             (2, 4): 5,
             (4, 0): 6,
             (4, 2): 7,
             (4, 4): 8}


def main(stdscr):
    stdscr.immedok(True)

    win = curses.newwin(16, 16, 2, 4)
    win.keypad(True)
    win.immedok(True)

    ttt = tictactoe.TicTacToe()
    win.addstr(str(ttt))
    win.move(2, 2)

    while True:
        char = win.getch()
        if char == ord('q'):
            break
        elif char == ord(' '):
            current_loc = win.getyx()
            current_char = chr(win.inch(*current_loc))
            if current_char == ".":
                ttt = ttt.move(LOCATIONS[current_loc])
                win.clear()
                win.addstr(str(ttt))
                win.move(*current_loc)
        elif curses.KEY_DOWN <= char <= curses.KEY_RIGHT:
            cur_y, cur_x = win.getyx()
            if char == curses.KEY_UP and cur_y-2 >= 0:
                    win.move(cur_y-2, cur_x)
            elif char == curses.KEY_DOWN and cur_y+2 < 5:
                    win.move(cur_y+2, cur_x)
            elif char == curses.KEY_LEFT and cur_x-2 >= 0:
                    win.move(cur_y, cur_x-2)
            elif char == curses.KEY_RIGHT and cur_x+2 < 5:
                    win.move(cur_y, cur_x+2)
        if ttt.won:
            win.addstr(6, 0, "Winner is {}!".format(ttt.winner))
            win.addstr(7, 1, " ('q' to quit)")


if __name__ == "__main__":
    wrapper(main)
