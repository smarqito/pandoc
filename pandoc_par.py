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

def p_Rules_a(p): r"Rules :";                          pass
def p_Rules_b(p): r"Rules : Rules Rule";               pass

def p_Rule_a(p): r"Rule : Stmt";                       print(p[1], end='')
def p_Rule_b(p): r"Rule : TEXTO ";                     print(p[1], end='')

def p_Stmt_a(p): r"Stmt : IF '(' Cond ')'";            p[0] = str(p[3]); p.parser.level += 1
def p_Stmt_b(p): r"Stmt : ENDIF";                      p[0] = p[1]; p.parser.level -= 1
def p_Stmt_c(p): r"Stmt : FOREACH '(' Var ')'";        p[0] = str(p[3])
def p_Stmt_d(p): r"Stmt : Var";                        p[0] = p[1]

def p_Cond_a(p): r"Cond : Var";                        p[0] = p[1]
#def p_Cond_b(p): r"Cond : ";                           pass

def p_Var_a(p): r"Var : ID";                           p[0] = p.parser.ids.get(p[1])
def p_Var_b(p): r"Var : Var '.' ID";                   p[0] = p[1].get(p[3], "N/D")

def p_debug_id(p): r"SeenId :";                        print("seen", end='')

def p_error(p):
     print("Syntax error in input!", p)

parser = yacc.yacc(debug=1)

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


