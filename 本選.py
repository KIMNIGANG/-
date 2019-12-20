#!/usr/bin/env python3
import sys, os, time, math
from ev3dev2.led import Leds
from ev3dev2.button import Button
from ev3dev2.sensor.lego import GyroSensor, ColorSensor, UltrasonicSensor
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sound import Sound
import sys, os, time
from sys import stderr
from threading import Thread
from ev3dev2.display import Display
from ev3dev2.motor import Motor, SpeedNativeUnits

speed = 675 #670
backspeed = 550 #620
sbackspeed = 500
sspeed = 550    #380
fspeed = 77 #75
fturnspeed = 105    #100
sturnspeed = 40     #40
fullturnspeed = 130
offset = 150
car_width = 135
wheel_size = 56
mySound=Sound()
motor_pair = MoveTank(OUTPUT_C, OUTPUT_B)   #port changed
ml = LargeMotor('outC'); ml.stop_action = 'brake'   
mr = LargeMotor('outB'); mr.stop_action = 'brake'  
hand = MediumMotor(OUTPUT_A)
myBtn = Button()
cl = ColorSensor()
cl.mode = "COL-COLOR"
us = UltrasonicSensor()
us.mode='US-DIST-CM'
gy = GyroSensor()
gy.mode = 'GYRO-RATE'
gy.mode = 'GYRO-ANG'

deg1 = 0
R = 0
list1 = [0, 1, 2]

deg2 = 0
L = 0
list2 = [0, 1, 2]

deg3 = 0
work1degree = 0
countR = 0
R1 = 0
list3 = [0, 1, 2, 3, 4, 5]
degcountR = 0

deg13 = 0
countR2 = 0
work2degree = 0
R2 = 0
list13 = [0, 1, 2, 3, 4, 5]
degcount1R = 0

deg4 = 0
countL = 0
L1 = 0
list4 = [0, 1, 2, 3, 4, 5]
degcountL = 0

deg14 = 0
countL2 = 0
L2 = 0
list14 = [0, 1, 2, 3, 4, 5]
degcount1L = 0

x = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0 
l = 0   
m = 0   
n = 0   
o = 0   
p = 0
q = 0  
H = 0
CR = 0
CL = 0

def forward(mm):
    degree = (360 * mm) / (math.pi * wheel_size)
    ml.run_to_rel_pos(position_sp= degree, speed_sp = speed)
    mr.run_to_rel_pos(position_sp= degree, speed_sp = speed)

def backward(mm):
    degree = (360 * mm) / (math.pi * wheel_size)
    ml.run_to_rel_pos(position_sp= degree, speed_sp = -backspeed)
    mr.run_to_rel_pos(position_sp= degree, speed_sp = -backspeed)

def sforward(mm):
    degree = (360 * mm) / (math.pi * wheel_size)
    ml.run_to_rel_pos(position_sp= degree, speed_sp = sspeed)
    mr.run_to_rel_pos(position_sp= degree, speed_sp = sspeed)

def keepforward():
    ml.run_forever(speed_sp = speed)
    mr.run_forever(speed_sp = speed)

def skeepforward():
    ml.run_forever(speed_sp = sspeed)
    mr.run_forever(speed_sp = sspeed)

def keepbackward():
    ml.run_forever(speed_sp = -sbackspeed)
    mr.run_forever(speed_sp = -sbackspeed)

def skeepbackward():
    ml.run_forever(speed_sp = -sbackspeed)
    mr.run_forever(speed_sp = -sbackspeed)

def turn(angle):
    pivot = gy.value()
    if angle > 0:
        while pivot + angle >= gy.value():
            ml.run_forever(speed_sp = fspeed)
            mr.run_forever(speed_sp = -fspeed)
    else:
        while pivot + angle <= gy.value():
            ml.run_forever(speed_sp = -fspeed)
            mr.run_forever(speed_sp = fspeed)
    ml.stop()
    mr.stop()

