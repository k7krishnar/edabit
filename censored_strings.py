
def uncensor(txt, vowels):
    v = ([v for v in vowels])
    t1=txt
    for i in range(1,txt.count('*')+1):
        print(i)
        t1=txt.replace('*',v.pop(0),1)
        txt=t1
    print(t1)

# test case
uncensor ( 'Wh*r* d*d my v*w*ls g*?','eeioeo')
uncensor('abcd', '')

# elegant
def uncensor(t, v):
    for c in v: t = t.replace('*', c, 1)
    return t

def uncensor(txt, vowels):
    return txt.replace('*', '{}').format(*vowels)

