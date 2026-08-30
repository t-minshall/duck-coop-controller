from gpiozero import LED
import time
T5=LED(23)
LED10=LED(18)

for _ in range(5):
    LED10.on()
    T5.off()
    print("light on,  transistor off")
    time.sleep(1.4)
    LED10.off()
    T5.on()
    print("light off, transistor on")
    time.sleep(1.4)
