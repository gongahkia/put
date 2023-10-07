# FUA
# - DEBUG EXISITING PROGRAM
# - handle scrolling screen
# - handle cursor movement
# - implement vim key binds
    # 1. COMMAND MODE
        # - to NORMAL MODE with esc
        # - write files with :w enter
        # - write and quit file with :wq enter
        # - quit file with :q
        # - quit file if there was an edit that you dont wanna save with :q!
    # 2. NORMAL MODE 
        # to COMMAND MODE with :
        # to INSERT MODE with i, I, a, A, o, O 
        # to VISUAL MODE with v
    # 3. INSERT MODE
        # to NORMAL MODE with esc
    # 4. VISUAL MODE
        # to NORMAL MODE with esc
# - subsequently implementing opening a local file

# ----------

# required imports
from enum import Enum
import curses
import time

# ----------

class mode(Enum):
    Command = 1
    Normal = 2
    Insert = 3
    Visual = 4

def main(stdscr):
    current_mode = mode.Normal # default start mode
    file_name:str = "" # FUA: initial file name, later when able to edit existing files, add that value to this variable

    text_buffer:str = ""
    curses.curs_set(0) # hide cursor

    while True:

        match current_mode:

            # FUA:
            # - implement check to see whether a file has been written to
            # - implement command :q that allows quitting of PUT if file has not been written to
            # - implement command for :q that does not allow a new file just created to be quit normally with :q if it is empty
            case mode.Command:
                curses.nocbreak() # require enter to be pressed to register keypress buffer
                char_buffer = stdscr.getch()

                stdscr.erase()
                stdscr.addstr(0,15,"Command mode")
                stdscr.addstr(2,0,f"{text_buffer}_")
                stdscr.refresh() 

                if char_buffer == ord("w"):
                    stdscr.erase()
                    stdscr.addstr(0,15,"Changes written to file.")
                    stdscr.addstr(2,0,f"{text_buffer}_")
                    stdscr.refresh() 
                    if len(file_name) == 0:
                        curses.cbreak()
                        while True:
                            stdscr.erase()
                            stdscr.addstr(0,15,f"Enter file name: {file_name}_")
                            stdscr.addstr(2,0,f"{text_buffer}_")
                            stdscr.refresh() 
                            char_buffer = stdscr.getch()
                            if char_buffer == curses.KEY_BACKSPACE: # backspace
                                file_name = file_name[:-1]
                            elif char_buffer == ord("\t"): # tab
                                file_name += "\t"
                            elif char_buffer == curses.KEY_UP or char_buffer == curses.KEY_DOWN or char_buffer == curses.KEY_LEFT or char_buffer == curses.KEY_RIGHT:
                                pass
                            elif char_buffer == curses.KEY_ENTER: # enter to save file name
                                break
                            else:
                                file_name += chr(char_buffer)
                    fhand = open(file_name, "w")
                    fhand.write(text_buffer)
                    fhand.close()
                    current_mode = mode.Normal

                elif char_buffer == ord("wq"):
                    stdscr.erase()
                    stdscr.addstr(0,15,"Changes written to file. Exiting.")
                    stdscr.addstr(2,0,f"{text_buffer}_")
                    stdscr.refresh() 

                    if len(file_name) == 0:
                        curses.cbreak()
                        while True:
                            stdscr.erase()
                            stdscr.addstr(0,15,f"Enter file name: {file_name}_")
                            stdscr.addstr(2,0,f"{text_buffer}_")
                            stdscr.refresh() 
                            char_buffer = stdscr.getch()
                            if char_buffer == curses.KEY_BACKSPACE: # backspace
                                file_name = file_name[:-1]
                            elif char_buffer == ord("\t"): # tab
                                file_name += "\t"
                            elif char_buffer == curses.KEY_UP or char_buffer == curses.KEY_DOWN or char_buffer == curses.KEY_LEFT or char_buffer == curses.KEY_RIGHT:
                                pass
                            elif char_buffer == curses.KEY_ENTER: # enter to save file name
                                break
                            else:
                                file_name += chr(char_buffer)
                    fhand = open(file_name, "w")
                    fhand.write(text_buffer)
                    fhand.close()
                    current_mode = mode.Normal
                    break

                elif char_buffer == ord("q!"):
                    stdscr.erase()
                    stdscr.addstr(0,15,"Exiting file without saving.")
                    stdscr.addstr(2,0,f"{text_buffer}_")
                    stdscr.refresh() 
                    break

            # FUA:
            # - implement entering insert mode using I, a, A, o, O as well
            # - implement movement using hjklG and w b and the combination of numbers and movement keys as well
            case mode.Normal:
                curses.cbreak()
                char_buffer = stdscr.getch()

                if char_buffer == ord("i"):
                    current_mode = mode.Insert
                    continue
                elif char_buffer == ord(":"):
                    current_mode = mode.Command 
                    continue
                else:
                    stdscr.erase()
                    stdscr.addstr(0,15,"Normal mode")
                    stdscr.addstr(2,0,f"{text_buffer}_")
                    stdscr.refresh() 

            # FUA:
            # - implement any additonal special keys similar to the arrow keys that i need to ignore
            case mode.Insert:
                char_buffer = stdscr.getch()

                if char_buffer == 27: # escape to normal mode
                    current_mode = mode.Normal
                    
                elif char_buffer == curses.KEY_BACKSPACE: # backspace
                    text_buffer = text_buffer[:-1]
                elif char_buffer == curses.KEY_ENTER: # enter
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

            # FUA:
            # - implement entering visual mode using small v, large V etc 
            case mode.Visual:
                char_buffer = stdscr.getch()

    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
