#Write program to read inputs & flash LED appropriately based on which input is detected
#Tutorial source:  gpiozero docs page (https://gpiozero.readthedocs.io/en/stable/recipes.html)
#Read input, flash light
from gpiozero import LED, Button
import time

#Define sub-routines
def Flash_LED():
    print("Button detected")
    
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
print("Open Button          GPIO-5     Header-29  ")
print("Close Button         GPIO-6     Header-31  ")
print("Stop Button          GPIO-13    Header-33  ")
print("Open u-switch        GPIO-19    Header-35  ")
print("Closed u-switch      GPIO-26    Header-37  ")
print("Torque u-switch      GPIO-20    Header-38  ")
print("Latch disable sw     GPIO-21    Header-40  ")
while True:
    btn_open.when_pressed = Flash_LED
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
