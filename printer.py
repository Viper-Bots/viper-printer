from ev3dev.ev3 import *
import datetime
import time
import png
import argparse

SECONDS_1 = datetime.timedelta(seconds=1)
SECONDS_3 = datetime.timedelta(seconds=3)
TIME_LIMIT = datetime.timedelta(seconds=2)


LINE_HEIGHT = 1
DOT_WIDTH = 1
PEN_DROP = 4



motor_linefeed = LargeMotor("outB")
motor_print_head = LargeMotor("outC")
motor_pen = MediumMotor("outD")

def cr():
	motor_print_head.run_to_abs_pos(position_sp=0, speed_sp=400, stop_action='hold')
	motor_print_head.wait_while('running',timeout=1000)
	time.sleep(0.2)

def left(amt=0):
	start = str(motor_print_head.position)
	motor_print_head.run_to_rel_pos(position_sp=amt*DOT_WIDTH, speed_sp=400, stop_action='hold')
	motor_print_head.wait_while('running',timeout=1000)
	time.sleep(0.2)
	finish = str(motor_print_head.position)
	dif = str( int(finish) - int(start) )
	print('start: ' + start + '\tamt: ' + str(amt*DOT_WIDTH) + '\tfinish: ' + finish + '\tdif: ' + dif )

def right(amt=0):
	start = str(motor_print_head.position)
	motor_print_head.run_to_rel_pos(position_sp=amt*DOT_WIDTH*-1, speed_sp=400, stop_action='hold')
	motor_print_head.wait_while('running',timeout=1000)
	time.sleep(0.2)
	finish = str(motor_print_head.position)
	dif = str( int(finish) - int(start) )
	print('start: ' + start + '\tamt: ' + str(amt*DOT_WIDTH*-1) + '\tfinish: ' + finish + '\tdif: ' + dif )

def forward(amt=0):
	motor_linefeed.run_to_rel_pos(position_sp=amt*LINE_HEIGHT*-1, speed_sp=400, stop_action='hold')
	motor_linefeed.wait_while('running',timeout=00)
	time.sleep(0.)

def backward(amt=0):
	motor_linefeed.run_to_rel_pos(position_sp=amt*LINE_HEIGHT, speed_sp=400, stop_action='hold')
	motor_linefeed.wait_while('running',timeout=1000)
	time.sleep(0.2)


def pen_up(amt=0):
	motor_pen.run_to_rel_pos(position_sp=amt*PEN_DROP*-1, speed_sp=400, stop_action='hold')
	motor_pen.wait_while('running',timeout=1000)
	time.sleep(0.1)

def pen_down(amt=0):
	motor_pen.run_to_rel_pos(position_sp=amt*PEN_DROP, speed_sp=400, stop_action='hold')
	motor_pen.wait_while('running',timeout=1000)
	time.sleep(0.1)


def go_to(pos=0):
	start = str(motor_print_head.position)
	motor_print_head.run_to_abs_pos(position_sp=pos, speed_sp=400, stop_action='hold')
	motor_print_head.wait_while('running',timeout=4000)
	time.sleep(0.2)
	finish = str(motor_print_head.position)
	dif = str( int(finish) - int(pos) )
	print('start: ' + start + '\tdest: ' + str(pos) + '\tfinish: ' + finish + '\tdif: ' + dif )


def pen_draw(amt=0):
	start = motor_pen.position
	dest = start + (amt*PEN_DROP)
	motor_pen.run_to_rel_pos(position_sp=dest, speed_sp=400, stop_action='hold')
	motor_pen.wait_while('running',timeout=1000)
	time.sleep(0.2)
	motor_pen.run_to_abs_pos(position_sp=0, speed_sp=400, stop_action='hold')
	motor_pen.wait_while('running',timeout=1000)
	time.sleep(0.2)



def josh():
	# LETTER J

	pen_down(3)
	right(20)
	pen_up(3)
	left(10)
	pen_down(3)
	forward(20)
	left(10)
	pen_up(3)

	# SPACE
	right(25)

	# LETTER O
	pen_down(3)
	backward(20)
	right(20)
	forward(20)
	left(20)
	pen_up(3)

	# SPACE
	right(25)

	# LETTER S
	pen_down(3)
	right(20)
	backward(10)
	left(20)
	backward(10)
	right(20)
	pen_up(3)

	# SPACE
	right(25)

	# LETTER S
	pen_down(3)
	forward(20)
	pen_up(3)
	backward(10)
	pen_down(3)
	right(20)
	pen_up(3)
	backward(10)
	pen_down(3)
	forward(20)
	pen_up(3)


def checkRemainingPixels( j, pixels ):
	# Returns true if all remaining pixels are empty, false if there's at least one black pixel
	for px in pixels[j:]:
		if px < 0.25: 
			return False
	return True








def reset_motors():
	motor_linefeed.reset()
	motor_print_head.reset()
	motor_pen.reset()


def main(filename='josh.png'):

	reset_motors()

	print (filename)

	img = png.Reader(filename=filename)
	imgFloat = img.asFloat()
	print ( imgFloat )
	planes = imgFloat[3]['planes']


	horiz_amt = 5*3
	vert_amt = 2*8

	# Calculate positions where pen needs to go
	pen_rows = []
	for row in imgFloat[2]:
		pen_positions = []
		position = 0

		for px in row[0::planes]:
			# If pixel is black, add this position to the list
			if px < 0.25:
				pen_positions.append(position)
				position -= horiz_amt
			# Otherwise increment position value
			else:
				position -= horiz_amt

		pen_rows.append(pen_positions)
	print (pen_rows)

	cr()
	forward(12)

	for row in pen_rows:
		for pos in row:
			go_to(pos)
			pen_draw(5)

		cr()
		forward(vert_amt)

	reset_motors()



if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--filename", help="PNG filename")
	args = parser.parse_args()
	if args.filename:
		try:
			main(args.filename)
		except:
			reset_motors()
			exit()
