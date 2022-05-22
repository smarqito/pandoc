#!/bin/bash
echo '#############################'
echo '            BEM VINDO        '
echo '  SCRIPT DE TESTES GRUPO 57  '
echo '#############################'
echo ''
clean=false


function clean() {
    rm -r __pycache__ parser.out parsetab.py
}
case $1 in
    "default")
    echo '#############################'
    echo '        Exemplo default      '
    echo 'pandoc.py -i samples/info.yaml samples/ex1.in'
    echo '#############################'
    echo ''
    pandoc.py -i samples/info.yaml samples/ex1.in
    clean
    ;;
    "help")
    echo '#############################'
    echo '        Exemplo help         '
    echo 'pandoc.py -h                 '
    echo '#############################'
    echo ''
    pandoc.py -h
    clean
    ;;
    "input")
    echo '##############################'
    echo '        Exemplo redirect input'
    echo 'pandoc.py -i samples/info.yaml -f samples/ ex1.in'
    echo '##############################'
    echo ''
    pandoc.py -i samples/info.yaml -f samples/ ex1.in
    clean
    ;;
    "output")
    echo '##############################'
    echo '        Exemplo redirect output'
    echo 'pandoc.py -i samples/info.yaml -t' $2/$3 'ex1.in'
    echo '##############################'
    echo ''
    pandoc.py -i samples/info.yaml -t $2/$3 samples/ex1.in
    clean
    ;;
    "comments")
    echo '##############################'
    echo '        Exemplo redirect output & print comments'
    echo 'pandoc.py -i samples/info.yaml -t' $2/$3 'ex1.in'
    echo '##############################'
    echo ''
    pandoc.py -i samples/info.yaml -t $2/$3 --oc=$4 --cc=$5 samples/ex1.in
    clean
    ;;
    "html")
    echo '##############################'
    echo '        Exemplo html'
    echo 'pandoc.py -i samples/info2.yaml -t www/.html --oc='<!--' --cc='-->' samples/default.html
    echo '##############################'
    echo ''
    pandoc.py -i samples/info2.yaml -t www/.html --oc='<!--' --cc='-->' samples/default.html
    clean
    ;;
esac