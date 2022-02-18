import sys
import Parser
import Scanner
import Codegen
import Compilo
################################
_scanner = 1
_parser = 1
_codegen = 1
_compilo = 1
#################################
test_scanner = ["FAUX ET VRAU", "FAUX XOR VRAI", "FAUX AND VRAI","FAUX ET NON ( VRAI OU FAUX)" ]
test_parser =  [[('BOOL', 'VRAI'), ('OP', 'OU'),('BOOL', 'FAUX'), ('OP', 'ET'),('PAR_OUV', '('), ('BOOL', 'FAUX'), ('OP', 'OU'), ('OP', 'NON'), ('BOOL', 'VRAI'),('PAR_FER', ')')]]
test_codegen =  [[('BOOL', 'VRAI'), ('BOOL', 'FAUX'), ('OP', 'ET')]]
test_compilo  = ['tests/fichier.txt','tests/fichier1.txt','tests/fichier2.txt','tests/fichier3.txt','tests/fichier4.txt']
#################################

import os

try:
    import Scanner
except:
    print("fichier Scanner.py absent")
    _scanner = 0

try:
    import Parser
except:
    print("fichier Parser.py absent")
    _parser = 0

try:
    import Codegen
except:
    print("fichier Codegen.py absent")
    _codegen = 0

try:
    import Compilo
except:
    print("fichier compilo.py absent")
    _compilo = 0


if _scanner:
    input("=========================\nTest de la fonction scanner\n=========================\n")
    for case in test_scanner:
        print("==test case: '{}'  ==\n".format(case))
        print(Scanner.scanner(case))

if _parser:
    input("=========================\nTest de la fonction parser\n=========================\n")
    for case in test_parser:
        print("==test case: '{}'  ==\n".format(case))
        print(Parser.parser(case))

if _codegen:
    input("=========================\nTest de la fonction codegen\n=========================\n")
    for case in test_codegen:
        print("==test case: '{}'  ==\n".format(case))
        print(Codegen.codegen(case))

if _compilo:
    input("=========================\nTest du compilateur\n=========================\n")
    for case in test_compilo:
        os.system('rm a.out')
        print("==test case: '{}'  ==\n".format(case))
        print("expression a evaluer  : ")
        os.system("python3 Compilo.py {}".format(case))
        os.system("./a.out")
