# *************  Start Controlling the H-Bridge  *************
# 1) Identify which transistor controls which relay, and which relay controls which armature-flow
#    MAKE SURE NOT TO SHORT THE RELAYS !!!!!!!!!!!
# 2) Turn on one set of armature relays (leave the others un-connected to guard against shorts
# 3) Toggle armature relays to get motor cycling fwd/rev
# 4) Make armature direction a function of which switch is pressed
#
# ***********  Section 1 ************************************
# ***********  Initialization  ******************************
import init_controller
import time
section=2

init_controller.T1.off()
init_controller.T2.off()
init_controller.T3.off()
init_controller.T4.off()
init_controller.T5.off()
init_controller.T6.off()
init_controller.T7.off()
init_controller.LED10.on()

# ***********  Section 2 ************************************
# ***********  Identify Transistors, Relays, Armatures  *****
if section=2:
    del_time=1.5
    init_controller.T2.toggle()
    time.sleep(del_time)
    while True:
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
        init_controller.T2.toggle()
        time.sleep(del_time)
  
# ***********  Section 3 ************************************
# ***********  Make Motor Turn  *****************************
if section=3:
    del_time=1.5
    while True:
        init_controller.LED10.toggle()
        #init_controller.Tx.toggle()
        #init_controller.Tx.toggle()
        time.sleep(del_time)

# ***********  Section 4 ************************************
# ***********  Make Motor Toggle  ***************************
if section=4:
    del_time=1.5
    switch_time=0.2
    while True:
        init_controller.LED10.toggle()
        #init_controller.Tx.toggle()
        #init_controller.Tx.toggle()
        time.sleep(del_time)

# ***********  Section 5 ************************************
# ***********  Control Motor with Inputs  *******************
