#!/usr/bin/env python3
# #----------------------------------------------------------------
# Created by: G53@PL
# Created date: 2022-04-11
# Version = '1.0'
# ----------------------------------------------------------------
''' pandoc_par.py: parsing algorithm '''
# ----------------------------------------------------------------
from re import *
import sys
import ply.yacc as yacc
from modules.Range import Range
from pandoc_lex import tokens
from modules.Entity import Entity
from modules.Var import Var
from modules.Document import Document
from modules.Text import Text
from modules.Nesting import Nesting
from modules.Pipe import Pipe
from modules.Pipes import Pipes
from modules.It.It import It
from modules.It.ItVar import ItVar
from modules.It.ItRange import ItRange
from modules.It.ItSubtemplate import ItSubtemplate
from modules.Stmt.StmtFor import StmtFor
from modules.Stmt.StmtIf import StmtIf
from modules.Stmt.StmtIfElse import StmtIfElse
from modules.Stmt.StmtSubtemplate import StmtSubtemplate
##########################################


def my_error(msg):
    print(msg)
    exit()


def getVar(dict, elem):
    if elem in dict:
        return dict[elem]


def getFinfo(path) -> dict:
    m = search(
        r"(?P<path>\/?(?:\w+\/)*)(?P<fname>[^\\\/;:\"?<>|]+)(?P<ext>\.\w+)$", path)
    return {
        'path': m['path'],
        'fname': m['fname'],
        'ext': m['ext']
    }

##########################################


# LIXO PARA REMOVER
ids = {
    'obj': {
        'incl': 'ola',
        'bat': ['eu', 'sei', 'que', 'nao', 'vai', 'funcionar', 'direito'],
        'map': {'key1': {'key22': 'value2'}, 'key2': {'key22': 'value22'}, 'key3': {'key22': 'value222'}},
        'descr': 'A fine bottle of 18-yr-old\nOban whiskey.\nclaro que esta',
        'alpha' : 'numero para letra : 0 1 2 3 10 26',
        'roman' : 'numeros romanos : 1 4 14 93 192 1053',
        'autores' : {'ent1' : {'nome' : 'Jose', 'numero' : '93271'}, 'ent2' : {'nome' : 'Marco', 'numero' : '62608'},
                   'ent3' : {'nome' : 'Miguel', 'numero' : '94269'}}
    }

}
########

######################
#     @axioma        #
#     Document       #
######################


def p_Doc(p):
    "Doc : Elems"
    p[0] = Document(p[1])

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
    r"Elem : Stmt Newline"
    #p[0] = p[1]
    p[1].setEnd(p[2])
    p[0] = p[1]


def p_Elem_b(p):
    r"Elem : TEXT Newline"
    p[0] = Text(p[1], p[2])


def p_Elem_c(p):
    r"Elem : Var Newline"
    p[1].setEnd(p[2])
    p[0] = p[1]


def p_Elem_d(p):
    r"Elem : BACK Newline"
    p[0] = Entity(p[1], p[2])


def p_Elem_e(p):
    r"Elem : It"
    p[0] = p[1]


def p_Elem_f(p):
    r"Elem : Nesting"
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
    r"Stmt : StmtSubtemplate"
    p[0] = p[1]

######################
#       IF STMT      #
######################


def p_If(p):
    r'If : IF OPAR Cond CPAR Newline Elems Else ENDIF'
    _elseifs, _else = p[7]  # Else
    if len(_else) > 0 or len(_elseifs) > 0:
        p[0] = StmtIfElse(p[3], p[6], _elseifs, _else)
    else:
        p[0] = StmtIf(p[3], p[6])

######################
#        Else        #
######################


def p_Else_a(p):
    r'Else : ELSE Newline Elems'
    p[0] = ([], p[3])


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
    r'ElseIf : ELSEIF OPAR Cond CPAR Newline Elems'
    p[0] = [StmtIf(p[3], p[6])]


######################
#      For Stmt      #
######################

def p_For(p):
    r"For : FOR OPAR Cond CPAR Newline Elems Sep ENDFOR"
    p[0] = StmtFor(p[3], p[6], p[7])


def p_Sep(p):
    r"Sep : SEP TEXT Newline"
    p[0] = p[2]


def p_Sep_empty(p):
    r"Sep : "
    p[0] = None

######################
#   StmtSubtemplate  #
######################


def p_subtemplate_a(p):
    r"StmtSubtemplate : VarAtomic OPAR CPAR Pipes"
    np = yacc.yacc()
    np.lineno = p.lineno
    np.yaml = p.parser.yaml
    np.finfo = p.parser.finfo
    sub = StmtSubtemplate(p[1].getKeyword(), np)
    if p[4]:
        sub.set_pipes(Pipes(p[4]))
    p[0] = sub


