import init_controller
import time
#init_controller.motor_loop

#def motor_loop():
#  while True: 
#    motor_fwd()
#    time.sleep(1)
#    motor_bkwd()
#    time.sleep(1)
#  return

init_controller.motor_stop()
while True:
  init_controller.motor_fwd()
  time.sleep(1)
  init_controller.motor_bkwd()
  time.sleep(1)
  LED10.toggle()
