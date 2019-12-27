def combinations(*items):
    output = 1
    for i in items:
        if i != 0:
            output *= (i)

    print(output)
    return output

combinations(2,3,0)


# other
from numpy import prod
def combinations(*a):
	return prod([x for x in a if x>0])

import operator
import functools

def combinations(*items):
	return functools.reduce(operator.mul, [i for i in items if i > 0])