def fturn(angle):
    pivot = gy.value()
    if angle > 0:
        while pivot + angle >= gy.value():
            ml.run_forever(speed_sp = fturnspeed)
            mr.run_forever(speed_sp = -fturnspeed)
    else:
        while pivot + angle <= gy.value():
            ml.run_forever(speed_sp = -fturnspeed)
            mr.run_forever(speed_sp = fturnspeed)
    ml.stop()
    mr.stop()

def sturn(angle):
    pivot = gy.value()
    if angle > 0:
        while pivot + angle >= gy.value():
            ml.run_forever(speed_sp = sturnspeed)
            mr.run_forever(speed_sp = -sturnspeed)
    else:
        while pivot + angle <= gy.value():
            ml.run_forever(speed_sp = -sturnspeed)
            mr.run_forever(speed_sp = sturnspeed)
    ml.stop()
    mr.stop()

def serveturn(angle):
    pivot = gy.value()
    if angle > 0:
        while pivot + angle >= gy.value():
            ml.run_forever(speed_sp = 10)
            mr.run_forever(speed_sp = -10)
    else:
        while pivot + angle <= gy.value():
            ml.run_forever(speed_sp = -10)
            mr.run_forever(speed_sp = 10)
    ml.stop()
    mr.stop()

def fullturn(angle):
    pivot = gy.value()
    if angle > 0:
        while pivot + angle >= gy.value():
            ml.run_forever(speed_sp = fullturnspeed)
            mr.run_forever(speed_sp = -fullturnspeed)
    else:
        while pivot + angle <= gy.value():
            ml.run_forever(speed_sp = -fullturnspeed)
            mr.run_forever(speed_sp = fullturnspeed)
    ml.stop()
    mr.stop()

def handopen():
    hand.on_for_seconds(speed=100, seconds=0.72, brake=True, block=True)
def handclose():
    hand.on_for_seconds(speed=-100, seconds=0.72, brake=True, block=True)
                
            
mySound.play_tone(440, 0.1, delay=0.0, volume=100, play_type=0 )

handclose()
time.sleep(0.1)

result = myBtn.wait_for_pressed("up")

while x == 0:   #work1
    if cl.value() == 5: 
        sforward(100)
        handopen()
        ml.wait_while('running')
        mr.wait_while('running')
        serveturn(0.0001)
        #time.sleep(0.25)
        x = 1
        break
    elif us.value() < 80 or us.value() > 2000:
        if H == 0:
            handclose()
            keepforward()
            H = 1
        elif H == 1:
            keepforward()
    elif us.value() > 80 or us.value() < 2000:
        if i == 0:
            keepforward()
            handopen()
            i = 1
        elif i == 1:
            keepforward()

while x == 1:   
    if cl.value() != 4:
        keepbackward()
    else: 
        forward(-40)
        x = 2
        break
    
while x == 2:   #work2
        if a == 0:
            fturn(23)
            ml.wait_while('running')
            mr.wait_while('running')
            motor_pair.stop()
            a = 1
        elif deg1 == 2:
            forward(150) #120
            sforward(40)
            handopen()
            time.sleep(0.25)
            ml.wait_while('running')
            mr.wait_while('running')
            x = 3
            break
        while a == 1:
            while deg1 == 0:
                if us.value() < list1[-3] -3 and us.value() < 760:  #-5
                    sturn(3)    #4
                    motor_pair.stop
                    time.sleep(0.25)
                    global deg1
                    deg1 = 1
                    break
                else:
                    sturn(1)
                    ml.wait_while('running')
                    mr.wait_while('running')
                    if us.value() < 760:
                        list1.append(us.value())
            while deg1 == 1:
                if us.value() > 40 and us.value() <2500:
                    keepforward()
                    if cl.value() == 5:
                        deg1 = 2
                        a += 1
                        break
                elif us.value() <= 40:
                    if cl.value() == 5:
                        deg1 = 2
                        a += 1
                        break
                    elif R == 0:
                        handclose()
                        sforward(20)
                        ml.wait_while('running')
                        mr.wait_while('running')
                        turn(-55.9)  #56
                        ml.wait_while('running')
                        mr.wait_while('running')
                        time.sleep(0.25)
                        global R
                        R = 1
                    elif R == 1:
                        keepforward()
                elif us.value() >= 2500:
                    keepforward()
                    if cl.value() == 5:
                        deg1 = 2
                        a += 1
                        break 

