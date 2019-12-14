from surgelex import SurgeLexer

lexer = SurgeLexer()

while True:
	try:
		s = input('S/> ')
		lexer.input(s)
		while True:
			tok = lexer.token()
			if not tok:
				break
			print(tok)
	except EOFError:
		print()
		break
