def uncensor1(txt, vowels):
    un=[]
    v=([ v for v in vowels])
    for t in txt.split(" "):
        for i in range(1,t.count('*')+1):
            print(i)
            t=t.replace('*',v.pop(0),1)
            print(t)

    print(''.join(t))

def uncensor(txt, vowels):
    v = ([v for v in vowels])
    t1=txt
    for i in range(1,txt.count('*')+1):
        print(i)
        t1=txt.replace('*',v.pop(0),1)
        txt=t1
    print(t1)

uncensor ( 'Wh*r* d*d my v*w*ls g*?','eeioeo')
uncensor('abcd', '')



