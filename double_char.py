def double_char(txt):
    double_list=[]
    for item in range(0,len(txt),1):
        double_list.append(2*txt[item])

    print(''.join(double_list)) # for ref
    return (''.join(double_list))

# test
double_char("1234!_ ")

# best solution
def double_char(txt):
    return ''.join([c * 2 for c in txt])


