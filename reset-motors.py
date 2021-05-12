from ev3dev.ev3 import *


motor_linefeed = LargeMotor("outB")
motor_print_head = LargeMotor("outC")
motor_pen = MediumMotor("outD")


motor_linefeed.reset()
motor_print_head.reset()
motor_pen.reset()
