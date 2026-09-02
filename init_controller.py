from gpiozero import LED
import time
LED10=LED(18)
T5=LED(23)
T4=LED(27)
T3-LED(22)
T2=LED(17)
T1=LED(25)
T6=LED(7)
T7=LED(8)

def motor_stop():
  T2.off()
  T3.off()
  T4.off()
  T5.off()
  return()
  
def motor_fwd():
  T2.off()
  T3.off()
  T4.off()
  T5.off()
  time.sleep(0.05)
  T2.on()
  T4.on()
  return()
  
def motor_bkwd():
  T2.off()
  T3.off()
  T4.off()
  T5.off()
  time.sleep(0.05)
  T3.on()
  T5.on()
  return()
  
def motor_kill():
    T3.on()
    T5.on()
    T3.on()
    T5.on()
    return()
  
