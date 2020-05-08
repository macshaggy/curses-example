import curses

screen = curses.initscr()

screen.addstr(0, 0, "This string gets printed at position (0, 0)")
screen.addstr(4, 4, "X")
screen.addstr(5, 5, "Y")
screen.addstr(30, 70, "Z")

screen.refresh()

curses.napms(3000)
curses.endwin()
