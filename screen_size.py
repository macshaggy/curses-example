import curses

screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()
row = int(num_rows / 2)
col = int(num_cols / 2)
screen.addstr(row, col, 
              f"Screen size is {num_cols} columns and {num_rows} rows.")
screen.getkey()
curses.endwin()
