#!/bin/bash
echo '#############################'
echo '        Exemplo default'
echo '#############################'
pandoc.py -i samples/info.yaml samples/ex1.in

rm -r __pycache__ parser.out parsetab.py