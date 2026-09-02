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
  init_controller.T1.on()
  init_controller.T6.off()
  init_controller.T7.off()
  time.sleep(1)
  init_controller.motor_bkwd()
  init_controller.T1.off()
  init_controller.T6.on()
  init_controller.T7.on()
  time.sleep(1)
  init_controller.LED10.toggle()
