#  This program operates the H-bridge in 1 direction for 2 seconds, then reverses for 2 seconds.
#  The program will execute this fwd/rev cycle a total of 5 times

from gpiozero import LED
import time
