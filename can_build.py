def can_build(lst):
    l=len(lst)
    print(l)
    last=l-1
    lastbut1=l-2
    check=True
    print(lst[last],lst[lastbut1])
    for i in range(1,l):
        if lst[lastbut1] in lst[last] and len(lst[last]) == len(lst[lastbut1])+1:
            print ( lst[lastbut1] + " exists in " + lst[last] )
            last-=1
            lastbut1-=1
            print("True")
        else:
            check=False
            print("False")
    return check

can_build(["it", "bit", "bite", "biters"])
can_build ( ["a","at","ate","late","plate","plates"] )
can_build(["a", "at", "ate", "late", "plate", "plater", "platter"])


#other
https://edabit.com/challenge/zQespQxTsiGoeMNP3