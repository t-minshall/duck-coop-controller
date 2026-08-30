from gpiozero import LED
import time
led10 = LED(18)
while True:
  led10.blink()
