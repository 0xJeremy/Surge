from ast import *

class CannotFindA(Exception):
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
	def __init__(self, cls, fields):
		self.cls = cls
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
		if lookup(A, e.value) is not None:
			return lookup(A, e.value)
		raise CannotFindA
	elif type(e) == ELocWr:
		A, H, v = eval(p, A, H, e)


def run(p):
	e = p.prog_main
	A = {}
	H = {}
	loc = fresh_location()
	update(H, (loc, object("Object", [])))
	update(A, ("self", loc))
	A1, H1, v = eval(p, A, H, e)
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

