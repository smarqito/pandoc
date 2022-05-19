#!/usr/bin/env python3 
#----------------------------------------------------------------
# Created by: G53@PL
# Created date: 2022-04-11
# Version = '1.0'
#----------------------------------------------------------------
''' pandoc_lex.py: Lexic analysis '''
#----------------------------------------------------------------
from re import *
import ply.lex as lex
import sys

states = [
    ('metadata', 'exclusive'),
    ('args', 'exclusive')
]

reservadas = "if else elseif endif for endfor sep it".upper().split(' ')

tokens = "ID TEXT OPAR CPAR BACK COLON OSQBRAC CSQBRAC COMMA DOT SLASH NUM QUO NL".split(' ') + reservadas

literals = "^".split(' ')


#  adicionar contexto para o $ com lookbehind do '\' -> "(?<!\\)$"

###################
# handle metadata
###################

def t_ON(t):
    r"\$"
    t.lexer.push_state('metadata')

def t_metadata_OFF(t):
    r"\$"
    t.lexer.pop_state()
    if len(t.value) > 1:
        t.lexer.lineno += 1

###################
# handle conditions
###################
# def t_metadata_COND(t):
#     r"(if|elseif|for)"
#     t.lexer.push_state('conditions')
#     t.type = t.value.upper()
#     return t
    
# def t_conditions_CPAR(t):
#     r"\)"
#     t.lexer.pop_state()
#     return t

# def t_conditions_CID(t):
#     r'(?i)[a-z_]\w*'
#     return t

def t_TEXT(t): 
    r"[^$\\\n]+"
    return t

def t_BACK(t):
    r"\\[^\s]+"
    return t

def t_error(t):
    print("Illegal char '%s'" % t.value[0])
    t.lexer.skip(1)

    return t

def t_metadata_ID(t):
    r'(?i)[a-z_-][\w-]*'
    if t.value.upper() in reservadas:
        t.type = t.value.upper()
    return t

def t_metadata_OPAR(t):
    r"\("
    return t
    
def t_metadata_CPAR(t):
    r"\)"
    return t

def t_metadata_COLON(t):
    r":"
    return t

def t_metadata_OSQBRAC(t):
    r"\["
    return t

def t_metadata_CSQBRAC(t):
    r"\]"
    return t

def t_metadata_COMMA(t):
    r","
    return t

def t_metadata_DOT(t):
    r"\."
    return t

def t_metadata_NUM(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_metadata_SLASH(t):
    r"\/"
    return t

def t_metadata_QUO(t):
    r"\""
    t.lexer.push_state('args')
    return t
    
def t_args_QUO(t):
    r"\""
    t.lexer.pop_state()
    return t

def t_args_TEXT(t):
    r'[^"]+'
    return t

def t_metadata_args_error(t):
      print("Metadata illegal!! '%s'" % t.value)
      exit()

def t_NL(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
     return t


t_metadata_args_ignore = ' \t\r'

lexer = lex.lex()

# for line in sys.stdin:
#     lexer.input(line)
#     for tok in lexer:
#         print(tok)