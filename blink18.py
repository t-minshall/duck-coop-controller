from gpiozero import LED
import time
led=LED(18)
for _ in range(15):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
