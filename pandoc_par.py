#!/usr/bin/env python3
# #----------------------------------------------------------------
# Created by: G53@PL
# Created date: 2022-04-11
# Version = '1.0'
#----------------------------------------------------------------
''' pandoc_par.py: parsing algorithm '''
#----------------------------------------------------------------
from re import *
import sys
import ply.yacc as yacc
from modules.Entity import Entity
from modules.StmtFor import StmtFor
from modules.Var import Var
from pandoc_lex import tokens
from modules.Document import Document
from modules.StmtIf import StmtIf
from modules.Text import Text
from modules.StmtIfElse import StmtIfElse
from modules.Subtemplate import Subtemplate
from modules.ItVar import ItVar
from modules.It import It
##########################################
def my_error(msg):
     print(msg)
     exit()

def getVar(dict, elem):
     if elem in dict:
          return dict[elem]

def getFinfo(path) -> dict:
     m = search(r"(?P<path>\/?(?:\w+\/)*)(?P<fname>[^\\\/;:\"?<>|]+)(?P<ext>\.\w+)$", path) 
     return {
          'path' : m['path'],
          'fname' : m['fname'],
          'ext' : m['ext']
     } 

##########################################

######## LIXO PARA REMOVER
ids = {
    'obj' : {
        'incl' : 'ola',
        'bat' : ['eu', 'sei', 'que', 'nao', 'vai', 'funcionar', 'direito'],
        'map' : {'key1' : {'key22' : 'value2'}, 'key2' : {'key22' : 'value22'}, 'key3' : {'key22' : 'value222'}}
    }
    
}
########

######################
#     @axioma        #
#     Document       #
######################

def p_Doc(p): 
     "Doc : Elems" 
     p[0]= Document(p[1])

######################
#     Elementos      #
######################

def p_Elems_a(p):
     r"Elems : Elems Elem"
     p[0] = p[1] + [p[2]]

def p_Elems_b(p): 
     r"Elems : Elem"
     p[0] = [p[1]]

######################
#     Elemento       #
######################

def p_Elem_a(p): 
     r"Elem : Stmt"
     #p[0] = p[1]
     p[0] = p[1]

def p_Elem_b(p): 
     r"Elem : TEXT"
     p[0] = Text(p[1])

def p_Elem_c(p): 
     r"Elem : Var"
     p[0] = p[1]

def p_Elem_d(p):
     r"Elem : BACK"
     p[0] = Entity(p[1])

def p_Elem_e(p):
     r"Elem : It"
     p[0] = p[1]

######################
#       STMT         #
######################

def p_Stmt_If(p):
     r"Stmt : If"
     p[0] = p[1]

def p_Stmt_For(p):
     r"Stmt : For"
     p[0] = p[1]

def p_Stmt_Subtemplate(p):
     r"Stmt : Subtemplate"
     p[0] = p[1]

######################
#       IF STMT      #
######################

def p_If(p):
     r'If : IF OPAR Cond CPAR Elems Else ENDIF'
     _elseifs, _else = p[6] # Else
     if len(_else) > 0 or len(_elseifs) > 0:
          p[0] = StmtIfElse(p[3], p[5], _elseifs, _else)
     else:         
          p[0] = StmtIf(p[3], p[5])

######################
#        Else        #
######################

def p_Else_a(p):
     r'Else : ELSE Elems'
     p[0] = ([], p[2])

def p_Else_b(p):
     r'Else : ElseIf Else'
     p[0] = (p[1] + p[2][0], p[2][1])

def p_Else_d(p):
     r'Else : '
     p[0] = ([], [])
     
######################
#       ElseIf       #
######################

def p_ElseIf(p):
     r'ElseIf : ELSEIF OPAR Cond CPAR Elems'
     p[0] = [StmtIf(p[3], p[5])]


######################
#      For Stmt      #
######################

def p_For(p):
     r"For : FOR OPAR Cond CPAR Elems Sep ENDFOR"
     p[0] = StmtFor(p[3], p[5], p[6])

def p_Sep(p):
     r"Sep : SEP TEXT"
     p[0] = p[2]

def p_Sep_empty(p):
     r"Sep : "
     p[0] = None

######################
#     Subtemplate    #
######################

