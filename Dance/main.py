#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from ColorShow import ColorShow

# Hyperparameters
wheel_diameter = 56
axle_track = 114

# Initialize Light Show
colorshow = ColorShow()

# Initialize Motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor,
                  right_motor, 
                  wheel_diameter, 
                  axle_track)

#Cha Cha
def ChaCha(iters = 1,
           dir = 'forward',
           big_step_speed = 1e8,
           small_step_speed = 1e8,
           big_step_time = 1717/4,
           small_step_time = 1717/6):

    if dir != 'forward':
        big_step_speed = -big_step_speed
        small_step_speed = -small_step_speed
    
    for i in range(iters):
        left_motor.run_time(big_step_speed, big_step_time) # Big Step

        right_motor.run_time(small_step_speed, small_step_time) # ChaCha Steps
        left_motor.run_time(small_step_speed, small_step_time)

        right_motor.run_time(big_step_speed, big_step_time) # Big Step

        right_motor.run_time(small_step_speed, small_step_time) # ChaCha Steps
        left_motor.run_time(small_step_speed, small_step_time)

        # Symetric Sequence
        right_motor.run_time(big_step_speed, big_step_time)

        left_motor.run_time(small_step_speed, small_step_time)
        right_motor.run_time(small_step_speed, small_step_time)

        left_motor.run_time(big_step_speed, big_step_time)

        left_motor.run_time(small_step_speed, small_step_time)
        right_motor.run_time(small_step_speed, small_step_time)

def TurnAround(dir = 'cw',        # clockwise (cw) or counterclockwise (ccw)
               speed = 0,
               dps =  2*(180/1.717), # [deg per sec]
               time = 1717/2):      # [ms]
    if dir == 'cw':
        robot.drive_time(speed, dps, time)
    elif dir == 'ccw':
        robot.drive_time(speed, -dps, time)
    else:
        print("Must give vaild turn around direction")

def NewColor():
    colorshow.get_next_color()
    brick.light(colorshow.color_number)

def WaitForButton():
    print("Please unplug the EV3 then press any button to continue.")
    while not any(brick.buttons()):
        NewColor()
        wait(100)

    while any(brick.buttons()):
        wait(10)




WaitForButton()
time = StopWatch()

ChaCha()
NewColor()

ChaCha(dir = 'backward')
NewColor()

TurnAround()
NewColor()

ChaCha(dir = 'backward')
NewColor()

ChaCha()
NewColor()

TurnAround(time = 2*1717)
NewColor()

TurnAround(dir= 'ccw',
           time = 2*1717)
NewColor()

print(time.time())

