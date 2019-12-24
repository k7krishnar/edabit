
def pentagonal(num):
    c=num
    sum=0
    while c > 1:
        sum=sum+(c-1)*5
        c-=1
    print(sum+1)
    return sum+1


#test cases

pentagonal(21)
pentagonal(13)

# top answer


def pentagonal(num):
    print([ sumi for i in range(1,num)])