def gcd(n1, n2):
    d1=[d for d in range(1,n1+1,1) if n1%d ==0 ]
    d2=[d for d in range(1,n2+1,1) if n2%d ==0 ]
    print(d1)
    print (d2)
    print(max(set(d1) & set(d2)))

gcd(8, 12)