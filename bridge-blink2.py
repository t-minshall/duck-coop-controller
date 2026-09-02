import init_controller
'init_controller.motor_loop

#def motor_loop():
#  while True: 
#    motor_fwd()
#    time.sleep(1)
#    motor_bkwd()
#    time.sleep(1)
#  return

init_controller.motor_off()
while True:
  init_controller.motor_fwd()
  time.sleep(1)
  init_controller.motor_bkwd()
  time.sleeep(1)
