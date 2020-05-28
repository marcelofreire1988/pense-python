#EXERCICIO 1

#1 forma:

def do_twice(s):
    print(" "* 65 + s)

do_twice('monty')

# 2 forma:


def do_twice(s):
    print(s)

do_twice(" " * 65 + 'monty')


#EXERCICIO 2

def do_twice(of, v):
    of(v)
    of(v)

def print_twice(v):
    print('spam')
    print('spam')

def do_four(of, v):
    do_twice(of, v)
    do_twice(of, v)


do_twice(print,'spam')

do_four(print, 'spam')


#EXERCICIO 3


def linha():
    print("+","-" * 4,"+","-" * 4, "+", end=' ')
    print()
def colunas():
    print("|", " " * 4, "|"," " * 4, "|")
    print("|", " " * 4, "|"," " * 4, "|")
    print("|", " " * 4, "|"," " * 4, "|")

def linha_coluna():
    linha()
    colunas()
    linha()
    colunas()
    linha()

linha_coluna()
