from ev3dev.ev3 import *
import datetime
import time
import png
import argparse


def main(filename='josh.png'):

	print (filename)

	img = png.Reader(filename=filename)

	imgFloat = img.asFloat()

	print ( imgFloat )


	for row in imgFloat[2]:
		print ('ROW')
		for px in row[0::4]:
			print (px)


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--filename", help="PNG filename")
	args = parser.parse_args()
	if args.filename:
		main(args.filename)
