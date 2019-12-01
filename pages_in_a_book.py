def pages_in_book(total):
    if (total is None) or (int(total) == 0) :
        print('input is none or zero') # for ref
        return False
    else:
        print('input is',total) # for ref
        sum_list = []
        for item in range(0,total+1):
            sum=((item*(item+1))//2)
            if sum <= total:
                sum_list.append(sum)
            else:
             break;
        if total in sum_list:
            print('Valid sum of pages') # for ref
            return True
        else:
            print('Invalid sum of pages') # for ref
            return False

# Test cases
pages_in_book(None)
pages_in_book(4005)
pages_in_book(5)















