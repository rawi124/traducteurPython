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

t1 = 9
t2 = 5
t3 = 2
t2 = t2 + t3
t1 = t1 - t2
print (t1)
'''
def codegen(postfixe):
	i = 0
	c ="#!/usr/bin/python3\n"
	for el in postfixe :  #parcourir la liste d'unites lexicales 
		if el[0] == 'NOMBRE' :
			i = i + 1
			c = c + "t" + str(i) + " = " + str(el[1]) + "\n"
		else :
			i = i- 1
			c = c + "t" + str(i) + " = " + "t" + str(i)+" "+str(el[1]) + " t" + str(i+1) + "\n"
	c = c + "print(t1)\n"
	return c   # c une chaîne de caractères correspondant au code à 3 adresses de l'expression
