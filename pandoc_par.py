#!/usr/bin/env python3
#----------------------------------------------------------------
# Created by: G53@PL
# Created date: 2022-04-11
# Version = '1.0'
#----------------------------------------------------------------
''' pandoc_par.py: parsing algorithm '''
#----------------------------------------------------------------
from array import array
from re import *
import sys
import ply.yacc as yacc
from pandoc_lex import tokens

def p_Doc(p): 
     "Doc : Rules" 
     p[0] = p[1]

def p_Rules_a(p): 
     r"Rules : "
     p[0] = ''     

def p_Rules_b(p):
     r"Rules : Rules Rule"
     p[0] = p[1] + p[2]

def p_Rule_a(p): 
     r"Rule : Stmt"
     p[0] = p[1]

def p_Rule_b(p): 
     r"Rule : TEXTO"
     p[0] = p[1]

def p_Stmt_a(p):
     r"Stmt : IF '(' Cond ')' Rules Else ENDIF"
     if p[3] != "N/D":
          p[0] = p[5]
     else:
          p[0] = p[6]
     

def p_Stmt_b(p): 
     r"Stmt : FOR '(' Var ')' Rules ENDFOR"  
     p[0] = ""
     for elem in p[3]:
          p[0] += p[5]

def p_Stmt_c(p): 
     r"Stmt : Var"
     p[0] = str(p[1])

def p_else_a(p):
     r"Else : ELSEIF '(' Cond ')' Rules Else"
     if p[3] != "N/D":
          p[0] = p[5]
     else:
          p[0] = p[6]

def p_else_b(p):
     r"Else : ELSE Rules"
     p[0] = p[2]

def p_else_c(p):
     r"Else : "
     p[0] = ""

def p_Cond_a(p): 
     r"Cond : Var"
     p[0] = p[1]

def p_Var_a(p): 
     r"Var : Var '.' ID"
     p[0] = p[1].get(p[3], "N/D")

def p_Var_b(p): 
     r"Var : ID"
     p[0] = p.parser.ids.get(p[1], "N/D")

def p_Var_c(p):
     r"Var : ID '(' ')'"
     subtemplate = open(p[1])
     txt = subtemplate.read()
     #p[0] = p.parse(txt)
     p[0] = "partial"

def p_Var_d(p):
     r"Var : Var '/' ID"
     if p[1] is array:
          if p[3] == "length":
               p[0] = len(p[1])
          elif p[3] == "first":
               p[0] = p[1].get(0, "N/D")
          elif p[3] == "last":
               p[0] = p[1].get(len(p[1]) - 1, "N/D")
          elif p[3] == "reverse":
               p[0] = p[1].reverse()
     elif p[1] is dict:
          if p[3] == "pairs":
               p[0] = "convert to array os maps"
     else:
          if p[3] == "uppercase":
               p[0] = p[1].upper()
          elif p[3] == "lowercase":
               p[0] = p[1].lower()
          if p[3] == "length":
               p[0] = len(p[1])
          else :
               print("pipe nao definido")

def p_error(p):
     print("Syntax error in input!", p)

parser = yacc.yacc()

parser.ids = {
    'obj' : {
        'incl' : 'ola',
        'bat' : ['eu', 'sei', 'que', 'nao', 'vai', 'funcionar', 'direito']
    }
}

#parser.level = 0

# for line in sys.stdin:
#     print(parser.parse(line))
if len(sys.argv) == 1:
     for line in sys.stdin:
          print(parser.parse(line))
else:
     f = open(sys.argv[1])
     txt = f.read()
     result = parser.parse(txt)
     print(result)


