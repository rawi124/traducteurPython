#!/usr/bin/python

import Scanner, Parser, Codegen
import sys, os, stat

if __name__ == "__main__":
    fichier = open(sys.argv[1], 'r')
    expression = fichier.read().strip()
    print("expression a avaluer :",expression)
    #on fait un print de expression pour mieux voir l'expression
    #a l execution de compilo.py
    l = Scanner.scanner(expression)
    postfixe = Parser.parser(l)
    code = Codegen.codegen(postfixe)
    out = open("a.out", 'w')
    out.write(code)
    os.chmod("a.out", stat.S_IRWXU)
