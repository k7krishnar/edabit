def index_of_caps(word):
    icap = []
    lenw = len ( word )
    for w in range ( 0,lenw,1 ):
        print(w,word[w])
        if word[w].isupper():
            icap.append ( w )
    print(icap)
    return icap
index_of_caps("Fuck")

def count_ones(num):
    b=bin(num)[2:]


    print(type(b))
count_ones(12)

def list_of_multiples (num, length):
    print([ c for c in range(num,(num*length)+1,num)])

list_of_multiples(7, 5)




def sort_by_length(lst):
    l1=[]
    for l in lst:
        l1.append(len(l))

    d= dict ( zip ( l1,lst ) )
    print(d)
    print(sorted(d.values(),key=))
    return sorted(d.values(),reverse=True)

sort_by_length(["Google", "Apple", "Microsoft"])
sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"])
sort_by_length(["Turing", "Einstein", "Jung"])
sort_by_length(["Tatooine", "Hoth", "Yavin", "Dantooine"])
sort_by_length(["Mario", "Bowser", "Link"])







