from operator import mul



def sum_dig_prod(n):
    sum=0
    p=1
    if len(n)!=1:
        for i in n:
            sum=sum+i
        if sum>9:
            for s in range(1,len(str(sum))):
                print(str(sum)[s])

    print(sum)
    print(p)


sum_dig_prod ([16,28])



