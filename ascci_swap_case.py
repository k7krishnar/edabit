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