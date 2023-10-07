# FUA:
#   - watch entire playthrough of curses playlist by techwithtim here at https://youtu.be/Db4oc8qc9RU?si=vttv0z0YC23QDYEW
# - try write a text editor similar to https://youtu.be/UcE9yelzgD8?si=VmGrJxRxUa3tCIx2
# - try to opitmise it by writing it under 50 lines like him!

import curses

"""

stdscr = curses.initscr()
curses.noecho() # stops automatic echoing of keypresses to screen
curses.cbreak() # react to keypresses without need for enter key
stdscr.keypad(True) # enables other keys like arrow keys to be registered as keypresses
window.addstr(0,0,"shitass")
window.refresh() # refresh the display view window to reflect changes
key = stdscr.getch() # takes in user input

# boilerplate to exit the window
curses.nocbreak()
curses.keypad(False)
curses.echo()
curses.endwin() # restores terminal to its original state

"""

def testinguwu(stdscr):
    curses.curs_set(0) # hides the cursor
    stdscr.addstr(2, 10, "shit!") # adds string to window to be displayed
    stdscr.refresh() # refreshes window 
    stdscr.getch()  # waits to take in user input but does nothing with it
    curses.endwin()  # closes the curses window

if __name__ == "__main__":
    curses.wrapper(testinguwu) # curses.wrapper() takes in a function as per the function name, and helps with initialising all the boilerplate and cleaning up the curse environment when terminating the window
