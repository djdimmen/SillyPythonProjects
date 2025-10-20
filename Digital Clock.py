"""Digital Clock, by Al Sweigart al@inventwithpython.com
Displays a digital clock of the current time with a seven-segment
display. Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic"""

import sys, time
import sevseg  # Imports our sevseg.py program.

try:
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the current time from the computer's clock:z
        current