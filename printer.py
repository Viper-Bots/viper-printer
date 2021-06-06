from ev3dev2.motor import *
import datetime
import time
from purepng import png
import argparse

SECONDS_1 = datetime.timedelta(seconds=1)
SECONDS_3 = datetime.timedelta(seconds=3)
TIME_LIMIT = datetime.timedelta(seconds=2)

# Variables to control spacing
LINE_HEIGHT = 1
DOT_SPACING = 60
LINE_SPACING = 16

# Time to sleep between actions
SLEEP_TIME = 0.05

# Motor port assignments
motor_linefeed = MediumMotor("outB")
motor_print_head = MediumMotor("outC")
motor_pen = MediumMotor("outD")

def out(s):
	return str(s).rjust(5)


# Carriage return
def cr():
	motor_print_head.run_to_abs_pos(position_sp=0, speed_sp=800, stop_action='hold')
	motor_print_head.wait_while('running',timeout=4000)
	time.sleep(SLEEP_TIME)

def forward(amt=0):
	motor_linefeed.run_to_rel_pos(position_sp=amt*LINE_HEIGHT*-1, speed_sp=300, stop_action='hold')
	motor_linefeed.wait_while('running',timeout=4000)
	time.sleep(SLEEP_TIME)

def backward(amt=0):
	motor_linefeed.run_to_rel_pos(position_sp=amt*LINE_HEIGHT, speed_sp=300, stop_action='hold')
	motor_linefeed.wait_while('running',timeout=4000)
	time.sleep(SLEEP_TIME)

def pen_draw(amt=0):
	start = motor_pen.position
	dest_rel = amt*PEN_DROP
	dest_abs = start + dest_rel
	motor_pen.run_to_rel_pos(position_sp=dest_rel, speed_sp=500, stop_action='hold')
	motor_pen.wait_while('running',timeout=4000)
	finish = motor_pen.position
	dif = int(finish) - int(dest_abs)
	print(' pen start: ' + out(start) + '\tdest: ' + out(dest_abs) + '\t pen finish: ' + out(finish) + '\tdif: ' + out(dif) )
	time.sleep(SLEEP_TIME)

	# THIS USES ABSOLUTE VALUES AND .run_to_abs_pos()
	curr = motor_pen.position
	motor_pen.run_to_abs_pos(position_sp=0, speed_sp=600, stop_action='hold')
	motor_pen.wait_while('running',timeout=4000)
	time.sleep(SLEEP_TIME)
	finish = motor_pen.position
	dif = int(finish) - int(0)
	print(' pen start: ' + out(curr) + '\tdest: ' + out(0) + '\t pen finish: ' + out(finish) + '\tdif: ' + out(dif) )


# THIS USES ABSOLUTE VALUES AND .run_to_abs_pos()
def pen_reset(pos=0):
	start = motor_pen.position
	motor_pen.run_to_abs_pos(position_sp=0, speed_sp=600, stop_action='hold')
	motor_pen.wait_while('running',timeout=4000)
	finish = motor_pen.position
	dif = int(finish) - int(pos)
	print(' pen start: ' + out(start) + '\tdest: ' + out(0) + '\t pen finish: ' + out(finish) + '\tdif: ' + out(dif) )


# THIS USES ABSOLUTE VALUES AND .run_to_abs_pos()
def go_to(pos=0):
	start = motor_print_head.position
	motor_print_head.run_to_abs_pos(position_sp=pos, speed_sp=600, stop_action='hold')
	motor_print_head.wait_while('running',timeout=8000)
	time.sleep(SLEEP_TIME)
	finish = motor_print_head.position
	dif = int(finish) - int(pos)
	print('goto start: ' + out(start) + '\tdest: ' + out(pos) + '\tgoto finish: ' + out(finish) + '\tdif: ' + out(dif) )



def checkRemainingPixels( j, pixels ):
	# Returns true if all remaining pixels are empty, false if there's at least one black pixel
	for px in pixels[j:]:
		if px < 0.25: 
			return False
	return True


def motors_off():
	motor_linefeed.off()
	motor_print_head.off()
	motor_pen.off()


def reset_motor_params():
	motor_linefeed.reset()
	motor_print_head.reset()
	motor_pen.reset()


def reset_printer():
	# Move print head back to start position
	print(' - Resetting print_head')
	go_to(0)

	print(' - Resetting pen')
	pen_reset(0)


def main(filename='png/cartoon.png'):

	reset_motor_params()

	img = png.Reader(filename=filename)
	imgFloat = img.asFloat()
	print('* Parsed data from PNG file:')
	print(imgFloat)
	planes = imgFloat[3]['planes']

	# Need to change these to be variables so it's clearer what I'm multiplying.
	horiz_amt = 5*12
	vert_amt = 4*4

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

	print('* Calculated pen positions:')
	print (pen_rows)

	print('\n\n')
	print('* BEGINNING TO PRINT')

	cr()
	forward(60)

	for row in pen_rows:
		for pos in row:
			go_to(pos)
			pen_draw(25)

		cr()
		forward(vert_amt)

	print('* PRINTING COMPLETE!')


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--filename", help="PNG filename")
	args = parser.parse_args()
	if args.filename:
		print('RUNNING. Loading file `' + args.filename + '`')

		try:
			print('RUNNING. Loading file `' + args.filename + '`')
			main(args.filename)
			reset_printer()
			motors_off()
		except KeyboardInterrupt:
			reset_printer()
			motors_off()
			sys.exit(0)
		except Exception as e:
			print('ERROR. There was a problem. Exiting.')
			reset_printer()
			motors_off()
			sys.exit(e)
