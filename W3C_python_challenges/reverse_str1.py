def reverse(x):
    if(x>=0):
        st=str(x)
        st2 = st[::-1]
        
    s = str(x)
    s2 = s[::-1]
    n = int(s2)

    if (n >= 0):
        return n
    else:
        return "-" + str(n)

n = -431

print(reverse(n))