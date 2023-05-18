def Sample(n):
    i = 0
    s = 0
    while( n > 0 ):
        r = n % 10
        p = 8^i
        s = s + p*r
        i = i+ 1
        n = n / 10
    return s

n=5
print(Sample(n))