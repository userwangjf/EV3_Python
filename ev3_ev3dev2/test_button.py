#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import ev3dev2 lib
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from ev3dev2.button import Button
from ev3dev2.console import Console
import ev3dev2.fonts as fonts

# import python stand lib
import queue
import threading
import time
from time import sleep
import sys


console = Console(font='Lat15-TerminusBold20x10')
#Console.set_font(font='Lat15-TerminusBold24x12', reset_console=True)
#打印到LCD
print('start test:')


#按键
button = Button()

print('please press enter')
print(button.buttons_pressed,file=sys.stderr)
button.wait_for_pressed('enter',timeout_ms=10000)
print(button.buttons_pressed,file=sys.stderr)

def key_enter(new_state):
    print(new_state)
    print('press enter',file=sys.stderr)

button.on_enter = key_enter

while True:
    if button.right:
        print("press right",file=sys.stderr)
    button.process()


