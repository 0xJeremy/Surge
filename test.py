from ast import *
import ply.lex as lex
import ply.yacc as yacc

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
	'NUMBER'
] + list(reserved.values())

t_INHERITS = r'\<'
t_LP       = r'\('
t_RP       = r'\)'
t_COMMA    = r'\,'
t_SEMI     = r'\;'
t_DOT      = r'\.'
t_EQ       = r'\='
t_ignore   = ' \t'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	if t.value in reserved:
		t.type = reserved[t.value]
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

def p_p(p):
	'''program : class expression'''
	p[0] = surge_prog(p[1], p[2])

def p_c(p):
	'''class : CLASS ID INHERITS ID BEGIN method END'''
	p[0] = cls(p[2], p[4], p[6])

def p_m(p):
	'''method : DEF ID expression expression END'''
	p[0] = meth(p[2], p[3], p[4])

def p_expression(p):
	'''expression : value'''
	p[0] = p[1]

def p_self(p):
	'''expression : SELF'''
	p[0] = ESelf()

def p_id(p):
	'''expression : ID'''
	p[0] = ELocRd()

def p_fid(p):
	'''expression : FID'''
	p[0] = EFldRd()

def p_locwr(p):
	'''expression : ID EQ expression'''
	p[0] = ELocWr(p[1], p[3])

def p_fldwr(p):
	'''expression : FID EQ expression'''
	p[0] = ERldWr(p[1], p[3])

def p_new(p):
	'''expression : NEW ID'''
	p[0] = ENew(p[2])

def p_if(p):
	'''expression : IF expression THEN expression ELSE expression'''
	p[0] = EIf(p[2], p[4], p[6])

def p_seq(p):
	'''expression : expression SEMI expression'''
	p[0] = ESeq(p[1], p[3])

def p_invoke(p):
	'''expression : expression DOT expression LP expression RP'''
	p[0] = EInvoke(p[1], p[3], p[5])

def p_int(p):
	'''value : NUMBER'''
	p[0] = EInt(p[1])

def p_nil(p):
	'''value : NIL'''
	p[0] = ENil()

def p_string(p):
	'''value : STRING'''
	p[0] = EString(p[1])

parser = yacc.yacc()

