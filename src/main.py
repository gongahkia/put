# FUA
# - implement escape from editor key
# - implement vim key binds
# - handle cursor movement

import curses

def main(stdscr):
    text_buffer:str = ""
    curses.curs_set(0)
    while True:
        char_buffer = stdscr.getch()

        if char_buffer == curses.KEY_BACKSPACE: # backspace
            text_buffer = text_buffer[:-1]
        elif char_buffer == curses.KEY_ENTER: # enter
            text_buffer += "\n"
        elif char_buffer == ord("\t"): # tab
            text_buffer += "\t"
        else:
            text_buffer += chr(char_buffer)

        stdscr.erase()
        stdscr.addstr(0,0,f"{text_buffer}_")
        stdscr.refresh() 

if __name__ == "__main__":
    curses.wrapper(main)
