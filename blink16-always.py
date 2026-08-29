from gpiozero import LED
import time
led=LED(16)
#while True:
#    led.on()
#    time.sleep(0.5)
#    led.off()
#    time.sleep(0.5)
while True:
    for _ in range(3):
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.2)
    time.sleep(0.8)
