## TODO: Fix string parsing

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
	'LP',
	'RP',
	'COMMA',
	'SEMI',
	'DOT',
	'EQ',
	'STRING',
	'ID',
	'FID',
	'NUMBER',
	'EOF'
] + list(reserved.values())


def SurgeLexer():

	t_INHERITS = r'\<'
	t_LP       = r'\('
	t_RP       = r'\)'
	t_COMMA    = r'\,'
	t_SEMI     = r'\;'
	t_DOT      = r'\.'
	t_EQ       = r'\='
	t_ignore   = ' \t'

	def t_ID(t):
		r'[\*\/\?\!a-zA-Z_+-]+'
		if t.value in reserved:
			t.type = reserved[t.value]
		return t

	def t_FID(t):
		r'@[\*\/\?\!a-zA-Z_+-]+'
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
		r'"[\@\=\[\]\n\ \*\/\?\!a-zA-Z0-9_+-]*"'
		t.value = str(t.value.replace('"', ''))
		return t

	def t_newline(t):
		r'\n+'
		t.lexer.lineno += t.value.count("\n")

	def t_error(t):
		print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)

	# def t_eof(t):
	# 	more = input('... ')
	# 	if more:
	# 		t.lexer.input(more)
	# 		return t.lexer.token()
	# 	return None

	def t_COMMENT(t):
		r'\#.*'
		pass

	return lex.lex()
