#!/usr/bin/env python3
import sys, os, time, math
from ev3dev2.led import Leds
from ev3dev2.button import Button
from ev3dev2.sensor.lego import GyroSensor, TouchSensor, ColorSensor, UltrasonicSensor
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sound import Sound
import sys, os, time
from threading import Thread
from ev3dev2.display import Display
from ev3dev2.motor import Motor, SpeedNativeUnits


speed = 330
sspeed = 165
offset = 150
car_width = 113
wheel_size = 56
mySound=Sound()
motor_pair = MoveTank(OUTPUT_B, OUTPUT_C)
ml = LargeMotor('outB'); ml.stop_action = 'hold'
mr = LargeMotor('outC'); mr.stop_action = 'hold'
hand = MediumMotor(OUTPUT_A)
myBtn = Button()
cl = ColorSensor()
cl.mode = "COL-COLOR"
us = UltrasonicSensor()
us.mode='US-DIST-CM'
gy = GyroSensor()
gy.mode = 'GYRO-ANG'

x = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
A = 0
B = 0
C = 0
D = 0

def handopen():
    hand.on_for_seconds(speed=80, seconds=0.72, brake=True, block=True)
    hand.wait_while('running')

handopen()