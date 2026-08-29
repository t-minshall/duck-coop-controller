
#Write program to read inputs & flash LED appropriately based on which input is detected
#Tutorial source:  gpiozero docs page (https://gpiozero.readthedocs.io/en/stable/recipes.html)
#Read input, flash light
import time
from gpiozero import LED
from gpiozero import Button

#Define sub-routines
def Flash_LED_open_cmd():
    print("Button detected: open-command")
    for _ in range(1):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    
def Flash_LED_close_cmd():
    print("Button detected: close-command")
    for _ in range(2):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    
def Flash_LED_stop_cmd():
    print("Button detected: stop-command")
    for _ in range(3):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    
def Flash_LED_open_sw():
    print("Button detected: open limit-switch")
    for _ in range(4):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    
def Flash_LED_closed_sw():
    print("Button detected: closed limit-switch")
    for _ in range(5):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    
def Flash_LED_torque_sw():
    print("Button detected: over-torque limit-switch")
    for _ in range(6):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    
def Flash_LED_latch_sw():
    print("Button detected: latch overide switch")
    for _ in range(7):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)

def announce_input(code,button_name):
    print(f"Button {code} pressed: {button_name}")
    for _ in range(code):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)

#Define all IO ports
led=LED(18)
buzzer=LED(25)
btn_open=Button(5, bounce_time=0.2)
btn_close=Button(6, bounce_time=0.2)
btn_stop=Button(13, bounce_time=0.2)
sw_open=Button(19, bounce_time=0.2)
sw_close=Button(26, bounce_time=0.2)
sw_torque=Button(20, bounce_time=0.2)
sw_latch=Button(21, bounce_time=0.2)
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
    while btn_open.is_pressed:
        announce_input(1,"Open Command")
    while sw_torque.is_pressed:
        announce_input(6, "Over-torque switch")
    while sw_latch.is_pressed:
        announce_input(7, "Latch overide switch")
                           
        
#    btn_open.when_pressed = Flash_LED_open_cmd
#    btn_close.when_pressed = Flash_LED_close_cmd
#    btn_stop.when_pressed = Flash_LED_stop_cmd
#    sw_open.when_pressed = Flash_LED_open_sw
#    sw_close.when_pressed = Flash_LED_closed_sw
#    sw_torque.when_pressed = Flash_LED_torque_sw
#    sw_latch.when_pressed = Flash_LED_latch_sw

#hang program, let "when_pressed" interrupts execute
#not sure how to debounce
#not sure how to prevent alternate inputs from interfering
#not sure how to pass an argument to "Flash_LED" so it can be more uniquely responsive
