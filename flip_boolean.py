def reverse(arg):
    if isinstance(arg, bool):
        if arg == True:
            print ( "False" )
            return False

        else:
            print("True")
            return True
    print("boolean expected")
    return "boolean expected"

reverse(False)
reverse(0)
reverse({})

# best solution
def reverse(arg):
	return "boolean expected" if not isinstance(arg, bool) else not arg