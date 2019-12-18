def counterpartCharCode(char):
	if char.islower():
		print(ord(char.upper()))
		return ascii(char.upper())
	else:
		print(ascii(char.lower()))
		return ascii(char.lower())

# test case
counterpartCharCode("a")

# better solution
def counterpartCharCode(char):
	return ord(char.swapcase())


def filter_list(l):
	print( [ i for i in l if type(i) == type(1)])

filter_list(["A", 1, '&amp', 0, -9, 'Edabit'])

cat="cat"
print(reversed("cat"))


def is_symmetrical(num):
	if str(num) == str(num)[::-1]:
		print( "True" )
		return True
	else:
		print("Flase")
		return False

is_symmetrical(123)
is_symmetrical(111)


def alphabet_soup(txt):
	print(''.join(sorted(txt)))

alphabet_soup("hello")
