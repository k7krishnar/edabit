def concat(*args):
    join_list=[]
    for i in args:
        join_list=join_list+i

    print(join_list) # for ref
    return join_list


# test
concat([1, 2], [3, 4], [1, 2, 3, 4] )

# top answers
def concat(*args):
    print(sum(args, []))
    return sum(args, [])

concat([1, 2], [3, 4], [1, 2, 3, 4])

def concat(*args):
    print([a for arg in args for a in arg]) # for ref
    return [a for arg in args for a in arg]

concat([1, 2], [3, 4], [1, 2, 3, 4] )