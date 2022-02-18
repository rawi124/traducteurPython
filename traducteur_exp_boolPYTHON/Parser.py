#***************************GRAMMAIRE****************************************

# Parser d unites lexicales Booléennes

#************************************************************************
x = ''
i = 0
postfixe = []
exp = []
import sys


def Expr():
	if Terme() and ResteE() :
		return 1
	else :
		return 0

def ResteT():
		global i
		if ( len(exp) > i ) :
			if (exp[i][1] == 'ET')  :
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
	 #facteur() assure la validite des chaines (NON BOOL) et (NON(NON BOOL))
	 #et non pas (NON BOOL NON) ou (NON BOOL BOOL)
	 #
		global i
		if (i < len(exp)) :
			if exp[i][0] == 'BOOL' :
				postfixe.append(exp[i])
				i = i + 1
				return 1
			if exp[i][1] == '(' :
				i = i + 1
				Expr()
			if exp[i][1] == ')' :
				i = i + 1
				if ResteE():
					return 1
				elif ResteT() :
					return 1
			if exp[i][1] == 'NON':
				y = exp[i]
				i = i + 1
				if Facteur() :
					postfixe.append(y)
					return 1
			else :
				i = i + 1
				Expr()
				return 1
		else :
			print('erreur caractere ',i)
			return 0

def ResteE():
	global i
	if ( len(exp) > i ) :
		if (exp[i][1] == 'OU')  :
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
	#parser prend en entrée une liste "d'unités lexicales" et renvoie la liste en notation postfixée.
	global postfixe
	global exp
	global i
	exp = l
	if Expr() :
		return postfixe   #postfixe est la sortie de notre analyseur syntaxique
	else :
		sys.stderr.write("erreur à la position " + str(i) + ": caractère " + exp[i-1][1] + " invalide\n")
		return 0
