#  This program operates the H-bridge in 1 direction for 2 seconds, then reverses for 2 seconds.
#  The program will execute this fwd/rev cycle a total of 5 times

from gpiozero import LED
import time
              #    Motor term.      Battery side     Wire to    Relay ID  Transistor  GPIO    Header pin
T2=LED(17)    #    Left armature    Positive side    X3-2       K1        T2          17      11
T3=LED(22)    #    Left armature    Negative side    X3-3       K2        T3          22      15
T4=LED(27)    #    Right armature   Positive side    X3-4       K3        T4          27      13
T5=LED(23)    #    Right armature   Negative side    X3-5       K4        T5          23      16
led=LED(18)   #    LED-10, driven by GPIO-18
led.off()
for _ in range(20):
  led.on()
  time.sleep(0.1)
  led.off()
  time.sleep(0.2)
T2.off()
T3.off()
T4.off()
T5.off()
time.sleep(0.1)
for _ in range(5):
    T2.on()
    T5.on()
    #T3.off()
    #T4.off()
    led.on()
    time.sleep(1.0)
    T2.off()
    T5.off()
    time.sleep(0.1)
    T3.on()
    T4.on()
    led.off()
    time.sleep(0.3)
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.3)
    led.on()
    time.sleep(0.1)
    led.off()
    T3.off()
    T4.off()
    time.sleep(0.1)
