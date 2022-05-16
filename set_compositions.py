##CODE CREATED BY RAUL PENAGUIAO
##May 2022


"""
Some code related to set composition operations
It includes a generation of set compositions with parts on a list

"""



"""
PREP
P: list of (presumably distinct) elements to build set compositions on
These are all strings that do not contain , or |
R: a tuple of all set compositions, of the form "a,b|c,d|e", for instance

"""
def generate_set_compositions(parts):
    l = len(parts)
    if parts == []:
        return ("",)
    if l == 1:
        return (parts[0],)
    if l == 2:
        return (parts[0] + "," + parts[1], parts[0] + "|" + parts[1], parts[1] + "|" + parts[0])
    #select a non empty sublist of parts
    #for each sublist, consider all set composutions built from its compliment, plus a first term that contains the chosen set
    #LOOP over non-empty subsets of parts
    #this non-empty set will be represented by an integer in with l bits
    #an element part[i] is in it if if%pow2[i] == 0
    it = 1
    pow2 = [1]
    #pow2[i] = 2^(i+1)
    for i in range(1, l+1):
        pow2+= [pow2[-1] * 2]
    ans_list = []
    #print(pow2)
    while it < pow2[-1]-1:
        #build the set S and it's complement C
        S = []
        C = []
        for i in range(l):
            if (it//pow2[i])%2 == 1:
                S += [parts[i]]
            else:
                C += [parts[i]]
        #print("it = ", it)
        #print("S = ", S)
        #print("C = ", C)
        first_set = ",".join(S)
        #print("first_set = ", first_set)
        ans_list += [first_set + "|" + small_set_composition for small_set_composition in generate_set_compositions(C)]
        it += 1
    ans_list += [",".join(parts)]
    return (set_comp for set_comp in ans_list)


#composition function underlying to a set composition
#it returns a composition in the form of a list
def alpha(set_comp):
    return [len(part.split(",")) for part in set_comp.split("|")]




if __name__ == "__main__":
    set_comps = generate_set_compositions(["1", "2", "3"])
    for s in set_comps:
        print(s)
        print(alpha(s))
