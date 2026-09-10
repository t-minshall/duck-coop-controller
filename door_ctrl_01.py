def initialize():
    from gpiozero import LED
    from gpiozero import Button
    import time
    LED10=LED(18)  # General purpose annunciator (blue)
    T5=LED(23)   # Motor x y (red)
    T4=LED(27)   # Motor x y (red)
    T3=LED(22)   # Motor x y (red)
    T2=LED(17)   # Motor x y (red)
    T1=LED(25)   # Buzzer (greeen)
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

initialize()
var_a = 1
print("running -001")
