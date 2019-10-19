#!/usr/bin/env python3
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

# import user lib

# TODO: Add code here


testcase='test_print'

if testcase=='test_print':
    from test_print import test

if testcase=='test_button':
    from test_button import test

#执行用例
test()
exit()

disp = Display()
leds = Leds()
sounds = Sound()
#ts = TouchSensor(INPUT_2)

sounds.beep()

sleep(1)
sounds.set_volume(100)
sounds.speak(text='1.15')
#sounds.speak(text='Welcome to the E V 3 dev project!')
sleep(1)

exit()

'''
console.reset_console()
console.text_at('Hello World!', column=1, row=5, reset_console=True, inverse=True)
sleep(2)
'''

# 在屏幕上显示字体
if True:
    #显示有效的Display字体
    print(fonts.available(),file=sys.stderr)
    sleep(2)
    exit()
disp.clear()
disp.draw.text((10,10), 'Hello World!', font=fonts.load('courB18'))
disp.update()

# 改变面板显示灯的颜色
leds.set_color("LEFT","GREEN")
leds.set_color("RIGHT","RED")

# 英文转语音
sleep(1)
sounds.speak(text='Welcome to the E V 3 dev project!')
sleep(1)

# 控制电机转动
m = LargeMotor(OUTPUT_A)
#m.on_for_rotations(SpeedPercent(75), 1)
m.on_for_degrees(50,50)
sleep(1)
m.on_for_degrees(50,-50)
sleep(1)

# 检测接触传感器，并显示不同颜色
while True:
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")


# 等待1秒
sleep(1)

print("helloworld")
