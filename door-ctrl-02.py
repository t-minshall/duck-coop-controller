import init_controller
import time
import logging
from datetime import datetime
section=9

init_controller.T1.off()
init_controller.T2.off()
init_controller.T3.off()
init_controller.T4.off()
init_controller.T5.off()
init_controller.T6.off()
init_controller.T7.off()
init_controller.LED10.off()
logging.basicConfig(
    filename='/home/duckie/duck-coop-controller/door-ctrl-02.log',  # Path to your log file
    level=logging.INFO,                # Track INFO level messages and above
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
print("Section-1 (Initialization) complete")
logging.info("\c\c Starting Program")
logging.info("Section-1 (Initialization) complete")


# ***********  Section 9 ************************************
# ***********  All IO working Together  *********************
if section==9:
    print("Starting Section-9 (all IO working together)")
    logging.info("Starting Section-9 (all IO working together)")
    switch_time=0.2
    print_end="                                    \r"
    print_end="\r"
    #print_end="\r\n"
    #Starting condition (from Sec-1), all transistors OFF
    direction="NONE"
    init_controller.T2.off()
    init_controller.T3.off()
    init_controller.T4.off()
    init_controller.T5.off()
    init_controller.T6.off()
    init_controller.T7.off()
    init_controller.LED10.blink(0.2, 1.8)
    sys_state_local=init_controller.system_state()
    sys_state_old=sys_state_local
    message="NO buttons pressed, stopping motor"
    print(f"{message:<50} {sys_state_local} {direction} 0", end=print_end)
    #print(f"{message:<50} {sys_state_local}", end=print_end)
    logging.info(sys_state_local+" | "+message)
    while True:
        message="looping"
        sys_state_local=init_controller.system_state()
        print(f"{message:<50} {sys_state_local} {direction} 1", end=print_end)
        if not sys_state_local==sys_state_old:
            logging.info(sys_state_local+" | "+message)
            sys_state_old=sys_state_local
        
        while init_controller.CMD_open.is_pressed:
            if direction!="OPEN":
                init_controller.T2.off()
                init_controller.T3.off()
                init_controller.T6.off()    # Release Hard-latch
                init_controller.T7.off()    # Release Soft-latch
                time.sleep(switch_time)
                init_controller.T4.on()
                init_controller.T5.on()
                init_controller.T1.blink(0.1, 0.9)
                init_controller.LED10.blink(0.5, 0.5)
            direction="OPEN"
            sys_state_local=init_controller.system_state()
            message="Button OPEN is pressed, Motor turning FWD/OPEN"
            print(f"{message:<50} {sys_state_local} {direction} 2", end=print_end)
            if not sys_state_local==sys_state_old:
                logging.info(sys_state_local+" | "+message)
                sys_state_old=sys_state_local
            
        if direction=="OPEN" and init_controller.SW_open.is_pressed:
            # motor has moved all the way to the open position-sensor
            # stop motor, reset buzzer and LED-flasher
            init_controller.T4.off()
            init_controller.T5.off()
            init_controller.T1.off()
            init_controller.LED10.blink(0.2, 1.8)
            direction="NONE"
            #sys_state_local=init_controller.system_state()
            message="Door had fully opened, Stop Motors"
            #print("Door had fully opened, Stop Motors",end=print_end)
            print(f"{message:<50} {sys_state_local} {direction} 3", end=print_end)
            if not sys_state_local==sys_state_old:
                logging.info(sys_state_local+" | "+message)
                sys_state_old=sys_state_local
        
        while init_controller.CMD_close.is_pressed:
            if direction!="CLOSE":
                init_controller.T4.off()
                init_controller.T5.off()
                time.sleep(switch_time)
                init_controller.T2.on()
                init_controller.T3.on()
                init_controller.T1.blink(0.1, 0.9)
                init_controller.LED10.blink(0.25, 0.25)
            direction="CLOSE"
            sys_state_local=init_controller.system_state()
            message="Button CLOSE is pressed, Motor turning REV/CLOSE"
            print(f"{message:<50} {sys_state_local} {direction} 4", end=print_end)
            if not sys_state_local==sys_state_old:
                logging.info(sys_state_local+" | "+message)
                sys_state_old=sys_state_local

        if direction=="CLOSE" and init_controller.SW_closed.is_pressed:
            # motor has moved all the way to the closed position-sensor
            # stop motor, reset buzzer and LED-flasher
            #throw Latch
            init_controller.T2.off()
            init_controller.T3.off()
            init_controller.T1.off()
            init_controller.LED10.blink(0.2, 1.8)
            init_controller.T6.on()     # Hard-latch on
            time.sleep(5)               # Allow time to push door closed
            init_controller.T7.on()     # Soft-latch on
            time.sleep(0.25)            # transition delay, ensure soft-latch catches before hard-latch releases
            init_controller.T6.off()    # Hard-latch off
            direction="NONE"
            #sys_state_local=init_controller.system_state()
            message="Door had fully closed, Stop Motors, Set Latch"
            print(f"{message:<50} {sys_state_local} {direction} 5", end=print_end)
            if not sys_state_local==sys_state_old:
                logging.info(sys_state_local+" | "+message)
                sys_state_old=sys_state_locallogging.info(sys_state_local+" | "+message)
            
        while init_controller.CMD_stop.is_pressed:
            init_controller.T1.off()
            init_controller.T2.off()
            init_controller.T3.off()
            init_controller.T4.off()
            init_controller.T5.off()
            init_controller.T6.off()
            init_controller.T7.off()            ;     print("T7 off")
            init_controller.LED10.blink(0.2, 1.8)
            direction="NONE"
            sys_state_local=init_controller.system_state()
            message="Button STOP is pressed, Motor halted"
            print(f"{message:<50} {sys_state_local} {direction} 6", end=print_end)
            if not sys_state_local==sys_state_old:
                logging.info(sys_state_local+" | "+message)
                sys_state_old=sys_state_locallogging.info(sys_state_local+" | "+message)
            
        if init_controller.SW_torque.is_pressed:
            # Note: system will get hung-up here ... no way to jog-out while over-torque is sensed
            init_controller.T1.blink(0.5, 0.5)
            init_controller.T2.off()
            init_controller.T3.off()
            init_controller.T4.off()
            init_controller.T5.off()
            init_controller.T6.off()
            init_controller.T7.off()
            init_controller.LED10.blink(0.2, 0.2)
            direction="NONE"
            sys_state_local=init_controller.system_state()
            message="Over-Torque detected, Stop motors, sound alarm"
            print(f"{message:<50} {sys_state_local} {direction} 7", end=print_end)
            if not sys_state_local==sys_state_old:
                logging.error(sys_state_local+" | "+message)
                sys_state_old=sys_state_locallogging.info(sys_state_local+" | "+message)
          
