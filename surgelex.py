import ply.lex as lex

reserved = {
	'class': 'CLASS',
	'if': 'IF',
	'then': 'THEN',
	'else': 'ELSE',
	'end': 'END',
	'def': 'DEF',
	'nil': 'NIL',
	'self': 'SELF',
	'begin': 'BEGIN',
	'new': 'NEW',
}

tokens = [
	'INHERITS',
	'LPAREN',
	'RPAREN',
	'COMMA',
	'SEMI',
	'DOT',
	'EQ',
] + list(reserved.values())

t_INHERITS = r'\<'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_COMMA    = r'\,'
t_SEMI     = r'\;'
t_DOT      = r'\.'
t_EQ       = r'\='

t_ignore  = ' \t'

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()

while True:
	try:
		s = input('RUBE > ')
		lexer.input(s)
		while True:
			tok = lexer.token()
			if not tok:
				break
			print(tok)
	except EOFError:
		break
