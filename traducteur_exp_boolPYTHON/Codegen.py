#!/usr/bin/python

##############################################
#
# codegen.py
# __________
#
# Producteur de code Python de notation postfixee
#
# I53 - Compilation et theories des langages
##############################################

'''
codegen prend en paramètres la sortie (postfixe) de l'analyseur syntaxique
et produit un code de ce type:

t1 = True
t2 = False
t1 = t1 and t2
print(t1)
'''
def codegen(postfixe):
	i = 0
	c ="#!/usr/bin/python3\n"
	for el in postfixe : #parcourir la liste d'unites lexicales 
		if el[1] == 'VRAI':
			i = i + 1
			c = c + "t" + str(i) + " = " + "True" + "\n"
		elif el[1] == 'FAUX' :
			i = i + 1
			c = c + "t" + str(i) + " = " + "False" + "\n"
		else :
			i = i - 1
			if el[1] == 'OU':
				c = c + "t" + str(i) + " = " + "t" + str(i)+" "+'or' + " t" + str(i+1) + "\n"
			elif el[1] == 'ET' :
				c = c + "t" + str(i) + " = " + "t" + str(i)+" "+'and' + " t" + str(i+1) + "\n"
			elif el[1] == 'NON' :
				i = i + 1
				c = c + "t" + str(i) + " = " + "not "+"t" + str(i) + "\n"
	c = c + "print(t1)\n"
	return c  # c une chaîne de caractères correspondant au code à 3 adresses de l'expression
