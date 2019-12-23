#
def encrypt(word):
	w=word[-1::-1].replace('a','0').replace('e','1').replace('o','2').replace('u','3')
	return w+'aca'


#optimal
	return word[::-1].translate(word.maketrans("aeou","0123")) + "aca"