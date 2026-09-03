import init_controller
import time
del_time_init = 0.2
del_time_min=0.025
del_time_increment=0.025
del_time=del_time_init

init_controller.T1.off()
init_controller.T2.off()
init_controller.T3.off()
init_controller.T4.off()
init_controller.T5.off()
init_controller.T6.off()
init_controller.T7.off()
init_controller.LED10.on()
time.sleep(del_time)
while True:
  init_controller.LED10.toggle()
  init_controller.T2.toggle()
  time.sleep(del_time)
  init_controller.T2.toggle()
  init_controller.T3.toggle()
  time.sleep(del_time)
  init_controller.T3.toggle()
  init_controller.T4.toggle()
  time.sleep(del_time)
  init_controller.T4.toggle()
  init_controller.T5.toggle()
  time.sleep(del_time)
  init_controller.T5.toggle()
  init_controller.T6.toggle()
  time.sleep(del_time)
  init_controller.T6.toggle()
  init_controller.T7.toggle()
  time.sleep(del_time)
  init_controller.T7.toggle()
  init_controller.T1.toggle()
  time.sleep(del_time)
  init_controller.T1.toggle()
  init_controller.LED10.toggle()
  time.sleep(del_time)
  del_time=del_time - del_time_increment
  if del_time<del_time_min:
      del_time=del_time_init

