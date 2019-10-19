#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import sys

# Write your program here
brick.sound.beep()

brick.display.clear()
brick.display.text("Hello World",(0,10))
brick.display.text("Have a nice day",(0,20))

brick.sound.file(SoundFile.HELLO)

# 等待2秒
wait(2000)

print("HelloWorld!")


print("print to screen", file=sys.stdout)
wait(2000)