while x == 3:
    if cl.value() == 4:
        sforward(-30)
        motor_pair.stop
        x = 4
        break
    else:
        if b == 0:
            sforward(-30)
            ml.wait_while('running')
            mr.wait_while('running')
            sturn(15.3)   #14.5
            ml.wait_while('running')
            mr.wait_while('running')
            time.sleep(0.25)
            b = 1
        elif b == 1:
            keepbackward()

while x == 4: #work3
    if d == 0:
        fturn(-23)
        ml.wait_while('running')
        mr.wait_while('running')
        motor_pair.stop()
        d = 1
    elif deg2 == 2:
        forward(150)
        sforward(40)
        handopen()
        time.sleep(0.25)
        ml.wait_while('running')
        mr.wait_while('running')
        motor_pair.stop
        x = 5
        break
    while d == 1:
        while deg2 == 0:
            if us.value() < list2[-3] -3 and us.value() < 760:
                sturn(-3)
                motor_pair.stop()
                time.sleep(0.25)
                global deg2
                deg2 = 1
                break
            else:
                sturn(-1)
                ml.wait_while('running')
                mr.wait_while('running')
                if us.value() < 760:
                    list2.append(us.value())
        while deg2 == 1:
            if us.value() > 40 and us.value() <1000:
                keepforward()
                if cl.value() == 5:
                    deg2 = 2
                    d += 1
                    break
            elif us.value() <= 40:
                if cl.value() == 5:
                    deg2 = 2
                    d += 1
                    break
                elif L == 0:
                    handclose()
                    sforward(20)
                    ml.wait_while('running')
                    mr.wait_while('running')
                    turn(57.45)
                    ml.wait_while('running')
                    mr.wait_while('running')
                    time.sleep(0.25)
                    global L
                    L = 1
                elif L == 1:
                    keepforward()
            elif us.value() >= 2500:
                keepforward()
                if cl.value() == 5:
                    deg2 = 2
                    d += 1
                    break

while x == 5:
    if f == 0:
        sforward(-35)
        ml.wait_while('running')
        mr.wait_while('running')
        turn(13.5)    #16
        ml.wait_while('running')
        mr.wait_while('running')
        time.sleep(0.25)
        f = 1
    elif f == 1:
        backward(-440)  #540
        ml.wait_while('running')
        mr.wait_while('running')
        time.sleep(0.25)
        fturn(-150) #152
        ml.wait_while('running')
        mr.wait_while('running')
        time.sleep(0.25)
        degcountR = gy.value()
        x = 6
        break

#############final##########