def p_subtemplate_a(p):
     r"Subtemplate : Var OPAR CPAR"
     np = yacc.yacc()
     np.lineno = p.lineno
     np.yaml = p.parser.yaml
     np.finfo = p.parser.finfo
     p[0] = Subtemplate(p[1].getKeyword(), np)

######
# def p_subtemplate_b(p):
#      r"Subtemplate : Var COLON Var OPAR CPAR"
#      np = yacc.yacc()
#      kws = p[1].getKeywords() # keywords por lista
#      if kws[0] == "it":
#           np.yaml = None
#      else:
#           print("erro na iteracao")
#           exit()
#      np.lineno = p.lineno
#      np.finfo = p.parser.finfo
#      p[0] = Subtemplate(p[3].getKeyword(), np, kws[1:])
######

######################
#         IT         #
######################

def p_It(p):
     r"It : IT ItOpt"
     p[0] = p[2]

def p_ItOpt_subtemplate_var(p):
     r"ItOpt : DOT Var COLON Subtemplate"
     p[4].setObj(None)
     p[4].setKeywords(p[2].getKeywords())
     p[0] = p[4]

def p_ItOpt_subtemplate(p):
     r"ItOpt : COLON Subtemplate"
     p[2].setObj(None)
     p[0] = p[2]

def p_ItOpt_Var(p):
     r"ItOpt : DOT Var"
     p[0] = ItVar(p[2].getKeywords(), p.parser.yaml)

#def p_ItOpt_Var_brackets(p):
#     r"ItOpt : OSQBRACK NUM COMMA NUM CSQBRACK"

def p_ItOpt_Var_empty(p):
     r"ItOpt : "
     p[0] = It(p.parser.yaml)


######################
#     Condicoes      #
######################

def p_Cond_a(p): 
     r"Cond : Var"
     p[0] = p[1]

######################
#        Var         #
######################

def p_Var_a(p): 
     r"Var : Var DOT ID"
     p[1].nextValue(p[3])
     p[0] = p[1]

def p_Var_b(p): 
     r"Var : ID"
     p[0] = Var(p[1], p.parser.yaml)

######################
#      CondVar_      #
######################

# def p_CondVar_a(p): 
#      r"CondVar : CondVar '.' CID"
#      p[1].nextValue(p[3])
#      p[0] = p[1]

# def p_CondVar_b(p): 
#      r"CondVar : CID"
#      p[0] = CondVar(p[1], p.parser.yaml)

# def p_Var_c(p):
#      r"Var : ID '(' ')'"
#      subtemplate = open(p[1])
#      txt = subtemplate.read()
#      #print(p.parser.parse(txt, lexer=lexer))
#      p[0] = "partial"

# def p_Var_d(p):
#      r"Var : Var '/' ID"
#      if p[1] is list:
#           if p[3] == "length":
#                p[0] = len(p[1])
#           elif p[3] == "first":
#                p[0] = p[1].get(0, "N/D")
#           elif p[3] == "last":
#                p[0] = p[1].get(len(p[1]) - 1, "N/D")
#           elif p[3] == "reverse":
#                p[0] = p[1].reverse()
#      elif p[1] is dict:
#           if p[3] == "pairs":
#                p[0] = "convert to array os maps"
#      else:
#           if p[3] == "uppercase":
#                p[0] = p[1].upper()
#           elif p[3] == "lowercase":
#                p[0] = p[1].lower()
#           elif p[3] == "length":
#                p[0] = len(p[1])
#           else:
#                print("pipe nao definido")
# def p_sep_a(p):
#      r"Sep : SEP TEXTO"
#      p[0] = p[2]

# def p_sep_b(p):
#      r"Sep : "
#      p[0] = ""



def p_error(p):
     print("Syntax error in input!", p)

parser = yacc.yacc()
parser.lineno = 0


#parser.level = 0

# for line in sys.stdin:
#     print(parser.parse(line))
if len(sys.argv) == 1:
     parser.yaml = ids
     for line in sys.stdin:
          print(parser.parse(line))
else:
     parser.finfo = getFinfo(sys.argv[1])
     parser.yaml = ids
     f = open(sys.argv[1])
     txt = f.read()
     result = parser.parse(txt)
     result.pp()