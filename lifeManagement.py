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
startTime = time.time()
pauseTime = 0
pauseBool = False
roundTime = time.time()
hours = 0
minutes = 0
seconds = 0
prevHours = 0

stdscr.addstr(5, 0, "quit: q    pause: p", curses.A_REVERSE)

while (ch != 113): #q
    curses.flushinp()
    curses.halfdelay(1)
    ch = stdscr.getch()
    if (ch == 112): #p
        ch = 0
        if (pauseBool == False):
            pauseBool = True
        else:
            pauseBool = False
    pastTime = roundTime
    roundTime = time.time()
    if (pauseBool):
        pauseTime = pauseTime + roundTime - pastTime
    currentTime = int(time.time() - startTime - pauseTime)
    hours = currentTime // 3600
    if (prevHours < hours):
        prevHours = hours
        with open('dataLifeManagement/hours.txt', 'a') as f:
            f.write(str(hours))
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


