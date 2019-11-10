#!/usr/bin/env micropython
# -*- coding: utf-8 -*-

'''
#!/usr/bin/env python3
#!/usr/bin/env micropython
# -*- coding: utf-8 -*-
'''

# import ev3dev2 lib
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
#from ev3dev2.sound import Sound
#from ev3dev2.display import Display
from ev3dev2.button import Button
#from ev3dev2.console import Console
#import ev3dev2.fonts as fonts

# import python stand lib
import queue
import threading
import time
from time import sleep
import sys

# import user lib

# TODO: Add code here


testcase='test_print'

if testcase=='test_print':
    from test_print import test

if testcase=='test_button':
    from test_button import test

if testcase=='test_led':
    from test_led import test

if testcase=='test_sound':
    from test_sound import test    

#执行用例
test()

exit()

