import curses
import subprocess
import os

# Create a screen and print hello
screen = curses.initscr()
screen.addstr("Hello! Dropping you in to a command prompt...\n")
print("Program initialized...")
screen.refresh()
screen.getkey()

# Hide the screen, show original terminal, restore cursor position
curses.endwin()

# Update screen in background
screen.addstr("I'll be waiting for you when you return.\n")

# Drop the user in a command prompt
print("About to open command prompt...")
screen.getkey()

if os.name == "nt":
    shell = "pwsh.exe"
else:
    shell = "bash"

subprocess.call(shell)

# When the subprocess ends, return to our screen.
# also restoring cursor position
screen.refresh()
screen.getkey()

# Finally go back to the terminal for real
curses.endwin()
