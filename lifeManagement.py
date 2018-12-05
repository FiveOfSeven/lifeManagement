import time
import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(1)

ch = 0
counter = 0
blankString = "                                                 "

while (ch != 113):
    curses.halfdelay(10)
    ch = stdscr.getch()
    #currentTime = time.time()
    currentTime = counter
    hours = currentTime // 3600
    leftoverHours = currentTime % 3600
    minutes = leftoverHours // 60
    seconds = leftoverHours % 60
    hours = "  Hours: " + str(hours)
    minutes = "Minutes: " + str(minutes)
    seconds = "Seconds: " + str(seconds)
    stdscr.addstr(0, 0, blankString)
    stdscr.addstr(1, 0, blankString)
    stdscr.addstr(2, 0, blankString)
    stdscr.addstr(0, 0, hours, curses.A_REVERSE)
    stdscr.addstr(1, 0, minutes, curses.A_REVERSE)
    stdscr.addstr(2, 0, seconds, curses.A_REVERSE)
    stdscr.addstr(4, 0, str(counter), curses.A_REVERSE)
    stdscr.refresh()
    counter = counter + 1
    


curses.start_color()
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()


print(time.time())
print(seconds)
print(ch)


