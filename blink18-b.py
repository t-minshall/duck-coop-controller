from gpiozero import LED
import time
from signal import pause
led10 = LED(18)
#while True:
#  led10.blink(on_time=0.2, off_time=0.4)

led10.blink(on_time=0.2, off_time=0.4)
pause()
