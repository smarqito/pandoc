#!/usr/bin/env python3 
#----------------------------------------------------------------
# Created by: Marco António Sousa
# Created date: 2022-04-11
# Version = '1.0'
#----------------------------------------------------------------
''' pandoc_lex.py: Lexic analysis '''
#----------------------------------------------------------------
from re import *
import ply.lex as lex

states = [
    ('metadata', 'exclusive')
]

tokens = "ID IF ENDIF FOREACH TEXTO".split(' ')

literals = "$ . ( )".split(' ')

reservadas = "if else elseif endif foreach endfor".split(' ')

#  adicionar contexto para o $ com lookbehind do '\' -> "(?<!\\)$"

def t_ON(t):
    r"\$"
    t.lexer.begin('metadata')

def t_metadata_OFF(t):
    r"\$"
    t.lexer.begin('INITIAL')

def t_TEXTO(t): 
    r"[^$]+"
    return t

def t_error(t):
    print("Illegal char '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = '\t\r'
def t_eof(t):
    print(" ##endFILE##", end='')

def t_metadata_ID(t):
    r'(?i)[a-z_]\w*'
    if t.value in reservadas:
        t.type = t.value.upper()
    return t

def t_metadata_error(t):
      print("Metadata illegal!! '%s'" % t.value)
      t.lexer.begin('INITIAL')
      exit()

t_metadata_ignore = ' \t\n\r'

lexer = lex.lex()

# for line in sys.stdin:
#     lexer.input(line)
#     for tok in lexer:
#         print(tok)