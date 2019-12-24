#
def encrypt(word):
	w=word[-1::-1].replace('a','0').replace('e','1').replace('o','2').replace('u','3')
	print(w+'aca')
	return w+'aca'


#optimal

def encrypt1(word):
	print( word[::-1].translate ( word.maketrans ( "aeou","0123" ) ) + "aca")
	return word[::-1].translate(word.maketrans("aeou","0123")) + "aca"

encrypt("hello")
encrypt1("hello")