from surgeparse import SurgeParser

parser = SurgeParser()

while True:
	try:
		s = input('S/> ')
	except EOFError:
		print()
		break
	parser.parse(s)
