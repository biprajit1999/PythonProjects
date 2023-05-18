from itertools import *

def long_common_str(st1,st2):
    l1=list(permutations(st1,len(st1)))+list(permutations(st1,len(st1)-1))
    l2=list(permutations(st2,len(st2)))+list(permutations(st2,len(st2)-1))

    l3=[]
    for i in l1:
        l3.append(''.join(i))

    l4=[]
    for i in l2:
        l4.append(''.join(i))

    l5=[]
    for i in l3:
        if i in l4:
            l5.append(i)

    print(l5)
    print(max(l5))

st1=input("Enter 1st string: ")
st2=input("Enter 2nd string: ")

long_common_str(st1,st2)