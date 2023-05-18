'''
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
'''

def long_palindrome(re_str):
    sm_lst=[]
    for i in range(2,len(re_str)+1):
        sm_lst.append(re_str[:i])

    req_list=[]
    for i in sm_lst:
        if(i==i[::-1]):
            req_list.append(i)

    req_list2=[]
    req_list2=sorted(req_list)

    print(max(req_list2))


nm=input("Enter the string sequence: ")
long_palindrome(nm)


