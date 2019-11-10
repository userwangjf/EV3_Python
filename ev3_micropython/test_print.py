#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import ev3dev2 lib
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
#from ev3dev2.sound import Sound
from ev3dev2.display import Display
from ev3dev2.button import Button
from ev3dev2.console import Console
#import ev3dev2.fonts as fonts

# import python stand lib
import queue
import threading
import time
from time import sleep
import sys

#测试LCD控制台字体
'''
LCD Rows	LCD Columns	Font
4	11	Lat15-Terminus32x16.psf.gz
4	11	Lat15-TerminusBold32x16.psf.gz
4	11	Lat15-VGA28x16.psf.gz
4	11	Lat15-VGA32x16.psf.gz
4	12	Lat15-Terminus28x14.psf.gz
4	12	Lat15-TerminusBold28x14.psf.gz
5	14	Lat15-Terminus24x12.psf.gz
5	14	Lat15-TerminusBold24x12.psf.gz
5	16	Lat15-Terminus22x11.psf.gz
5	16	Lat15-TerminusBold22x11.psf.gz
6	17	Lat15-Terminus20x10.psf.gz
6	17	Lat15-TerminusBold20x10.psf.gz
7	22	Lat15-Fixed18.psf.gz
8	22	Lat15-Fixed15.psf.gz
8	22	Lat15-Fixed16.psf.gz
8	22	Lat15-Terminus16.psf.gz
8	22	Lat15-TerminusBold16.psf.gz
8	22	Lat15-TerminusBoldVGA16.psf.gz
8	22	Lat15-VGA16.psf.gz
9	22	Lat15-Fixed13.psf.gz
9	22	Lat15-Fixed14.psf.gz
9	22	Lat15-Terminus14.psf.gz
9	22	Lat15-TerminusBold14.psf.gz
9	22	Lat15-TerminusBoldVGA14.psf.gz
9	22	Lat15-VGA14.psf.gz
10	29	Lat15-Terminus12x6.psf.gz
16	22	Lat15-VGA8.psf.gz
21	44	Lat15-TomThumb4x6.psf.gz
'''


def test():
    #设置字体
    console = Console(font='Lat15-TerminusBold20x10')
    #Console.set_font(font='Lat15-TerminusBold24x12', reset_console=True)
    #显示到LCD屏幕
    print('start runing')
    #显示到调试器的output
    print("print to output",file=sys.stderr)
    print('Hello World 12345')
    print('0123456789ABCDEFabcdef')
    print('OK')

    sleep(3)

