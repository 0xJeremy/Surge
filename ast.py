class Expr: pass

class EInt(Expr):
	def __init__(self, value):
		self.type = "EInt"
		self.value = data

class ENil(Expr):
	def __init__(self):
		self.type = "ENil"

class ESelf(Expr):
	def __init__(self):
		self.type = "ESelf"

class EString(Expr):
	def __init__(self, value):
		self.type = "EString"
		self.value = value

class ELocRd(Expr):
	def __init__(self, value):
		self.type = "ELocRd"
		self.value = value

class ELocWr(Expr):
	def __init__(self, value, expr):
		self.type = "ELocWr"
		self.value = value
		self.expr = expr

class EFldRd(Expr):
	def __init__(self, value):
		self.type = "EFldRd"
		self.value = value

class EFldWr(Expr):
	def __init__(self, value, expr):
		self.type = "EFldWr"
		self.value = value
		self.expr = expr

class EIf(Expr):
	def __init__(self, guard, expr1, expr2):
		self.type = "EIf"
		self.guard = guard
		self.expr1 = expr1
		self.expr2 = expr2

class ESeq(Expr):
	def __init__(self, expr1, expr2):
		self.type = "ESeq"
		self.expr1 = expr1
		self.expr2 = expr2

class ENew(Expr):
	def __init__(self, value):
		self.type = "ENew"
		self.value = value

class EInvoke(Expr):
	def __init__(self, value, name, args):
		self.type = "EInvoke"
		self.value = value
		self.name = name
		self.args = args

class meth():
	def __init__(self, name, args, body):
		self.name = name
		self.args = args
		self.body = body

class cls():
	def __init__(self, name, super, meths):
		self.name = name
		self.super = super
		self.meths = meths

class surge_prog():
	def __init__(self, prog_clss, prog_main):
		self.prog_clss = prog_clss
		self.prog_main = prog_main
