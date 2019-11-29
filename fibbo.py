
def generate_fibbo(iteration):
    offset=0
    increment=1
    fibbo_list=[]
    for i in iteration:
        fibbo_list.append(offset)
        offset,increment=increment,increment+1

    print('Fibbo list',fibbo_list)

print('Enter the number of iteration')
iteration=input()
print('Limit: ', iteration)
generate_fibbo(iteration)
