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
init_controller.LED10.off()

# ***********  Section 2 ************************************
# ***********  Identify Transistors, Relays, Armatures  *****
if section=2:
    del_time=1.5
    init_controller.T2.toggle()
    init_controller.LED10.toggle()
    time.sleep(del_time)
    while True:
        init_controller.T2.toggle()
        init_controller.T3.toggle()
        init_controller.LED10.toggle()
        time.sleep(del_time)
        init_controller.T3.toggle()
        init_controller.T4.toggle()
        init_controller.LED10.toggle()
        time.sleep(del_time)
        init_controller.T4.toggle()
        init_controller.T5.toggle()
        init_controller.LED10.toggle()
        time.sleep(del_time)
        init_controller.T5.toggle()
        init_controller.T2.toggle()
        init_controller.LED10.toggle()
        time.sleep(del_time)
  
# ***********  Section 3 ************************************
# ***********  Make Motor Turn  *****************************
if section=3:
    del_time=1.5
    while True:
        init_controller.LED10.toggle()
        #init_controller.Tw.toggle()
        #init_controller.Tx.toggle()
        time.sleep(del_time)

# ***********  Section 4 ************************************
# ***********  Make Motor Toggle  ***************************
if section=4:
    del_time=1.5
    switch_time=0.2
    while True:
        #init_controller.Ty.off()
        #init_controller.Tz.off()
        time.sleep(switch_time)
        init_controller.LED10.on()
        #init_controller.Tw.on()
        #init_controller.Tx.on()
        time.sleep(del_time)
        #init_controller.LED10.off
        #init_controller.Tw.off()
        #init_controller.Tx.off()
        time.sleep(switch_time)
        #init_controller.Ty.on()
        #init_controller.Tz.on()
        time.sleep(del_time)

# ***********  Section 5 ************************************
# ***********  Control Motor with Inputs  *******************
if section=5:
    switch_time=0.2
    #Starting condition (from Sec-1), all transistors OFF
    while True:
        direction="NONE"
        print("NO buttons pressed, stopping motor", end="")
        #wait for OPEN input
        while init_controller.CMD_open.is_pressed:
            if direction!="FWD":
                #init_controller.Ty.off()
                #init_controller.Tz.off()
                time.sleep(switch_time)
                #init_controller.Tw.on()
                #init_controller.Tx.on()
            direction="FWD"
            print("Button OPEN is pressed, Motor turning FWD")
        #wait for CLOSE input
        while init_controller.CMD_close.is_pressed:
            if direction!="REV":
                #init_controller.Tw.off()
                #init_controller.Tx.off()
                time.sleep(switch_time)
                #init_controller.Ty.on()
                #init_controller.Tz.on()
            direction="REV"
            print("Button CLOSE is pressed, Motor turning REV")
