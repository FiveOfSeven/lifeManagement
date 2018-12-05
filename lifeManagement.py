import time
import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(1)

time.sleep(1)

curses.start_color()
curses.halfdelay(100)
ch = stdscr.getch()
if (ch == 113):
    stdscr.addstr(0, 0, "you made it hahahaha... Current mode: Typing mode", curses.A_REVERSE)
    stdscr.refresh()

time.sleep(2)

stdscr.addstr(0, 0, "Current mode: Typing mode", curses.A_REVERSE)
stdscr.refresh()

time.sleep(4)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

time.sleep(1)

#while (char != 'q'):
print(time.time())
print(ch)


