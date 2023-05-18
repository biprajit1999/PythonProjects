def lcs(str1,str2,m,n):
    if(m==0 or n==0):
        return 0
    elif(str1[m-1] == str2[n-1]):
        return 1+lcs(str1,str2,m-1,n-1)
    else:
        return max(lcs(str1,str2,m-1,n),lcs(str1,str2,m,n-1))

st1 = "debakshi"
st2 = "biprajit"

print("Length of LCS is ",lcs(st1,st2,len(st1),len(st2)))
