#!/usr/bin/env python3 
#----------------------------------------------------------------
# Created by: G53
# Created date: 2022-05-08
# Version = '1.0'
#----------------------------------------------------------------
''' pandoc.py: Ficheiro de inicialização our_pandoc '''
#----------------------------------------------------------------
from re import *
import sys
import yaml
import getopt

f = open("samples/data.yaml", "r")

loaded = yaml.load(f.read(), Loader=yaml.Loader)

print(loaded["doe"])
