import curses

screen = curses.initscr()

# Initialize color in a separate step
curses.start_color()
color = curses.can_change_color()
screen.addstr(f"Can this terminal do color? {color}\n")

# Change style: bold, highlighted, and underlined text
screen.addstr("Regular text\n")
screen.addstr("Bold\n", curses.A_BOLD)
screen.addstr("Highlighted\n", curses.A_STANDOUT)
screen.addstr("Underline\n", curses.A_UNDERLINE)
screen.addstr("Regular text again\n")

# Create a customer color set that you might re-use frequently
# Assign it a number (1-255), a foreground, and background color.
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
screen.addstr("RED ALERT!\n", curses.color_pair(1) | curses.A_BOLD | curses.A_BLINK)

screen.refresh()
screen.getch()
curses.endwin()
