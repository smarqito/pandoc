#!/usr/bin/env python3
# ----------------------------------------------------------------
# Created by: G57@PL
# Created date: 2022-05-08
# Version = '1.0'
# ----------------------------------------------------------------
''' pandoc.py: Ficheiro de inicialização our_pandoc '''
# ----------------------------------------------------------------
from re import *
import sys
import yaml
import json
import getopt
import os
from pandoc_par import parser, getFinfo
from aux import throw_error


args_filter = 'i:o:d:hgl:t:f:cj:'
long_args = ['help=', 'log=', 'oc=', 'cc=']
rootdir = False
outdir = False
stdin = False
stdout = False
t_info = {
    'input': {
        'path': '',
        'fname': '',
        'ext': ''
    },
    'output': {
        'path': '',
        'fname': '',
        'ext': ''
    },
    'files': [],
    'finfo': {
        'path': '',
        'fname': '',
        'ext': ''
    },
    'comments' : {
        'out' : False,
        'prefix': '',
        'suffix' : ''
    }
}


def getoutdir(path) -> dict:
    m = search(
        r"(?P<path>\/?(?:\w+\/)*)(?P<fname>[^\\\/;:\"?<>|]*)(?P<ext>\.\w+)$", path)
    if m:
        return {
            'path': m['path'],
            'fname': m['fname'],
            'ext': m['ext']
        }
    elif m := search(
        r"(?P<path>\/?(?:\w+\/)*)(?P<fname>[^\\\/;:\"?<>|]*)$", path):
        return {
            'path': m['path'],
            'fname': m['fname'],
            'ext': ''
        }
    else:
        m = search(
            r"(?P<path>[^\\;:\"?<>|]+)$", path)
        return {
            'path': m['path'],
            'fname': '',
            'ext': ''
        }


def build_path(filename):
    t_info['finfo']['fname'] = filename


def handle_input(x):
    global t_info
    # info = getFinfo(x)
    info = getFinfo(x)
    t_info['finfo'] = info

    if rootdir:
        t_info['finfo']['path'] = t_info['input']['path']
        t_info['finfo']['fname'] = info['fname']
    else:
        t_info['input']['path'] = info['path']
        t_info['input']['ext'] = info['ext']

    t_info['finfo']['ext'] = info['ext']
    try:
        sys.stdin = open(t_info['input']['path'] +
                         t_info['finfo']['fname'] + info['ext'], 'r')
    except:
        throw_error(f"template de input {x} nao encontrado!", True)


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

def handle_json(x):
    global t_info

    try:
        d = open(x, 'r')
    except:
        throw_error(f"Ficheiro YAML {x} nao encontrado!", True)

    t_info['yaml'] = json.loads(d.read())


def handle_output(x):
    info = getoutdir(x)
    path = ''
    if outdir:
        if t_info['output']['ext']:
            path = t_info['output']['path'] + \
                info['fname'] + t_info['output']['ext']
        else:
            path = t_info['output']['path'] + info['fname'] + info['ext']
    else:
        path = t_info['output']['path'] + info['fname'] + info['ext']
    f = open(path, 'w')
    sys.stdout = f


def handle_help(arg):
    path = 'assets/'+arg+'.txt'
    if os.path.isfile(path):
        f = open(path, 'r')
        print(f.read())
    else:
        throw_error(f"There is no help for searched topic: {arg}")

def help_menu():
    f = open('assets/manual.txt', 'r')
    print(f.read())


def handle_log(file):
    f = open(file, 'a')
    sys.stderr = f


def handle_outdir(path):
    global outdir
    t_info['output'] = getoutdir(path)
    if not os.path.exists(t_info['output']['path']):
        os.mkdir(t_info['output']['path'])
    outdir = True


def handle_indir(path):
    global rootdir
    t_info['input']['path'] = path
    rootdir = True

def handle_comments(value):
    global t_info
    t_info['comments']['out'] = True

def handle_ocomment(value):
    global t_info
    handle_comments('')
    t_info['comments']['prefix'] = value

def handle_ccomment(value):
    global t_info
    handle_comments('')
    t_info['comments']['suffix'] = value

args_handler = {
    'input': handle_input,
    '-i': handle_data,
    '-j': handle_json,
    '-l': handle_log,
    '-o': handle_output,
    '-t': handle_outdir,
    '-f': handle_indir,
    '-c': handle_comments,
    '--help': handle_help,
    '--log': handle_log,
    '--oc' : handle_ocomment,
    '--cc' : handle_ccomment,
}


def handle_opts():
    global t_info, stdin
    optlist, args = getopt.getopt(sys.argv[1:], args_filter, long_args)
    if ('-h', '') in optlist:
        help_menu()
        exit()
    elif x := [arg for opt, arg in optlist if opt == '--help']:
        for h in x:
            args_handler['--help'](h)
        exit()
    '''se chegou aqui, nao tem helpers (exit...)'''
    if not args:
        stdin = True
    # ordena por chave do tuplo (nao faz redirect do output ate ter info toda!)
    # optlist.sort(key=lambda y : y[0])
    for opt, value in optlist:
        if opt == '-c':
            value = ''
        args_handler[opt](value)
    set_input(args)

# define pasta output
# define extensao ficheiros
# processa os argumentos, redireciona o output para o PATH+FILENAME+EXTENSAO


def parse(txt):
    result = parser.parse(txt)
    result.pp()


def hdoc():
    global t_info
    global outdir, stdin
    handle_opts()
    if not t_info['yaml']:
        print('mal construido')
        throw_error("hdoc -d <yaml_file> <template_file> ", True)
    parser.yaml = t_info['yaml']
    parser.comments = t_info['comments']
    for filename in t_info['files']:
        handle_input(filename)
        if outdir:
            handle_output(filename)
        parser.finfo = t_info['finfo']
        txt = sys.stdin.read()
        parse(txt)
    if stdin:
        if outdir:
            handle_output("default")
        else:
            t_info['finfo']['path'] = ""
        parser.finfo = t_info['finfo']
        parse(sys.stdin.read())


hdoc()