def p_SubIt(p):
    r"SubIt : VarAtomic OPAR CPAR"
    np = yacc.yacc()
    np.lineno = p.lineno
    np.yaml = p.parser.yaml
    np.finfo = p.parser.finfo
    sub = ItSubtemplate(p[1].getKeyword(), np)
    p[0] = sub
    
######################
#         IT         #
######################


def p_It(p):
    r"It : IT ItOpt Pipes Newline"
    p[2].setEnd(p[4])
    if p[3]:
        p[2].set_pipes(Pipes(p[3]))
    p[0] = p[2]


def p_ItOpt_subtemplate(p):
    r"ItOpt : COLON SubIt"
    p[2].setObj(None)
    p[0] = p[2]


def p_ItOpt_subtemplate_var(p):
    r"ItOpt : DOT VarAtomic COLON SubIt"
    p[4].setObj(None)
    p[4].setKeywords(p[2].getKeywords())
    p[0] = p[4]


def p_ItOpt_Var(p):
    r"ItOpt : DOT VarAtomic"
    p[0] = ItVar(p[2].getKeywords(), p.parser.yaml)


def p_ItOpt_Var_brackets_var(p):
    r"ItOpt : DOT VarAtomic OSQBRAC Num COMMA Num CSQBRAC"
    p[0] = ItRange(p.parser.yaml, (p[4], p[6]), p[2].getKeywords())


def p_ItOpt_Var_brackets(p):
    r"ItOpt : OSQBRAC Num COMMA Num CSQBRAC"
    p[0] = ItRange(p.parser.yaml, (p[2], p[4]))


def p_ItOpt_Var_empty(p):
    r"ItOpt : "
    p[0] = It(p.parser.yaml)

######################
#       NESTING      #
######################


def p_Nesting_a(p):
    r"Nesting : Var '^' NestElems '^' Newline"
    p[0] = Nesting(p[1], p[3], p[5])


def p_NestElems_a(p):
    r"NestElems : NestElems NestElem"
    p[0] = p[1] + [p[2]]


def p_NestElems_b(p):
    r"NestElems : NestElem"
    p[0] = [p[1]]


def p_NestElem_a(p):
    r"NestElem : Var"
    p[0] = p[1]


def p_NestElem_b(p):
    r"NestElem : TEXT"
    p[0] = Text(p[1])

######################
#     Condicoes      #
######################


def p_Cond_a(p):
    r"Cond : Var"
    p[0] = p[1]


def p_Cond_b(p):
    r"Cond : It"
    p[0] = p[1]

def p_Cond_c(p):
    r"Cond : Range"
    p[0] = p[1]

######################
#        Var         #
######################


def p_Var(p):
    r"Var : VarAtomic Pipes"
    if p[2]:
        pipes = Pipes(p[2])
        p[1].set_pipes(pipes)
    p[0] = p[1]


def p_VarAtomic_a(p):
    r"VarAtomic : VarAtomic DOT ID"
    p[1].nextValue(p[3])
    p[0] = p[1]


def p_VarAtomic_b(p):
    r"VarAtomic : ID"
    p[0] = Var(p[1], p.parser.yaml)

######################
#       Pipes        #
######################


def p_pipes_a(p):
    "Pipes : Pipes SLASH ID"
    p[0] = p[1] + [Pipe(p[3])]


def p_pipes_b(p):
    "Pipes : Pipes SLASH ID NUM QUO TEXT QUO"
    p[0] = p[1] + [Pipe(p[3], (p[4], p[6], None))]


def p_pipes_c(p):
    "Pipes : Pipes SLASH ID NUM QUO TEXT QUO QUO TEXT QUO"
    p[0] = p[1] + [Pipe(p[3], (p[4], p[6], p[9]))]


def p_pipes_d(p):
    "Pipes : "
    p[0] = []

# 
def p_Range(p):
    r"Range : OSQBRAC NUM COLON NUM CSQBRAC"
    p[0] = Range(p[2], p[4])
    # p[0] = p[2]

######################
#        Num         #
######################


def p_Num_a(p):
    "Num : NUM"
    p[0] = p[1]


def p_Num_b(p):
    "Num : "
    p[0] = None


def p_Newline_a(p):
    r"Newline : NL"
    p[0] = Text(p[1], p[1])


def p_Newline_b(p):
    r"Newline : "
    p[0] = Text('')


def p_error(p):
    print("Syntax error in input!", p)


parser = yacc.yacc()
parser.lineno = 0

# if len(sys.argv) == 1:
#     parser.yaml = ids
#     for line in sys.stdin:
#         print(parser.parse(line))
# else:
#     parser.finfo = getFinfo(sys.argv[1])
#     parser.yaml = ids
#     f = open(sys.argv[1])
#     txt = f.read()
#     result = parser.parse(txt)
#     result.pp()
