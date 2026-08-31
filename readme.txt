--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 0:  Starting a Do-over  ------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
1) open Pi Imager, make new SD card per section-3 below (Creating the R-Pi Disk)
2) insert SD card, power pi, be patient ... takes 5 min or longer for initial boot-up.
3) open Pi-Connect, connect to a new shell (DOS window)
4) Update & Install Git per section below (Install Git-Hub on Pi)
5) Get background blinker (GPIO-16) running per section below (Make program that auto-starts on boot up)

--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 1:  Get Python running on laptop, run emulation program  ---------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
To get Python running on laptop, open a DOS-window in this directory, then type 
    'PY DOOR_LIFT.PY'      (or whatever other program you wish to run. DOS is NOT case sensitive, so upper-case was done just for emphasis.)
    
To get Python running on a Raspberry ...
IDK

--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 2:  Board Build / Debug Plan  ------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
Steps:
1) Build program to blink a LED on GPIO-18 [blink18.py or blink16-always.py using spare]
2) Test program on breadboard.
3) Build PCB to include power-supply (7805 & Caps), LED-10 & interconnect-header.  Verify 5/12 volts exist where expected
4) Connect Pi, verify Python can blink LED.
5) Add X1 connector, jump pins 3-4, verify 12V exists where expected (V-ctrl). Add LED-8 & verify it runs when X1-3 & 4 are jumpered.
6) Up. Test both 18/23 on breadboard. see program blink-18-23.py
6) Add T5 & components to drive 1 leg of H-bridge (board only, no relay). Test to ensure PY can control T5's LED.
7) Add relay, verify PCB/PY can blink one relay correctly.
8) Build PY program to "blink" the full H-bridge and LED-10 together (about 2 seconds in one direction, then 2 seconds in reverse).
9) Add balance of H-bridge relays, find a dummy 12V-dc motor, and verify system can spin motor forwards/backwards.
10) Test H-bridge blinker on real hoist (set door mid-travel first). Make sure there's a way to easily cut power.
11) write PY program to read various inputs & display status on LED-10 (OK to require recompile for each input). Ensure we can read 3-button controller, limit/torque switches ... 6 inputs in total. Extra credit if PY can read input, then blink "X" number of times, depending on which input it was.
12) write PY program to read 3-button controller & blink LED-10 at 3 different speeds, depending on which button is pressed (off if none).
13 Complete board build
14) Write PY to control latch based on 3-button input (up=hard-latch, down=soft-latch).
15) Write PY to control winch & latch, test, implement

--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 3:  Create the R-Pi Disk  ----------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
Creating the R-Pi Disk // Creating an Image of the OS on an SD card:
1) open Raspberry Pi Imager
2) put SD card into computer slot (dismiss any Dropbox prompts, note drive letter)
2) select correct Pi (pi zero W)
3) select OS (PI OS Other, Pi OS Lite)
4) select drive, making sure it's what you saw when SD card inserted
5) provide computer-name for Pi (duckie-01)
6) Ensure city/timezone/keyboard selections are correct
7) Provide username & password (duckie, quack)
8) provide SSID & password for home network
9) enable SSH, select using password authentication
10) enable raspberry pi connect. press "open pi connect" button, then selet "create auth key and launch imager.
11) select "open rpi imager callback relay EXE"
12) change window back to Imager, verify a code exists in the authentication token box, then hit "Next"
13) Select "Write" to write a blank OS image to the SD card

--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 4:  Opening a Shell, interacting w/ the R-Pi  --------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
Interacting with the R-pi once an image is created: getting a shell to open
1) remove SD card from computer (assuming it was just written per the section above)
2) insert SD card into R-pi, then power the PI.  Wait ~5 minutes until system fully booted.
3) open router home-page, look at connected devices, keep refreshing until "duckie" appears. Note: it may be necessary to refresh the R-pi connect chrome page ... not sure.
4) Go back to "connect" window in Chrome (https://connect.raspberrypi.com/devices), select the "connect" button for the R-pi

--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 5:  Build/Run a simple program  ----------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
Create simple program to blink a LED on GPIO-18
1) with the R-pi connected per above, in the shell-screen, type the following
    sudo nano blink18.py (this opens the nano text editor, editing the Python file blink18.py)
    {enter password if req'd: quack}
    from gpiozero import LED
    import time
    led=LED(18)
    for _ in range(15):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    <Ctrl-S> <Ctrl-X>
2) put LED/resistor between pins 9 & 12 (Gnd & GPIO-18)
3) type "python blink18.py", observed LED blinks 15 times
    
