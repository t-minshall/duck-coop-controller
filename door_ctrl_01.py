def initialize():
    from gpiozero import LED
    from gpiozero import Button
    import time
    LED10=LED(18)  # General purpose annunciator (blue)
    T5=LED(23)   # Motor x y (red)
    T4=LED(27)   # Motor x y (red)
    T3=LED(22)   # Motor x y (red)
    T2=LED(17)   # Motor x y (red)
    #T1=LED(25)   # Buzzer (greeen)
    Buzzer=LED(25) # Buzzer (green)
    #T6=LED(7)    # Hard Latch (green)  ******* GPIO-7 seems broken on my Pi ... re-routing to GPIO-12
    T6=LED(12)    # Hard Latch (green)
    T7=LED(8)    # Soft Latch (green)
    CMD_latch=Button(21, bounce_time=0.05)
    CMD_open=Button(5, bounce_time=0.05)
    CMD_close=Button(6, bounce_time=0.05)
    CMD_stop=Button(13, bounce_time=0.05)
    SW_open=Button(19, bounce_time=0.05)
    SW_closed=Button(26, bounce_time=0.05)
    SW_torque=Button(20, bounce_time=0.05)
    jog_delay=0.25                                #    Time when motor can be force-driven under over-torque condition
    open_time=10                                  #    Time it should take to fully open the door
    close_sns_time=1                              #    Time it should take to toggle the open-sensor from a normal-closed state
    close_time=10                                 #    Time it should take to fully close the door
    open_sns_time=1                               #    Time it should take to toggle the open-sensor from a normal-open state
    armature-debounce=0.2                        #    Time delay before energizing motor armature relays (prevent shorting)
    
def stop_all():
    T2.off()
    T3.off()
    T4.off()
    T5.off()

def winch_in():
    T4.off()
    T5.off()
    time.sleep(armature_debounce)
    T2.on()
    T3.on()

def winch_out():
    T2.off()
    T3.off()
    time.sleep(armature_debounce)
    T4.on()
    T5.on()

initialize()
stop_all()
jog_timer=time.time()+jog_delay
Motion_type="NULL"
while True:
    if SW_torque.is_pressed:
        Buzzer.on()
        if time.time()>jog_timer:                        # allow program to be force-jogged out of an over-torque position
            jog_timer=time.time()+(2*jog_delay)
            stop_all()
            Motion_type="ERROR"
            time.sleep(jog_delay)
    else:
        Buzzer.off()

    if CMD_open.is_pressed and <SW_closed.is_pressed:    # this is a normal open-op
        open_timer=time.time()+open_time
        switch_timer=time.time()+close_sns_time
        Motion_type="AUTO"
        winch_in()

    if switch_timer>time.time() and Motion_type="AUTO":    #    door failed to clear the open/closed sensors quickly enough
        stop_all()
        Motion_type="ERROR"
        Buzzer.on()
    
    if (open_timer>time.time() or close_timer>time.time()) and Motion_type="AUTO":    #    door failed to complete open- or close-motion before time-out
        stop_all()
        Motion_type="ERROR"
        Buzzer.on()
    
    
