import ply.lex as lex

reserved = {
	'class': 'CLASS',
	'if':    'IF',
	'then':  'THEN',
	'else':  'ELSE',
	'end':   'END',
	'def':   'DEF',
	'nil':   'NIL',
	'self':  'SELF',
	'begin': 'BEGIN',
	'new':   'NEW',
}

tokens = [
	'INHERITS',
	'LPAREN',
	'RPAREN',
	'COMMA',
	'SEMI',
	'DOT',
	'EQ',
	'STRING',
	'ID',
	'FID',
	'NUMBER'
] + list(reserved.values())

t_INHERITS = r'\<'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_COMMA    = r'\,'
t_SEMI     = r'\;'
t_DOT      = r'\.'
t_EQ       = r'\='

t_ignore  = ' \t'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	if t.value in reserved:
		t.value = reserved[t.value]
	return t

def t_FID(t):
	r'^@[a-zA-Z_][a-zA-Z_0-9]*'
	if t.value in reserved:
		t.type = reserved[t.value]
	return t

def t_NUMBER(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Integer value too large %d", t.value)
		t.value = 0
	return t

def t_STRING(t):
	r'^"$"'
	t.value = string(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

def t_COMMENT(t):
	r'\#.*'
	pass

lexer = lex.lex()

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
		break
