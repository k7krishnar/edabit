def accumulating_product(lst):
    res = []
    if len ( lst ) == 0:
        return []
    else:
        for l in lst:
            print(l)
            if len(res)==0:
                res.append(l)
            else:
                res.append(l*res[-1])
    print(res)

accumulating_product([1,2,3,4])