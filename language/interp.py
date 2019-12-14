from ast import *

class CannotFindInA(Exception):
	pass
class CannotFindVariable(Exception):
	pass
class NoSuchMethod(Exception):
	pass
class Fail(Exception):
	pass


class SurgeVal: pass
class RNil(SurgeVal): pass
class RInt(SurgeVal):
	def __init__(self, value):
		self.value = value
class RStr(SurgeVal):
	def __init__(self, value):
		self.value = value
class RLoc(SurgeVal):
	def __init__(self, value):
		self.value = value

class object():
	def __init__(self, class_name, fields):
		self.class_name = class_name
		self.fields = fields

def lookup(key, env):
	return env[key] if key in env.keys() else None

def update(env, t):
	key, val = t
	env[key] = val

last_loc = 0
def fresh_location():
	global last_loc
	last_loc += 1
	return last_loc

def eval(p, A, H, e):
	if   type(e) == ENil: return A, H, RNil()
	elif type(e) == EInt: return A, H, RInt(e.value)
	elif type(e) == ESelf: return A, H, RStr("self")
	elif type(e) == EString: return A, H, RStr(e.value)
	elif type(e) == ELocRd: 
		if lookup(e.value, A) is not None:
			return A, H, lookup(e.value, A)
		raise CannotFindInA
	elif type(e) == ELocWr:
		A, H, v = eval(p, A, H, e.expr)
		update(A, (e.value, v))
		return A, H, v
	elif type(e) == EFldRd:
		loc = lookup("self", A)
		if loc is None: raise CannotFindInA
		cur_object = lookup(loc, H)
		if cur_object is None: raise Fail
		value = lookup(e.value, cur_object.fields)
		if value is None: raise Fail
		return A, H, value
	elif type(e) == EFldWr:
		A, H, v = eval(p, A, H, e.expr)
		loc = lookup("self", A)
		if loc is None: raise Fail
		cur_object = lookup(loc, H)
		if cur_object is None: raise Fail
		update(cur_object.fields, (e.value, v))
		return A, H, v
	elif type(e) == EIf:
		A, H, v = eval(p, A, H, e.guard)
		if type(v) == RNil:
			return eval(p, A, H, e.expr1)
		return eval(p, A, H, e.expr2)
	elif type(e) == ESeq:
		A, H, v = eval(p, A, H, e.expr1)
		return eval(p, A, H, e.expr2)
	elif type(e) == ENew:
		if   e.value == "String": return A, H, RStr("")
		elif e.value == "Int": return A, H, RInt(0)
		elif e.value == "Bot": raise Fail
		


def run(p):
	e = p.prog_main
	A = {}
	H = {}
	loc = fresh_location()
	update(H, (loc, object("Object", [])))
	update(A, ("self", loc))
	A, H, v = eval(p, A, H, e)
	if   type(v) == RNil: print("nil")
	elif type(v) == RInt: print(v.value)
	elif type(v) == RStr: print(v.value)
	elif type(v) == RLoc: print(v.value)


	# if type(p) == surge_prog:
	# 	print("PATTERN MATCHED PROG")
	# 	cls = p.prog_clss
	# 	main = p.prog_main
	# 	print(type(main))
	# 	if type(main) == EInt:
	# 		print(main.value)

