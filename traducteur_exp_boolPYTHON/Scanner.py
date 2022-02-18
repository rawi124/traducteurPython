##############################################
#
# scanner.py
# ----------
#
# Analyseur lexical d expression Booléennes
#
#
# I53 - Compilation et theorie des langages
#
###############################################

"""
la fonction scanner prendra en entrée une chaîne de caractères et
renvoie une liste d'unités lexicales
"""
def scanner(s):
	i = 0
	l = []
	ch = ""
	while i < len(s) :
		if (s[i]== 'O' and s[i+1] == 'U') or(s[i]== 'E' and s[i+1] == 'T')  :
			ch  =s[i]+s[i+1]
			l.append(('OP',ch))
			i = i + 2
		elif s[i]== 'N' and s[i+1] == 'O' and s[i+2] =='N':
			ch  =s[i]+s[i+1]+s[i+2]
			l.append(('OP',ch))
			i = i + 3
		elif s[i] =='(':
			l.append(('PAR_OUV',s[i]))
			i = i + 1
		elif s[i] ==')':
			l.append(('PAR_FER',s[i]))
			i = i + 1
		elif s[i] == 'V' or s[i] == 'F' :
			j = i
			ch = ""
			while (j<i+4):
				ch = ch+s[j]
				j = j + 1
			if ch == 'VRAI' or ch == 'FAUX':
				l.append(('BOOL',ch))
			else :
				print("verifie syntaxe de vrai ou faux pres du charactere ",i)
				return 0
			i = i + 4
		elif s[i] == " " :
			i = i + 1
		else :
			print("erreur syntaxe verifiez votre expression ")
			return 0
	return l   # la liste d'unites lexicales
