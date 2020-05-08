import curses

screen = curses.initscr()

curses.curs_set(0)
screen.addstr(2, 2, "Hello, I disabled the cursor!")
screen.refresh()
screen.getch()

curses.curs_set(1)
screen.addstr(2, 2, "And now it's back on.")
screen.refresh()
screen.getch()

curses.endwin()