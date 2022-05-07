#!/usr/bin/env python3
#----------------------------------------------------------------
# Created by: G53@PL
# Created date: 2022-04-11
# Version = '1.0'
#----------------------------------------------------------------
''' pandoc_par.py: parsing algorithm '''
#----------------------------------------------------------------
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
     r"Stmt : IF '(' Cond ')' Rules Elseif ENDIF"
     p[0] = ""
     if p[3] != "N/D":
          p[0] = p[5] + p[6]
     

def p_Stmt_b(p): 
     r"Stmt : FOR '(' Var ')' Rules ENDFOR"  
     p[0] = ""
     for elem in p[3]:
          p[0] += p[5]

def p_Stmt_c(p): 
     r"Stmt : Var"
     p[0] = str(p[1])

def p_elseif_a(p):
     r"Elseif : Elseif ELSEIF '(' Cond ')' Rules Else"
     #p[0] = p[1] + p[2] + p[3] + str(p[4]) + p[5] + p[6] + p[7]
     p[0] = ""
     if p[4] != "N/D":
          p[0] = p[6] + p[7]

def p_elseif_b(p):
     r"Elseif : "
     p[0] = ""

def p_else_a(p):
     r"Else : ELSE Rules"
     p[0] = p[2]

def p_else_b(p):
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

def p_error(p):
     print("Syntax error in input!", p)

parser = yacc.yacc()

parser.ids = {
    'obj' : {
        'incl' : 'ola',
        'bat' : ['eu', 'sei', 'que', 'nao', 'vai', 'funcionar', 'direito']
    }
}

parser.level = 0

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


