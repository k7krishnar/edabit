def hamming2(x,y):
    """Calculate the Hamming distance between two bit strings"""
    assert len(x) == len(y)
    count,z = 0,int(x,2)^int(y,2)
    print(int(x,2))
    print(int(y,2))
    print(int(x,2)^int(y,2))
    while z:
        print('count before',count)
        print ( 'z before',z )
        count += 1
        z &= z-1 # magic!
        print ( 'count after',count )
        print ( 'z after',z )



hamming2("0001","1101")