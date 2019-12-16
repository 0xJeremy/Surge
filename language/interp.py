from ast import *

##################
### EXCEPTIONS ###
##################

class CannotFindInA(Exception):
	pass
class CannotFindVariable(Exception):
	pass
class NoSuchMethod(Exception):
	pass
class Fail(Exception):
	pass

###################
### SURGE TYPES ###
###################

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

########################
### HELPER FUNCTIONS ###
########################

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

#############################
### INTERPRETER FUNCTIONS ###
#############################

def defined_class(p, name):
	for obj in p.prog_clss:
		if obj.name == name:
			return True
	return False

def lookup_meth(p, c, m):
	for obj in p.prog_clss:
		if obj.name == c:
			for meth in obj.meths:
				if meth.name == m:
					return meth
			if c == "Object": return None
			lookup_meth(p, obj.super, m)
	raise Fail

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
		if defined_class(p, e.value):
			loc = fresh_location()
			update(H, (loc, object(e, {})))
			return A, H, RLoc(loc)
		raise Fail
	elif type(e) == EInvoke:
		return invoke(p, A, H, e)
		
###############################
### INVOKE DYNAMIC DISPATCH ###
###############################

def invoke(p, A, H, e):
	meth = e.name
	A, H, v_receiver = eval(p, A, H, e.value)
	v_args = []
	for item in e.args:
		A, H, v_arg = eval(p, A, H, item)
		v_args.append(v_arg)
	if type(v_receiver) == RInt:
		n = v_receiver.value
		if len(v_args) == 1 and type(v_args[0]) == RInt:
			m = v_args[0].value
			if meth == "+": return A, H, RInt(n+m)
			if meth == "-": return A, H, RInt(n-m)
			if meth == "*": return A, H, RInt(int(n*m))
			if meth == "/": return A, H, RInt(int(n/m))
			if meth == "equal?": return A, H, RInt(1) if n == m else A, H, RNil()
		if len(v_args) == 0:
			if meth == "to_s": return A, H, RStr(str(n))
			if meth == "print": print(n); return A, H, RNil()
		raise NoSuchMethod
	if type(v_receiver) == RStr:
		s = v_receiver.value
		if len(v_args) == 0:
			if meth == "length": return A, H, RInt(len(s))
			if meth == "to_s": return A, H, RStr(s)
			if meth == "print": print(s); return A, H, RNil()
		if len(v_args) == 1 and type(v_args[0]) == RStr:
			s1 = v_args[0].value
			if meth == "+": return A, H, RStr(s+s1)
			if meth == "equal?": return A, H, RInt(1) if s == s1 else A, H, RNil()
		raise NoSuchMethod
	if type(v_receiver) == RLoc:
		loc = v_receiver.value
		if len(v_args) == 0:
			if meth == "to_s": return A, H, RStr(loc)
			if meth == "print": print(loc); return A, H, RNil()
		if len(v_args) == 1 and type(v_args[0]) == RLoc:
			loc1 = v_args[0].value
			if meth == "equal?": return A, H, RInt(1) if loc == loc1 else A, H, RNil()
		cur_object = lookup(loc, H)
		if cur_object is None: raise Fail
		meth = lookup_meth(p, cur_object.class_name.value, meth)
		if meth is None: raise NoSuchMethod
		if len(v_args) != len(meth.args): raise NoSuchMethod
		tmp_A = {}
		update(tmp_A, ("self", loc))
		[update(tmp_A, item) for item in zip(meth.args, v_args)]
		tmp_A, H, s = eval(p, tmp_A, H, meth.body)
		return A, H, s

######################
### PROGRAM RUNNER ###
######################

def run(p):
	e = p.prog_main
	A = {}
	H = {}
	loc = fresh_location()
	update(H, (loc, object("Object", {})))
	update(A, ("self", loc))
	A, H, v = eval(p, A, H, e)
	if   type(v) == RNil: print("nil")
	elif type(v) == RInt: print(v.value)
	elif type(v) == RStr: print(v.value)
	elif type(v) == RLoc: print(v.value)