while x == 6:   #work4
    if deg3 == 2:
        forward(220)    #150
        sforward(50)
        handopen()
        ml.wait_while('running')
        mr.wait_while('running')
        x = 7
        break
    while deg3 == 0:
        if us.value() < list3[-3] -9 and us.value() < 1050 and countR < 25:     #-4
            sturn(-1.5) #5
            ml.wait_while('running')
            mr.wait_while('running')
            countR = gy.value() - degcountR
            global deg3
            deg3 = 1
            break
        elif us.value() < list3[-6] -20 and us.value() < 1050 and countR > 25:
            sturn(-2) #2.7
            ml.wait_while('running')
            mr.wait_while('running')
            countR = gy.value() - degcountR
            global deg3
            deg3 = 1
            break        
        else:
            sturn(-1.2) #1.5
            ml.wait_while('running')
            mr.wait_while('running')
            if us.value() < 1050:    #1000
                list3.append(us.value())
            time.sleep(0.16)
    while deg3 == 1:
        if us.value() > 40 and us.value() <1600:
            keepforward()
            if cl.value() == 1 and R1 == 0:
                fullturn(193 - 0.64732*countR)
                time.sleep(0.25)
                global R1
                R1 = 1                  
            elif cl.value() == 5 and R1 == 1: 
                deg3 = 2
                break
        elif us.value() <= 40 or us.value() >= 2500:
            if cl.value() == 1 and R1 == 0:
                fullturn(193 - 0.64732*countR)
                time.sleep(0.25)
                global R1
                R1 = 1            
            elif cl.value() == 5 and R1 == 1:
                deg3 = 2
                break
            elif R1 == 0 and us.value() <= 40:
                handclose()
                sforward(10)
                ml.wait_while('running')
                mr.wait_while('running')
                fullturn(-193 - 0.64732*countR)    #193 - 0.6467
                time.sleep(0.25)
                global R1
                R1 = 1
            elif R1 == 1:
                keepforward()

while x == 7:
    sforward(-35)
    time.sleep(0.25)
    work1degree = gy.value() + 360
    fturn(- work1degree - 41)    #31 cal:31
    ml.wait_while('running')
    mr.wait_while('running')
    time.sleep(0.25)
    backward(-500)      #550
    ml.wait_while('running')
    mr.wait_while('running')
    time.sleep(0.25)
    fturn(150)   #155
    ml.wait_while('running')
    mr.wait_while('running')
    time.sleep(0.25)
    degcountL = gy.value()
    x = 8

while x == 8:   #work5
    while deg4 == 2:
        forward(30)
        sforward(20)
        handopen()      #real X      
        ml.wait_while('running')
        mr.wait_while('running')
        time.sleep(0.25)
        x = 9
        break
    while deg4 == 0:
        if us.value() < list4[-3] -9 and us.value() < 1050 and countL < 25:
            sturn(2.5)
            ml.wait_while('running')
            mr.wait_while('running')
            countL = gy.value() - degcountL
            global deg4
            deg4 = 1
            break
        elif countL > 140:
            motor_pair.stop()
            x = 100
            sys.exit(0)
        elif us.value() < list14[-6] -20 and us.value() < 1050 and countL > 25:   #8
            sturn(3) #2.7
            ml.wait_while('running')
            mr.wait_while('running')
            countL = gy.value() - degcountL
            global deg3
            deg3 = 1
            break
        else:
            sturn(1.2) 
            ml.wait_while('running')
            mr.wait_while('running')  
            if us.value() < 1050:
                list4.append(us.value())
            time.sleep(0.16) 
    while deg4 == 1:
        if us.value() > 40 and us.value() <1600:
            keepforward()
            if cl.value() == 1 and L1 == 0:
                fullturn(193 - 0.64732*countL)
                time.sleep(0.25)
                global L1
                L1 = 1            
            elif cl.value() == 2 and L1 == 1:
                deg4 = 2
                break
        elif us.value() <= 40 or us.value() >= 2500:
            if cl.value() == 1 and L1 == 0:
                fullturn(193 - 0.64732*countL)
                time.sleep(0.25)
                global L1
                L1 = 1
            elif cl.value() == 2 and L1 == 1:    
                deg4 = 2
                break
            elif L1 == 0 and us.value() <= 40:
                handclose()
                sforward(10)
                ml.wait_while('running')
                mr.wait_while('running')
                fullturn(193 - 0.64732*countL)
                time.sleep(0.25)
                global L1
                L1 = 1
            elif L1 == 1:
                keepforward()

while x == 9:   #finish
    ml.run_forever(speed_sp = 0)
    mr.run_forever(speed_sp = 0)  
    motor_pair.stop()
    sys.exit(0)
    x = 100
    break


