#!/usr/bin/env python3
from ev3dev2.led import Leds
from ev3dev2.button import Button
from ev3dev2.sensor.lego import GyroSensor, TouchSensor, ColorSensor, UltrasonicSensor
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.motor import Motor, SpeedNativeUnits
from ev3dev2.sound import Sound
import sys, os, time
from threading import Thread
from ev3dev2.display import Display

us = UltrasonicSensor()
mySound=Sound()
motor_pair = MoveTank(OUTPUT_C, OUTPUT_B)
hand = MediumMotor(OUTPUT_A)


mySound.play_tone(440, 0.1, delay=0.0, volume=100, play_type=0 ) #testsound

hand.on_for_seconds(speed=-80, seconds=0.2, brake=True, block=True)
time.sleep(0.5)
