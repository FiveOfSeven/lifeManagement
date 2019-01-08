import pygame
pygame.init()
beep = pygame.mixer.Sound('./dataLifeManagement/timesUp.wav')
#beep.play()

import time
import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(1)

#converts seconds to a time string
def secTime (timeSec):
    h = timeSec // 3600
    hl = timeSec % 3600
    m = hl // 60
    s = hl % 60
    return str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
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
alarm = -1
currentTimer = "play"
workTime = 0
playTime = 0
lastSeconds = -1
timeLeft = -1

stdscr.addstr(0, 0, "quit: q     pause: p     4 hour timer: f", curses.A_REVERSE)
stdscr.addstr(1, 0, "1 hour timer: r     30 minute timer: t     5 minute timer: e", curses.A_REVERSE)

while (ch != 113): #q
    curses.flushinp()
    curses.halfdelay(1)
    ch = stdscr.getch()
    pastTime = roundTime
    roundTime = time.time()
    currentTime = int(time.time() - startTime - pauseTime)
    hours = currentTime // 3600
    if (ch == 112): #p
        ch = 0
        if (pauseBool == False):
            pauseBool = True
        else:
            pauseBool = False
    elif (ch == 116): #t
        alarm = currentTime + 1800
        currentTimer = "work"
    elif (ch == 114): #r
        alarm = currentTime + 3600
        currentTimer = "work"
    elif (ch == 102): #f
        alarm = currentTime + 14400
        currentTimer = "work"
    elif (ch == 101): #e
        alarm = currentTime + 300
        currentTimer = "play"
    if (currentTime == alarm):
        beep.play()
        alarm = -1
        currentTimer = "play"

    if (pauseBool):
        pauseTime = pauseTime + roundTime - pastTime
    if (prevHours < hours):
        prevHours = hours
        with open('dataLifeManagement/hours.txt', 'a') as f:
            f.write(str(hours))
    leftoverHours = currentTime % 3600
    minutes = leftoverHours // 60
    lastSeconds = seconds
    seconds = leftoverHours % 60
    timeLeft = alarm - currentTime
    if (timeLeft < 0):
        timeLeft = 0
    if (lastSeconds != seconds):
        if (currentTimer == "work"):
            workTime += 1
        elif(currentTimer == "play"):
            playTime += 1
    workString = "    Work Time: " + secTime(workTime)
    playString = "    Play Time: " + secTime(playTime)
    stdscr.addstr(2, 0, blankString)
    stdscr.addstr(3, 0, blankString)
    stdscr.addstr(4, 0, blankString)
    stdscr.addstr(5, 0, blankString)
    stdscr.addstr(6, 0, blankString)
    stdscr.addstr(7, 0, blankString)
    stdscr.addstr(8, 0, blankString)
    stdscr.addstr(3, 0, "   Total Time: " + secTime(currentTime), curses.A_REVERSE)
    stdscr.addstr(4, 0, workString, curses.A_REVERSE)
    stdscr.addstr(5, 0, playString, curses.A_REVERSE)
    stdscr.addstr(6, 0, "Current Timer: " + currentTimer, curses.A_REVERSE)
    stdscr.addstr(7, 0, "    Time Left: " + secTime(timeLeft), curses.A_REVERSE)
    stdscr.addstr(8, 0, str(counter), curses.A_REVERSE)
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


