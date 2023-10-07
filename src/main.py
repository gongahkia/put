import curses

# main-event loop
def main(stdscr):
    text_buffer:str = ""
    curses.curs_set(1)
    stdscr.addstr(0,0,text_buffer)
    stdscr.refresh()
    char_buffer = stdscr.getch()
    text_buffer += char_buffer
    if char_buffer == "!":
        curses.endwin()
    # add code here, just want keypress to translate to text on screen for now

if __name__ == "__main__":
    curses.wrapper(main)
