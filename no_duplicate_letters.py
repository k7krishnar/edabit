def no_duplicate_letters(phrase):
    flag=True
    for word in phrase.split(' '):
        print(word) # for ref
        if len(word) > len(set(word)):
            flag=False
    print(flag) # for ref
    return flag

no_duplicate_letters("Easy does it.")
no_duplicate_letters("So far, so good.")


#other

def no_duplicate_letters(phrase):
    return all([len(set(word))==len(word) for word in phrase.lower().split(' ')])


