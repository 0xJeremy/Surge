import ply.yacc as yacc
from surgelex import tokens, SurgeLexer
from ast import *

def SurgeParser():
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

	lexer = SurgeLexer()
	return yacc.yacc()
