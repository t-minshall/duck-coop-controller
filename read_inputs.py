#Write program to read inputs & flash LED appropriately based on which input is detected
#Tutorial source:  gpiozero docs page (https://gpiozero.readthedocs.io/en/stable/recipes.html)
#Read input, flash light
from gpiozero import LED, Button
import time

#Define sub-routines
def Flash_LED_open_cmd():
    print("Button detected: open-command")
    for _ in range(1)
        led.on()
        time.sleep(0.2)
        led.off()
        sleep(0.2)
    
def Flash_LED_close_cmd():
    print("Button detected: close-command")
    for _ in range(2)
        led.on()
        time.sleep(0.2)
        led.off()
        sleep(0.2)
    
def Flash_LED_stop_cmd():
    print("Button detected: stop-command")
    for _ in range(3)
        led.on()
        time.sleep(0.2)
        led.off()
        sleep(0.2)
    
def Flash_LED_open_sw():
    print("Button detected: open limit-switch")
    for _ in range(4)
        led.on()
        time.sleep(0.2)
        led.off()
        sleep(0.2)
    
def Flash_LED_closed_sw():
    print("Button detected: closed limit-switch")
    for _ in range(5)
        led.on()
        time.sleep(0.2)
        led.off()
        sleep(0.2)
    
def Flash_LED_torque_sw():
    print("Button detected: over-torque limit-switch")
    for _ in range(6)
        led.on()
        time.sleep(0.2)
        led.off()
        sleep(0.2)
    
def Flash_LED_latch_sw():
    print("Button detected: latch overide switch")
    for _ in range(7)
        led.on()
        time.sleep(0.2)
        led.off()
        sleep(0.2)
    
#Define all IO ports
led=LED(18)
buzzer=LED(25)
btn_open=Button(5)
btn_close=Button(6)
btn_stop=Button(13)
sw_open=Button(19)
sw_close=Button(26)
sw_torque=Button(20)
sw_latch=Button(21)
H_PL=LED(17)
H_PR=LED(27)
H_NL=LED(22)
H_NR=LED(23)

#main program
print("Waiting for input to be grounded:")
print("Open Button          GPIO-5     Header-29      1 flash      ")
print("Close Button         GPIO-6     Header-31      2 flashes    ")
print("Stop Button          GPIO-13    Header-33      3 flashes    ")
print("Open u-switch        GPIO-19    Header-35      4 flashes    ")
print("Closed u-switch      GPIO-26    Header-37      5 flashes    ")
print("Torque u-switch      GPIO-20    Header-38      6 flashes    ")
print("Latch disable sw     GPIO-21    Header-40      7 flashes    ")
while True:
    btn_open.when_pressed = Flash_LED("Open Command")
    btn_close.when_pressed = Flash_LED
    btn_stop.when_pressed = Flash_LED
    sw_open.when_pressed = Flash_LED
    sw_close.when_pressed = Flash_LED
    sw_torque.when_pressed = Flash_LED
    sw_latch.when_pressed = Flash_LED

#hang program, let "when_pressed" interrupts execute
#not sure how to debounce
#not sure how to prevent alternate inputs from interfering
#not sure how to pass an argument to "Flash_LED" so it can be more uniquely responsive
