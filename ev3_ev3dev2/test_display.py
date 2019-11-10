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
from PIL import Image


def test():
    print("start",file=sys.stderr)
    display = Display()
    display.draw.rectangle((10,10,80,50), fill='black')
    #display.draw.bitmap((0,0),im)

    #显示图片
    display.image.paste(Image.open('resources/2019-11-10_00126.png'),(0,0))
    display.update()

    sleep(5)
    print("end",file=sys.stderr)


    


