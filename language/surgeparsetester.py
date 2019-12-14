from surgeparse import SurgeParser
from ast import *

parser = SurgeParser()

while True:
	try:
		s = input('S/> ')
	except EOFError:
		print()
		break
	x = parser.parse(s)
	print(type(x))
	if type(x) == surge_prog:
		print("PATTERN MATCHED PROG")
		cls = x.prog_clss
		main = x.prog_main
		if type(main) == EInt:
			print(main.value)
