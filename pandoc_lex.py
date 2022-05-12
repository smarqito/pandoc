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
    # ('conditions', 'exclusive')
]

reservadas = "if else elseif endif for endfor sep".upper().split(' ')

tokens = "ID TEXT OPAR CPAR BACK".split(' ') + reservadas

literals = ". /".split(' ')


#  adicionar contexto para o $ com lookbehind do '\' -> "(?<!\\)$"

###################
# handle metadata
###################

def t_ON(t):
    r"\$"
    t.lexer.push_state('metadata')

def t_metadata_OFF(t):
    r"\$\n?"
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
    r"[^$\\]+"
    return t

def t_BACK(t):
    r"\\[^\s]+"
    return t

def t_error(t):
    print("Illegal char '%s'" % t.value[0])
    t.lexer.skip(1)

    return t

def t_metadata_ID(t):
    r'(?i)[a-z_]\w*'
    if t.value.upper() in reservadas:
        t.type = t.value.upper()
    return t

def t_metadata_OPAR(t):
    r"\("
    return t
    
def t_metadata_CPAR(t):
    r"\)"
    return t

def t_metadata_error(t):
      print("Metadata illegal!! '%s'" % t.value)
      exit()

# def t_ANY_newline(t):
#      r'\n+'
#      t.lexer.lineno += len(t.value)


t_metadata_ignore = ' \t\r'

lexer = lex.lex()

# for line in sys.stdin:
#     lexer.input(line)
#     for tok in lexer:
#         print(tok)