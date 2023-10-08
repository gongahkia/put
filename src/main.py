# FUA
# - handle scrolling screen
# - handle cursor movement
# - handle opening of file from CLI using a `put` command

# vim time :)

# - implement modes using enums 
    # use match case statement to determine current mode of editor
"""class mode(Enum):
    Command = 1
    Normal = 2
    Insert = 3
    Visual = 4
"""
# - implement vim key binds
    # 1. COMMAND MODE
        # - to NORMAL MODE with esc
        # - write files with :w enter
        # - write and quit file with :wq enter
        # - quit file with :q
        # - quit file if there was an edit that you dont wanna save with :q!
            # - implement check to see whether a file has been written to
            # - implement command :q that allows quitting of PUT if file has not been written to
            # - implement command for :q that does not allow a new file just created to be quit normally with :q if it is empty
    # 2. NORMAL MODE 
        # to COMMAND MODE with :
        # to INSERT MODE with i, I, a, A, o, O 
        # to VISUAL MODE with v
            # - implement entering insert mode using I, a, A, o, O as well
            # - implement movement using hjklG and w b and the combination of numbers and movement keys as well
    # 3. INSERT MODE
        # to NORMAL MODE with esc
            # - implement any additonal special keys similar to the arrow keys that i need to ignore
    # 4. VISUAL MODE
        # to NORMAL MODE with esc
            # - implement entering visual mode using small v, large V etc 
# - subsequently implementing opening a local file

# ----------

# required imports
from enum import Enum
import curses
import time

# ----------

def main(stdscr):
    file_name:str = "" # FUA: initial file name, later when able to edit existing files, add that value to this variable
    text_buffer:str = ""
    curses.curs_set(0) # hide cursor

    while True:

        char_buffer = stdscr.getch()

        if char_buffer == 27: # escape quits the editor and saves file as a text file
            file_name_buffer = ""
            if file_name == "":
                stdscr.erase()
                stdscr.addstr(0,15,f"File name: {file_name}_")
                stdscr.addstr(2,0,f"{text_buffer}_")
                stdscr.refresh() 
                while True:
                    file_name_buffer = stdscr.getch()
                    if file_name_buffer == curses.KEY_BACKSPACE: # backspace
                        file_name = text_buffer[:-1]
                    elif file_name_buffer == curses.KEY_ENTER or file_name_buffer == 10: # enter
                        fhand = open(f"{file_name}.txt", "w")
                        fhand.write(text_buffer)
                        fhand.close()
                        break
                    elif file_name_buffer == ord("\t"): # tab
                        file_name += "\t"
                    elif file_name_buffer == curses.KEY_UP or char_buffer == curses.KEY_DOWN or char_buffer == curses.KEY_LEFT or char_buffer == curses.KEY_RIGHT:
                        pass
                    else:
                        file_name += chr(file_name_buffer)
                    stdscr.erase()
                    stdscr.addstr(0,15,f"File name: {file_name}_")
                    stdscr.addstr(2,0,f"{text_buffer}_")
                    stdscr.refresh() 
            break
            
        elif char_buffer == curses.KEY_BACKSPACE: # backspace
            text_buffer = text_buffer[:-1]
        elif char_buffer == curses.KEY_ENTER or char_buffer == 10: # enter
            text_buffer += "\n"
        elif char_buffer == ord("\t"): # tab
            text_buffer += "\t"
        elif char_buffer == curses.KEY_UP or char_buffer == curses.KEY_DOWN or char_buffer == curses.KEY_LEFT or char_buffer == curses.KEY_RIGHT:
            pass
        else:
            text_buffer += chr(char_buffer)

        stdscr.erase()
        stdscr.addstr(0,15,"Insert mode")
        stdscr.addstr(2,0,f"{text_buffer}_")
        stdscr.refresh() 

    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
