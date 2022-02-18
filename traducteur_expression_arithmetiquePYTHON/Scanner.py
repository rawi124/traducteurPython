##############################################
#
# scanner.py
# ----------
#
# Analyseur lexical d expression arithmetique
#
#
# I53 - Compilation et theorie des langages
#
###############################################

'''
NB --> [0-9]+
OP --> + | - | * | /
PO  --> (
PF  --> )
'''

#
#la fonction scanner prendra en entrée une chaîne de caractères et
#renvoie une liste d'unités lexicales
#
def scanner(s):
	l = []
	i = 0
	ch = ""
	while i < len(s) :  # parcourir la chaine de caractere s
		if s[i] == " ":
			i = i + 1
		elif s[i].isnumeric() :
			ch = s[i]
			i = i + 1
			while(i < len(s) and s[i].isnumeric() ):
				ch = ch + s[i]
				i = i + 1
			l.append(('NOMBRE',ch))
		elif s[i] in ['+','-','*','/']:
			l.append(('OP',s[i]))
			i = i + 1
		elif s[i] =='(':
			l.append(('PAR_OUV',s[i]))
			i = i + 1
		elif s[i] ==')':
			l.append(('PAR_FER',s[i]))
			i = i + 1
		elif s[i] == "." :
			print("on ne gere que les entiers ")
			return 0
		elif s[i] == "%":
			print("on ne gere pas la division modulaire")
			return 0
		else :
			print("erreur syntaxe verifiez votre expression pres du caractere ",i)
			return 0
	return l  # la liste d'unites lexicales
