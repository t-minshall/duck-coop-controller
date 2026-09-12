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
section=7

init_controller.T1.off()
init_controller.T2.off()
init_controller.T3.off()
init_controller.T4.off()
init_controller.T5.off()
init_controller.T6.off()
init_controller.T7.off()
init_controller.LED10.off()
print("Section-1 (Initialization) complete")

# ***********  Section 2 ************************************
# ***********  Identify Transistors, Relays, Armatures  *****
if section==2:
    print("Starting Section-2 (identify TRA's)")
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
if section==3:
    print("Starting Section-3 (make motor turn)")
    del_time=1.5
    toggle_count=0
    while True:
        print("Motor-toggle", toggle_count, end="")
        init_controller.LED10.toggle()
        init_controller.T2.toggle()
        init_controller.T3.toggle()
        time.sleep(del_time)
        toggle_count += 1

# ***********  Section 4 ************************************
# ***********  Make Motor Toggle  ***************************
if section==4:
    print("Starting Section-4 (make motor toggle)")
    del_time=1.5
    switch_time=0.2
    while True:
        init_controller.T2.off()
        init_controller.T3.off()
        time.sleep(switch_time)
        init_controller.LED10.on()
        init_controller.T4.on()
        init_controller.T5.on()
        print("Motor FWD", end="")
        time.sleep(del_time)
        init_controller.LED10.off
        init_controller.T4.off()
        init_controller.T5.off()
        time.sleep(switch_time)
        init_controller.T2.on()
        init_controller.T3.on()
        print("Motor REV", end="")
        time.sleep(del_time)

# ***********  Section 5 ************************************
# ***********  Control Motor with Inputs  *******************
if section==5:
    print("Starting Section-5 (make motor respond to inputs)")
    switch_time=0.2
    #Starting condition (from Sec-1), all transistors OFF
    while True:
        direction="NONE"
        init_controller.T2.off()
        init_controller.T3.off()
        init_controller.T4.off()
        init_controller.T5.off()
        print("NO buttons pressed, stopping motor", end="\r")
        #wait for OPEN input
        while init_controller.CMD_open.is_pressed:
            if direction!="FWD":
                init_controller.T2.off()
                init_controller.T3.off()
                time.sleep(switch_time)
                init_controller.T4.on()
                init_controller.T5.on()
            direction="FWD"
            print("Button OPEN is pressed, Motor turning FWD")
        #wait for CLOSE input
        while init_controller.CMD_close.is_pressed:
            if direction!="REV":
                init_controller.T4.off()
                init_controller.T5.off()
                time.sleep(switch_time)
                init_controller.T2.on()
                init_controller.T3.on()
            direction="REV"
            print("Button CLOSE is pressed, Motor turning REV")


# ***********  Section 6 ************************************
# ***********  Control Motor with More Inputs  **************
if section==6:
    print("Starting Section-6 (motor responds to inputs, and buzzer/LED)")
    switch_time=0.2
    #Starting condition (from Sec-1), all transistors OFF
    while True:
        direction="NONE"
        init_controller.T2.off()
        init_controller.T3.off()
        init_controller.T4.off()
        init_controller.T5.off()
        print("NO buttons pressed, stopping motor", end="\r")

        while init_controller.CMD_open.is_pressed:
            if direction!="FWD":
                init_controller.T2.off()
                init_controller.T3.off()
                init_controller.T1.off()
                time.sleep(switch_time)
                init_controller.T4.on()
                init_controller.T5.on()
                init_controller.LED10.on()
            direction="FWD"
            print("Button OPEN is pressed, Motor turning FWD", end="\r")

        while init_controller.CMD_close.is_pressed:
            if direction!="REV":
                init_controller.T4.off()
                init_controller.T5.off()
                init_controller.LED10.off()
                time.sleep(switch_time)
                init_controller.T2.on()
                init_controller.T3.on()
                init_controller.T1.on()
            direction="REV"
            print("Button CLOSE is pressed, Motor turning REV", end="\r")

        while init_controller.CMD_stop.is_pressed:
            init_controller.T1.off()
            init_controller.T2.off()
            init_controller.T3.off()
            init_controller.T4.off()
            init_controller.T5.off()
            init_controller.LED10.off()
            print("Button STOP is pressed, Motor halted", end="\r")
            

# ***********  Section 7 ************************************
# ***********  Control Motor with More Inputs (w/o button-hold) **************
if section==7:
    print("Starting Section-7 (motor responds to inputs & holds, and buzzer/LED)")
    switch_time=0.2
    #Starting condition (from Sec-1), all transistors OFF
    direction="NONE"
    init_controller.T2.off()
    init_controller.T3.off()
    init_controller.T4.off()
    init_controller.T5.off()
    init_controller.LED10.blink(0.2, 1.8)
    print("NO buttons pressed, stopping motor", end="                                    \r")
    while True:
        while init_controller.CMD_open.is_pressed:
            if direction!="FWD":
                init_controller.T2.off()
                init_controller.T3.off()
                init_controller.T1.blink(0.5, 0.5)
                time.sleep(switch_time)
                init_controller.T4.on()
                init_controller.T5.on()
                init_controller.LED10.blink(0.5, 0.5)
            direction="FWD"
            print("Button OPEN is pressed, Motor turning FWD", end="                                    \r")

        while init_controller.CMD_close.is_pressed:
            if direction!="REV":
                init_controller.T4.off()
                init_controller.T5.off()
                init_controller.LED10.blink(0.25, 0.25)
                time.sleep(switch_time)
                init_controller.T2.on()
                init_controller.T3.on()
                init_controller.T1.blink(0.25, 0.25)
            direction="REV"
            print("Button CLOSE is pressed, Motor turning REV", end="                                    \r")

        while init_controller.CMD_stop.is_pressed:
            init_controller.T1.off()
            init_controller.T2.off()
            init_controller.T3.off()
            init_controller.T4.off()
            init_controller.T5.off()
            init_controller.LED10.blink(0.2, 1.8)
            direction="NONE"
            print("Button STOP is pressed, Motor halted", end="                                    \r")
            
