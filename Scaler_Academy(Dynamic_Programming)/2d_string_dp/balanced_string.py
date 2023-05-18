# balanced string

s = str(input())

l = set(s)

p = [s.count(i) for i in l]

print(sorted(p)==sorted(p,reverse=True))