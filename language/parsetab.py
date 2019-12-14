
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN CLASS COMMA DEF DOT ELSE END EOF EQ FID ID IF INHERITS LP NEW NIL NUMBER RP SELF SEMI STRING THENmain : clss exprs EOFclss : cls clss\n\t\t\t\t| emptycls : CLASS ID INHERITS ID BEGIN meths ENDmeths : meth meths\n\t\t\t\t | emptymeth : DEF ID LP ids RP exprs ENDids : empty\n\t\t\t   | ID\n\t\t\t   | ID COMMA idsexprs : expr\n\t\t\t\t | expr SEMI exprsexpr : NUMBERexpr : NILexpr : SELFexpr : STRINGexpr : IDexpr : ID EQ exprexpr : FIDexpr : FID EQ exprexpr : IF expr THEN exprs ELSE exprs ENDexpr : expr DOT ID LP params RPexpr : NEW IDexpr : LP exprs RPparams : empty\n\t\t\t\t  | expr\n\t\t\t\t  | expr COMMA paramsempty :'
    
_lr_action_items = {'CLASS':([0,3,49,],[5,5,-4,]),'NUMBER':([0,2,3,4,14,15,17,20,22,23,32,35,41,46,49,59,],[-28,8,-28,-3,8,8,-2,8,8,8,8,8,8,8,-4,8,]),'NIL':([0,2,3,4,14,15,17,20,22,23,32,35,41,46,49,59,],[-28,9,-28,-3,9,9,-2,9,9,9,9,9,9,9,-4,9,]),'SELF':([0,2,3,4,14,15,17,20,22,23,32,35,41,46,49,59,],[-28,10,-28,-3,10,10,-2,10,10,10,10,10,10,10,-4,10,]),'STRING':([0,2,3,4,14,15,17,20,22,23,32,35,41,46,49,59,],[-28,11,-28,-3,11,11,-2,11,11,11,11,11,11,11,-4,11,]),'ID':([0,2,3,4,5,14,15,16,17,20,21,22,23,27,32,35,41,45,46,49,54,58,59,],[-28,12,-28,-3,18,12,12,26,-2,12,29,12,12,34,12,12,12,51,12,-4,55,55,12,]),'FID':([0,2,3,4,14,15,17,20,22,23,32,35,41,46,49,59,],[-28,13,-28,-3,13,13,-2,13,13,13,13,13,13,13,-4,13,]),'IF':([0,2,3,4,14,15,17,20,22,23,32,35,41,46,49,59,],[-28,14,-28,-3,14,14,-2,14,14,14,14,14,14,14,-4,14,]),'NEW':([0,2,3,4,14,15,17,20,22,23,32,35,41,46,49,59,],[-28,16,-28,-3,16,16,-2,16,16,16,16,16,16,16,-4,16,]),'LP':([0,2,3,4,14,15,17,20,22,23,29,32,35,41,46,49,51,59,],[-28,15,-28,-3,15,15,-2,15,15,15,35,15,15,15,15,-4,54,15,]),'$end':([1,19,],[0,-1,]),'EOF':([6,7,8,9,10,11,12,13,26,28,30,31,33,47,53,],[19,-11,-13,-14,-15,-16,-17,-19,-23,-12,-18,-20,-24,-22,-21,]),'RP':([7,8,9,10,11,12,13,25,26,28,30,31,33,35,38,39,40,46,47,52,53,54,55,56,57,58,60,],[-11,-13,-14,-15,-16,-17,-19,33,-23,-12,-18,-20,-24,-28,-26,47,-25,-28,-22,-27,-21,-28,-9,59,-8,-28,-10,]),'ELSE':([7,8,9,10,11,12,13,26,28,30,31,33,36,47,53,],[-11,-13,-14,-15,-16,-17,-19,-23,-12,-18,-20,-24,41,-22,-21,]),'END':([7,8,9,10,11,12,13,26,28,30,31,33,37,42,43,44,47,48,50,53,61,62,],[-11,-13,-14,-15,-16,-17,-19,-23,-12,-18,-20,-24,-28,49,-28,-6,-22,53,-5,-21,62,-7,]),'SEMI':([7,8,9,10,11,12,13,26,30,31,33,47,53,],[20,-13,-14,-15,-16,-17,-19,-23,-18,-20,-24,-22,-21,]),'DOT':([7,8,9,10,11,12,13,24,26,30,31,33,38,47,53,],[21,-13,-14,-15,-16,-17,-19,21,-23,21,21,-24,21,-22,-21,]),'THEN':([8,9,10,11,12,13,24,26,30,31,33,47,53,],[-13,-14,-15,-16,-17,-19,32,-23,-18,-20,-24,-22,-21,]),'COMMA':([8,9,10,11,12,13,26,30,31,33,38,47,53,55,],[-13,-14,-15,-16,-17,-19,-23,-18,-20,-24,46,-22,-21,58,]),'EQ':([12,13,],[22,23,]),'INHERITS':([18,],[27,]),'BEGIN':([34,],[37,]),'DEF':([37,43,62,],[45,45,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,],[1,]),'clss':([0,3,],[2,17,]),'cls':([0,3,],[3,3,]),'empty':([0,3,35,37,43,46,54,58,],[4,4,40,44,44,40,57,57,]),'exprs':([2,15,20,32,41,59,],[6,25,28,36,48,61,]),'expr':([2,14,15,20,22,23,32,35,41,46,59,],[7,24,7,7,30,31,7,38,7,38,7,]),'params':([35,46,],[39,52,]),'meths':([37,43,],[42,50,]),'meth':([37,43,],[43,43,]),'ids':([54,58,],[56,60,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> clss exprs EOF','main',3,'p_main','surgeparse.py',12),
  ('clss -> cls clss','clss',2,'p_clss','surgeparse.py',16),
  ('clss -> empty','clss',1,'p_clss','surgeparse.py',17),
  ('cls -> CLASS ID INHERITS ID BEGIN meths END','cls',7,'p_cls','surgeparse.py',24),
  ('meths -> meth meths','meths',2,'p_meths','surgeparse.py',28),
  ('meths -> empty','meths',1,'p_meths','surgeparse.py',29),
  ('meth -> DEF ID LP ids RP exprs END','meth',7,'p_meth','surgeparse.py',36),
  ('ids -> empty','ids',1,'p_ids','surgeparse.py',44),
  ('ids -> ID','ids',1,'p_ids','surgeparse.py',45),
  ('ids -> ID COMMA ids','ids',3,'p_ids','surgeparse.py',46),
  ('exprs -> expr','exprs',1,'p_exprs','surgeparse.py',55),
  ('exprs -> expr SEMI exprs','exprs',3,'p_exprs','surgeparse.py',56),
  ('expr -> NUMBER','expr',1,'p_int','surgeparse.py',63),
  ('expr -> NIL','expr',1,'p_nil','surgeparse.py',67),
  ('expr -> SELF','expr',1,'p_self','surgeparse.py',71),
  ('expr -> STRING','expr',1,'p_string','surgeparse.py',75),
  ('expr -> ID','expr',1,'p_id','surgeparse.py',79),
  ('expr -> ID EQ expr','expr',3,'p_locwr','surgeparse.py',83),
  ('expr -> FID','expr',1,'p_fid','surgeparse.py',88),
  ('expr -> FID EQ expr','expr',3,'p_fldwr','surgeparse.py',92),
  ('expr -> IF expr THEN exprs ELSE exprs END','expr',7,'p_if','surgeparse.py',96),
  ('expr -> expr DOT ID LP params RP','expr',6,'p_invoke','surgeparse.py',100),
  ('expr -> NEW ID','expr',2,'p_new','surgeparse.py',104),
  ('expr -> LP exprs RP','expr',3,'p_paren','surgeparse.py',108),
  ('params -> empty','params',1,'p_params','surgeparse.py',112),
  ('params -> expr','params',1,'p_params','surgeparse.py',113),
  ('params -> expr COMMA params','params',3,'p_params','surgeparse.py',114),
  ('empty -> <empty>','empty',0,'p_empty','surgeparse.py',127),
]