--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 6:  Make a program that runs forever  ----------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
Make program that runs forever
1) type "sudo nano blink16-always.py"
    {enter password if req'd: quack}
    from gpiozero import LED
    import time
    led=LED(16)
    #while True:
    #    led.on()
    #    time.sleep(0.5)
    #    led.off()
    #    time.sleep(0.5)
    while True:
        for _ in range(3):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.2)
        time.sleep(0.8)
    <Ctrl-S> <Ctrl-X>
2) put LED/resistor between pins 9 & 36 (Gnd & GPIO-16)
3) type "python blink16-always.py", observed LED blinks and never stops.
4) press <Ctrl-C> to exit

--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 7:  Make a program that starts on boot-up  -----------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
Make program that auto-starts on boot-up
1) get a program working. In this case, use blink16-always.py, from above
2) type "sudo crontab -e", then enter the line below ... (enter password "quack" if needed) (select option-1 to use nano, if needed)
3) down-arrow to the bottom of the page, add the line
@reboot python /home/duckie/duck-coop-controller/blink16-always.py &
<Ctrl-S> <Ctrl-X>

--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 8:  Instal Git-Hub on Pi, Clone a Repository  --------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
Install Git-Hub on Pi, clone files from repository.  
Video Source:  https://www.youtube.com/watch?v=9CULlsc5BBU
Instructions:  Open shell, type:
    sudo apt update (enter password "quack" if needed)
    {sudo apt upgrade} (
                        this wasn't in initial source-instructions, but probably best if done ... 
                        Update fetches list of sw packages
                        Upgrade actually installs them    
                        )
    sudo apt install git -y
    git clone https://github.com/t-minshall/duck-coop-controller
To update Pi-local files, from the clone-directory, type
    git pull


--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 9:  Flash LED's based on GPIO inputs  ---------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
#Write program to read inputs & flash LED appropriately based on which input is detected
#Tutorial source:  gpiozero docs page (https://gpiozero.readthedocs.io/en/stable/recipes.html)
#Read input, flash light
from gpiozero import LED, Button
import time

#Define sub-routines
def Flash_LED():
    print("Button detected")
    
#Define all IO ports
led=LED(18)
buzzer=LED(25)
btn_open=Button(5)
btn_close=Button(6)
btn_stop=Button(13)
sw_open=Button(19)
sw_close=Button(26)
sw_torque=Button(20)
sw_latch=Button(21)
H_PL=LED(17)
H_PR=LED(27)
H_NL=LED(22)
H_NR=LED(23)

#main program
btn_open.when_pressed = Flash_LED
btn_close.when_pressed = Flash_LED
btn_stop.when_pressed = Flash_LED
sw_open.when_pressed = Flash_LED
sw_close.when_pressed = Flash_LED
sw_torque.when_pressed = Flash_LED
sw_latch.when_pressed = Flash_LED

#hang program, let "when_pressed" interrupts execute
#not sure how to debounce
#not sure how to prevent alternate inputs from interfering
#not sure how to pass an argument to "Flash_LED" so it can be more uniquely responsive
pause()



--------------------------------------------------------------------------------------------------------------------------
--------------- Sec 10:  Write a batch-type script  ----------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
Create a batch-type script
from shell window, create text-file (with .sh extension) ... eg
    sudo nano dc.sh
    enter appropriate command-line commands ... eg
        cd ./duck-coop-controller
        pwd
        ls
    make it executable ... type
        chmod +x dc.sh
    run the script/batch-file, preceeding the file-name with ". " (to "source" the script)
        . dc.sh (or type "source dc.sh")
