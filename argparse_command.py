
#link: https://www.youtube.com/watch?v=cdblJqEUDNo

import math
import argparse

""" # this is the basic (positional argument)
parser = argparse.ArgumentParser(description='Calculate volume of Cylinder')
parser.add_argument('radius',type=int,help='Radius of Cylinder')
parser.add_argument('height',type=int,help='Height of Cylinder')
args = parser.parse_args()
"""
#  if we want to input at any order (optional argument- add long hand notation)
#parser = argparse.ArgumentParser(description='Calculate volume of Cylinder')
#parser.add_argument('--radius',type=int,help='Radius of Cylinder')
#parser.add_argument('--height',type=int,help='Height of Cylinder')
#args = parser.parse_args()


""""#  we can even assign short cuts (flag- add shot hand notation)
parser = argparse.ArgumentParser(description='Calculate volume of Cylinder')
parser.add_argument('--radius',type=int,metavar='',help='Radius of Cylinder') #metavar just align flag and optional arguments well when we use 'help'
parser.add_argument('--height',type=int,metavar='',help='Height of Cylinder')
args = parser.parse_args()
"""

# 'metavar' just align flag and optional arguments well when we use 'help'
# 'required=True' makes it mantatory to ask for inputs

parser = argparse.ArgumentParser(description='Calculate volume of Cylinder')
parser.add_argument('-r','--radius', type=int, metavar='', required=True, help='Radius of Cylinder')
parser.add_argument('-H','--height', type=int, metavar='', required=True, help='Height of Cylinder')
# mutually exclusive arguments
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet', action= 'store_true',help='print quiet')
group.add_argument('-v','--verbose', action= 'store_true',help='print verbose')
args = parser.parse_args()


def cylinder_volume(radius,height):
	return (math.pi) * (radius**2) * (height)


if __name__=='__main__':
	volume = cylinder_volume(args.radius,args.height)
	if args.quiet:
		print(volume)
	elif args.verbose:
		print("volume of the cylinder with radius %s and height %s is %s"% (args.radius,args.height,volume) )
	else:
		print("volume of the cylinder = %s"%volume)


############
#  python argparse_command.py -h
#  python argparse_command.py 2 4

############
# --radius 2 --height 5

############
# -r 2 -H 5

############ to see the use of 'required=True'
# -r 2

#-r 2 -H 4 -v