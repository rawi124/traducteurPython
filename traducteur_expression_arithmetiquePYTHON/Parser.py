import sys

#***************************GRAMMAIRE****************************************

# Parser d unites lexicales arithmetiques

#EXPR--> Terme ResteE
#ResteE --> +Terme ResteE | -Terme ResteE | rien
#Terme --> Facteur ResteT
#ResteT -->*Facteur ResteT | rien
#Facteur --> NB | (EXPR)
#NB -- > 0|1|.......|9

#********************ALGORITHME DE DESCENTE RECURSIVE************************
x = ''
i = 0
postfixe = []
exp = []

def Expr():
    if Terme() and ResteE() :
        return 1
    else :
        return 0

def ResteT():
        global i
        global postfixe
        global exp
        if ( len(exp) > i ) :
                if (exp[i][1] == '*' or exp[i][1] == '/')  :
                        x = exp[i]
                        i = i + 1
                        if Facteur():
                                postfixe.append(x)
                                if ResteT() :
                                        return 1
                else :
                        return 1
        else :
                return 1

def Terme():
    return Facteur() and ResteT()


def Facteur():
#
#facteur() assure la validite des chaines (nb + nb) et (nb+(nb - nb))
#et non pas (nb+nb+) ou (-nb--nb)
#
        global i
        global exp
        global postfixe

        if i < len(exp) :
            if exp[i][0] == 'NOMBRE':
                postfixe.append(exp[i])
                i = i + 1
                return 1
            if exp[i][1] == '(' :
                i = i + 1
                Expr()
                if i < len(exp) and exp[i][1] == ')' :
                    i = i + 1
                    return 1
            else :
                print("erreur caractere position ",i)
                return 0
        else :
            print("erreur caractere position ",i)
            return 0

def ResteE():
    global i
    global exp
    global postfixe
    if ( len(exp) > i ) :
        if (exp[i][1] == '+' or exp[i][1] == '-')  :
            y = exp[i]
            i = i + 1
            if Terme():
                postfixe.append(y)
                if ResteE() :
                    return 1
        else :
            return 1
    else :
        return 1

def parser(l):
#parser prend en entrée une liste "d'unités lexicales" et renvoie la liste en notation postfixée
    global postfixe
    global exp
    global i

    exp = l
    if Expr() :
        return postfixe    #postfixe est la sortie de notre analyseur syntaxique
