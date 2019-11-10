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
import random

'''
Led groups:
• LEFT
• RIGHT
Colors:
• BLACK
• RED
• GREEN
• AMBER
• ORANGE
• YELLOW
'''

def wait_btn():
    rand = random.randint(900,1100)
    button.wait_for_pressed('enter',timeout_ms=rand)

def test():

    button = Button()
    leds = Leds()
    console = Console(font='Lat15-TerminusBold20x10')

    count=0

    while True:
        leds.set_color('LEFT','BLACK')
        leds.set_color('RIGHT',"BLACK")
        sleep(1)
        leds.set_color('LEFT','GREEN')
        leds.set_color('RIGHT','GREEN')
        sleep(1)
        leds.set_color('LEFT','BLACK')
        leds.set_color('RIGHT',"BLACK")
        sleep(1)
        leds.set_color('LEFT','RED')
        leds.set_color('RIGHT','RED')
        sleep(1)
        count=count+1
        if button.enter:
            print("press enter",file=sys.stderr)
            break

    print(count)

    sleep(10)



if __name__ == '__main__':
    test()




