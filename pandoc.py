#!/usr/bin/env python3
# ----------------------------------------------------------------
# Created by: G53
# Created date: 2022-05-08
# Version = '1.0'
# ----------------------------------------------------------------
''' pandoc.py: Ficheiro de inicialização our_pandoc '''
# ----------------------------------------------------------------
from re import *
import sys
import yaml
import getopt
import os
from pandoc_par import parser, getFinfo


# f = open("samples/data.yaml", "r")

# loaded = yaml.load(f.read(), Loader=yaml.Loader)

args_filter = 'd:o:hge:'
long_args = ['help=']

t_info = {
    'files': []
}


def throw_error(msg, to_exit=False):
    print(msg, file=sys.stderr)
    if to_exit:
        exit()


def handle_input(x):
    global t_info
    info = getFinfo(x)

    try:
        sys.stdin = open(x, 'r')
    except:
        throw_error(f"template de input {x} nao encontrado!", True)

    t_info['finfo'] = info


def set_input(x: list):
    global t_info
    t_info['files'] = x


def handle_data(x):
    global t_info

    try:
        d = open(x, 'r')
    except:
        throw_error(f"Ficheiro YAML {x} nao encontrado!", True)

    t_info['yaml'] = yaml.load(d.read(), Loader=yaml.Loader)


def handle_output(x):
    f = open(x, 'w')
    sys.stdout = f


def handle_help(arg):
    print("help type:", arg)


def handle_log(file):
    f = open(file, 'a')
    sys.stderr = f


args_handler = {
    'input': handle_input,
    '-d': handle_data,
    '-o': handle_output,
    '--help': handle_help,
    '--log': handle_log,
    '-e': handle_log
}


def handle_args():
    global t_info
    optlist, args = getopt.getopt(sys.argv[1:], args_filter, long_args)
    if ('-h', '') in optlist:
        print("carregamento do help menu")
        exit()
    elif x := [arg for opt, arg in optlist if opt == '--help']:
        for h in x:
            args_handler['--help'](h)
        exit()
    '''se chegou aqui, nao tem helpers (exit...)'''
    if not args:
        throw_error(f'Arguments not defined!!', True)
    # ordena por chave do tuplo (nao faz redirect do output ate ter info toda!)
    # optlist.sort(key=lambda y : y[0])
    for opt, value in optlist:
        args_handler[opt](value)
    set_input(args)

# define pasta output
# define extensao ficheiros
# processa os argumentos, redireciona o output para o PATH+FILENAME+EXTENSAO

def hdoc():
    global t_info
    if len(sys.argv) < 4:
        print('mal construido')
        throw_error("hdoc -d <yaml_file> <template_file> ", True)
    handle_args()
    for filename in t_info['files']:
        handle_input(filename)
        parser.finfo = t_info['finfo']
        parser.yaml = t_info['yaml']
        txt = sys.stdin.read()
        result = parser.parse(txt)
        result.pp()


hdoc()
