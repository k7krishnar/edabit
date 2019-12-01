def is_isogram(txt):
    if txt:
        input_list=list(txt)
        input_set=set(txt)
        print(input_list,len(input_list),input_set,len(input_set))
        if len(input_list) == len(input_set):
            print('True')
            return True
        else:
            print('False')
            return False
    else:
        return False


# test case
is_isogram("PasSword")