from gpiozero import LED
from gpiozero import Button
import time
LED10=LED(18)  # General purpose annunciator (blue)
T5=LED(23)   # Motor x y (red)
T4=LED(27)   # Motor x y (red)
T3=LED(22)   # Motor x y (red)
T2=LED(17)   # Motor x y (red)
T1=LED(25)   # Buzzer (greeen)
T6=LED(7)    # Hard Latch (green
T7=LED(8)    # Soft Latch (green)
CMD_latch=Button(21, bounce_time=0.05)
CMD_open=Button(5, bounce_time=0.05)
CMD_close=Button(6, bounce_time=0.05)
CMD_stop=Button(13, bounce_time=0.05)
SW_open=Button(19, bounce_time=0.05)
SW_closed=Button(26, bounce_time=0.05)
SW_torque=Button(20, bounce_time=0.05)

def motor_stop():
  T2.off()
  T3.off()
  T4.off()
  T5.off()
  return
  
def motor_fwd():
  T2.off()
  T3.off()
  T4.off()
  T5.off()
  time.sleep(0.05)
  T2.on()
  T4.on()
  return
  
def motor_bkwd():
  T2.off()
  T3.off()
  T4.off()
  T5.off()
  time.sleep(0.05)
  T3.on()
  T5.on()
  return
  
def motor_kill():
    T2.on()
    T3.on()
    T4.on()
    T5.on()
    return

def motor_loop():
    while True: 
        motor_fwd()
        time.sleep(1)
        motor_bkwd()
        time.sleep(1)
    return


