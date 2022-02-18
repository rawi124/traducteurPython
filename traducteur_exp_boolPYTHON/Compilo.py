#!/usr/bin/python

import Scanner, Parser, Codegen
import sys, os, stat

if __name__ == "__main__":
    fin = open(sys.argv[1], 'r')
    expression = fin.read().strip()
    print(expression)
    lexs = Scanner.scanner(expression)
    postfixe = Parser.parser(lexs)
    code = Codegen.codegen(postfixe)
    out = open("a.out", 'w')
    out.write(code)
    os.chmod("a.out", stat.S_IRWXU)
