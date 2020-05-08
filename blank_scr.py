# clear the screen and hold it for 3 seconds
import curses
import time

screen = curses.initscr()
screen.clear()
print("hello")

time.sleep(3)