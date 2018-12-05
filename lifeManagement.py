import time
import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

time.sleep(1)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

time.sleep(1)

#while (char != 'q'):
print(time.time())


