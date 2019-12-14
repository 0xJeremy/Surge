import ply.yacc as yacc
from surgelex import tokens, SurgeLexer
from ast import *

def SurgeParser():

	###########################
	### PROGRAM AND CLASSES ###
	###########################

	def p_main(p):
		'''main : clss exprs EOF'''
		p[0] = surge_prog(p[1], p[2])

	def p_clss(p):
		'''clss : cls clss
				| empty'''
		if len(p) == 1:
			p[0] = []
		else:
			p[0] = [p[1], p[2]]

	def p_cls(p):
		'''cls : CLASS ID INHERITS ID BEGIN meths END'''
		p[0] = cls(p[2], p[4], p[6])

	def p_meths(p):
		'''meths : meth meths
				 | empty'''
		if len(p) == 1:
			p[0] = []
		else:
			p[0] = [p[1], p[2]]

	def p_meth(p):
		'''meth : DEF ID LP ids RP exprs END'''
		p[0] = meth(p[2], p[4], p[6])

	###########################
	### IDS AND EXPRESSIONS ###
	###########################

	def p_ids(p):
		'''ids : empty
			   | ID
			   | ID COMMA ids'''
		if len(p) == 1:
			p[0] = []
		elif len(p) == 2:
			p[0] = p[1]
		elif len(p) == 4:
			p[0] = ESeq(p[1], p[3])

	def p_exprs(p):
		'''exprs : expr
				 | expr SEMI exprs'''
		if len(p) == 2:
			p[0] = p[1]
		else:
			p[0] = ESeq(p[1], p[3])

	def p_int(p):
		'''expr : NUMBER'''
		p[0] = EInt(p[1])

	def p_nil(p):
		'''expr : NIL'''
		p[0] = ENil()

	def p_self(p):
		'''expr : SELF'''
		p[0] = ESelf()

	def p_string(p):
		'''expr : STRING'''
		p[0] = EString(p[1])

	def p_id(p):
		'''expr : ID'''
		p[0] = ELocRd()

	def p_locwr(p):
		'''expr : ID EQ expr'''
		p[0] = ELocWr(p[1], p[3])


	def p_fid(p):
		'''expr : FID'''
		p[0] = EFldRd()

	def p_fldwr(p):
		'''expr : FID EQ expr'''
		p[0] = ERldWr(p[1], p[3])

	def p_if(p):
		'''expr : IF expr THEN exprs ELSE exprs END'''
		p[0] = EIf(p[2], p[4], p[6])

	def p_invoke(p):
		'''expr : expr DOT ID LP params RP'''
		p[0] = EInvoke(p[1], p[3], p[5])

	def p_new(p):
		'''expr : NEW ID'''
		p[0] = ENew(p[2])

	def p_paren(p):
		'''expr : LP exprs RP'''
		p[0] = p[2]

	def p_params(p):
		'''params : empty
				  | expr
				  | expr COMMA params'''
		if len(p) == 1:
			p[0] = []
		elif len(p) == 2:
			p[0] = p[1]
		else:
			p[0] = [p[1], p[3]]

	###############
	### HELPERS ###
	###############

	def p_empty(p):
		'''empty :'''
		pass

	def p_error(t):
		print("Syntax error at '%s'" % t.value)

	lexer = SurgeLexer()
	return yacc.yacc()
